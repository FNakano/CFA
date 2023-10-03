# Como usar Docker?

> Docker is an open platform for developing, shipping, and running applications. (https://docs.docker.com/get-started/overview/)

... então, os usos mais básicos de Docker são:

1. Construir uma aplicação;
2. Executar a aplicação construída.

A aplicação é construída com comandos do tipo `docker build -t getting-started` (https://docs.docker.com/get-started/02_our_app/#build-the-apps-image)

A aplicação é executada com comandos do tipo `docker run -dp 127.0.0.1:3000:3000 getting-started` (https://docs.docker.com/get-started/02_our_app/#start-an-app-container)

No exemplo (https://docs.docker.com/get-started/02_our_app/), a aplicação se chama `getting-started`. Mesmo nome dado ao arquivo, imagem, *container* que contém a aplicação.

Até aqui, não é muito diferente de `python -m flask --app hello run` (https://flask.palletsprojects.com/en/3.0.x/quickstart/)

... inclusive porque o exemplo do Docker *levanta* um servidor web e essa linha de comando do Python também *levanta* um servidor web.

A pegada está em como é feito e que características tem cada um dos jeitos. Vou escrever sobre o Docker e deixar a parte Python para o leitor interessado (inclusive porque explicar Python e Flask não é a proposta deste texto).

> Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production. (https://docs.docker.com/get-started/overview/)

A característica que ressaltam na citação acima é que Docker permite separar aplicações de infraestrutura. Aplicação é como o servidor do exemplo, infraestrutura é conjunto de programas que precisam estar rodando para a aplicação poder rodar. Usando linguagens e motores de tempo de execução como exemplo, Docker torna possível que se atualize, na infraestrutura, Python 2 para Python 3 ou; Java 8 para Java 11, sem *quebrar* a aplicação (desde que a atualização não quebre o Docker). A mesma característica permite criar uma aplicação única que pode ser executada em diferentes infraestruturas (desde que tenha Docker nelas). Ié a mesma aplicação roda no Linux, no MacOS e no Windows. **nota**: Isso é possível porque o container não usa as ferramentas da infraestrutura. As ferramentas necessárias à aplicação também estão no *container*.

Essa característica, um tipo de portabilidade da aplicação que é muito desejada em desenvolvimento e implantação de programas, é obtida através do uso de *containers*. 

> A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. (https://www.docker.com/resources/what-container/)

Então, `getting-started`, que é um arquivo, representa um *container*, e contém a aplicação e toda a infraestrutura necessária para executá-la. A infraestrutura de suporte para o *container* é Docker que, por sua vez, é executado sobre um (algum) Sistema Operacional.

## Como especificar e construir containers (imagens)

*Containers* são construídos com o comando `docker build ...`. Este comando lê a especificação armazenada em um arquivo de nome `Dockerfile`. Copio abaixo o `Dockerfile` do exemplo:
	
```
# syntax=docker/dockerfile:1

FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```

Superficialmente (porque ainda é até onde consigo ir), a aplicação é construída a partir da (FROM) imagem node:18-alpine (https://hub.docker.com/_/alpine
). Essa imagem já vem com Node.js instalado. Sobre essa imagem é executada e gravada a execução de `yarn ..` (RUN). Quando a aplicação é executada, com `docker run ...`, o *container* é carregado e o comando `node src/index.js` é executado. Nessa aplicação a porta 3000 deve estar aberta (EXPOSE).

A documentação para os comandos em letras maiúsculas está em https://docs.docker.com/engine/reference/builder/

Yarn é um gerenciador de pacotes. Ele instala o que estiver definido no arquivo `package.json`.

## Como desenvolver incrementalmente uma aplicação com Docker

Quando desenvolvo, o desenvolvimento de uma aplicação é incremental. Se a cada incremento tiver que atualizar a imagem, aumenta significativamente o tempo para desenvolver cada incremento.

Busquei um tanto até econtrar algo que eu acho que ajuda: https://docs.docker.com/compose/gettingstarted/#step-7-update-the-application .

Nele atualiza-se o código de um servidor flask sem precisar atualizar a imagem. O que se atualiza é o arquivo contido em um volume montado na imagem.

Nesse exemplo menciona-se um `requirements.txt`. É um arquivo de dependências gerado pelo Python. Ele é usado para instalar na imagem base, que é Python, o flask e o redis. Tem um tutorial sobre o requirements em: https://www.scaler.com/topics/how-to-create-requirements-txt-python/


## Links que consultei para a parte de desenvolvimento incremental

https://docs.docker.com/develop/
https://docs.docker.com/build/building/multi-stage/
https://docs.docker.com/get-started/kube-deploy/
https://docs.docker.com/get-started/swarm-deploy/
https://docs.docker.com/compose/
https://docs.docker.com/desktop/install/linux-install/
https://docs.docker.com/desktop/faqs/linuxfaqs/#why-does-docker-desktop-for-linux-run-a-vm
https://docs.docker.com/compose/gettingstarted/
https://docs.docker.com/develop/dev-best-practices/
https://docs.docker.com/engine/reference/builder/
https://docs.docker.com/build/ci/
https://docs.docker.com/storage/volumes/
https://docs.docker.com/storage/bind-mounts/
https://www.google.com/search?q=python+create+requirements.txt&oq=python+create+requirement&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIICAIQABgWGB4yCAgDEAAYFhgeMgoIBBAAGAoYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMgoICBAAGAoYFhgeMggICRAAGBYYHtIBCDkwNTBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1
https://www.scaler.com/topics/how-to-create-requirements-txt-python/


## Conclusão

Acredito que, agora, fica mais fácil de entender o exemplo em https://docs.docker.com/get-started/02_our_app/ .

## Comentários

O exemplo dá um passo a passo do que fazer para criar e executar uma aplicação mas não deixa claro o que está no domínio de conceitos de Docker e o que está no domínio de conceitos de outras ferramentas. Por exemplo. o conteúdo clonado do github (https://github.com/docker/getting-started-app/tree/main) tem mais a ver com Yarn e (muito mais com) Node.js, que com Docker.

Ele não conta no tutorial do compose (que pretendo usar para desenvolver incrementalmente uma aplicação) que `flask` (re)carrega automaticamente a aplicação em python quando o arquivo fonte é modificado.

O [Otávio](https://github.com/bambans) indicou um outro gerenciador de containers: [Podman](https://podman.io/). Parece que a maior vantagem de Podman sobre Docker é que Podman e a imagem são executados totalmente em modo usuário. Docker tem uma parte em modo superusuário pois precisa de um daemon. Detalhes em https://hub.alfresco.com/t5/alfresco-content-services-blog/using-podman-with-alfresco/ba-p/316257 , aplicado a uma aplicação específica. 


A seguir apresento um histórico do que estudei para chegar ao resultado acima:

## Tentando entender Docker (ou, puxando um pelo, aparecendo o gato, entendendo o gato)

Links que consultei:

https://www.google.com/search?q=docker+simple+tutorial&oq=docker+simple+tutorial&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABgTGBYYHjIKCAIQABgTGBYYHjIKCAMQABgTGBYYHjIKCAQQABgTGBYYHjIKCAUQABgTGBYYHjIKCAYQABgTGBYYHtIBCTExNzM5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://www.docker.com/101-tutorial/
https://docs.docker.com/get-started/02_our_app/
https://github.com/docker/getting-started-app/tree/main/src
https://www.google.com/search?q=what+is+docker+alpine%3A18&oq=what+is+docker+alpine%3A18&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCjE4MjM1ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8
https://hub.docker.com/layers/library/node/18-alpine/images/sha256-d51f2f5ce2dc7dfcc27fc2aa27a6edc66f6b89825ed4c7249ed0a7298c20a45a?context=explore
https://hub.docker.com/_/alpine
https://alpinelinux.org/about/
https://pkgs.alpinelinux.org/packages
https://hub.docker.com/_/node/
https://www.google.com/search?q=what+is+getting-started-app+in+alpine+docker+image&oq=what+is+getting-started-app+in+alpine+docker+image&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigAdIBCTIwOTI5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://www.docker.com/blog/how-to-use-the-alpine-docker-official-image/
https://www.google.com/search?q=what+is+the+dockerfile&oq=what+is+the+dockerfile&gs_lcrp=EgZjaHJvbWUyCwgAEEUYExg5GIAEMgkIARAAGBMYgAQyCQgCEAAYExiABDIKCAMQABgTGBYYHjIKCAQQABgTGBYYHjIKCAUQABgTGBYYHjIKCAYQABgTGBYYHjIKCAcQABgTGBYYHjIKCAgQABgTGBYYHjIKCAkQABgTGBYYHtIBCTE1NzUzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://docs.docker.com/engine/reference/builder/#run
https://www.google.com/search?q=what+is+yarn&oq=what+is+yarn&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDI4MzFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://yarnpkg.com/
https://www.google.com/search?q=what+does+yarn+install+--production+do&sca_esv=569142147&ei=KXcVZcalIaLX1sQPkZqq0Ag&ved=0ahUKEwiG3pbMrM2BAxWiq5UCHRGNCooQ4dUDCBA&uact=5&oq=what+does+yarn+install+--production+do&gs_lp=Egxnd3Mtd2l6LXNlcnAiJndoYXQgZG9lcyB5YXJuIGluc3RhbGwgLS1wcm9kdWN0aW9uIGRvSKFGUNoaWJhBcAF4AZABAJgBcKAB0QqqAQQzLjEwuAEDyAEA-AEBwgIKEAAYRxjWBBiwA-IDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp
https://classic.yarnpkg.com/lang/en/docs/cli/install/#:~:text=yarn%20install%20%2D%2Dproduction%5B%3D,status%20from%20this%20flag%20instead.
https://classic.yarnpkg.com/lang/en/docs/installing-dependencies/
https://www.google.com/search?q=what+is+node+js&oq=what+is+node+js&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEJMTA4NTdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://nodejs.org/en/about
https://www.google.com/search?q=a+simple+node+js+server+explained&oq=a+simple+node+js+server+explained&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigAdIBCDkyNzFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction
https://www.google.com/search?q=structure+of+a+node+simple+application&sca_esv=569142147&ei=EnoVZd3LKMfC5OUPsMmMqAE&ved=0ahUKEwjdnL2vr82BAxVHIbkGHbAkAxUQ4dUDCBA&uact=5&oq=structure+of+a+node+simple+application&gs_lp=Egxnd3Mtd2l6LXNlcnAiJnN0cnVjdHVyZSBvZiBhIG5vZGUgc2ltcGxlIGFwcGxpY2F0aW9uMgUQABiiBDIFEAAYogRI5BtQ6hZYuBlwAXgBkAEAmAGCAaAB_gKqAQMwLjO4AQPIAQD4AQHCAgoQABhHGNYEGLAD4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp
https://www.scaler.com/topics/nodejs/node-js-project-structure/
https://nodejs.org/api/
https://nodejs.org/api/synopsis.html
https://nodejs.org/api/http.html
https://nodejs.org/api/http.html#httpcreateserveroptions-requestlistener
https://nodejs.org/api/http.html#serverlisten
https://www.google.com/search?q=javascript+%3D%3E+operator&oq=javascript+%3D%3E+operator&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEJMTIxOTVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function
https://stackoverflow.com/questions/24900875/whats-the-meaning-of-an-arrow-formed-from-equals-greater-than-in-javas

Comecei com um desejo antigo e simples: "Quero usar Docker".

Como costumo fazer, busquei tutoriais que apresentem uma receita simples cujo resultado é algo sendo executado e que eu reconheça que me aproxime do objetivo, no caso, *usar Docker*. (De fato, eu não segui o tutorial, eu o li e interpretei)

Encontrei alguns tutoriais, prefiro os do site oficial da ferramenta, depois, os de instituições que reconheço (as que já me ajudaram a resolver algo ou que têm boa reputação dentro do meu grupo social).

1. https://www.docker.com/101-tutorial/ (só propaganda)
2. https://docs.docker.com/get-started/ (**este sim!**)

Seguir o tutorial, [até a parte 2](https://docs.docker.com/get-started/02_our_app/), e obter o resultado indicado por ele cumpre o desejo de "usar Docker", mas me trouxe mais perguntas:

- Como o exemplo do tutorial funciona?
   - por exemplo, o que é, de fato, executado?
- Qual relação tem a informação apresentada no tutorial com o que é, de fato, executado?

**nota**: estas perguntas não têm a ver diretamente com Docker. Na minha opinião, elas têm a ver com a minha falta de instrução sobre processos e ferramentas usadas no exemplo. Cabem mais comentários, mas deixarei assim no momento.

Fui seguindo indicações dadas no tutorial, que me levaram a outras ferramentas (além do Docker), em uma sequência, que poderia abrir-se em uma árvore, que, eu esperava, que os ramos terminassem em algo que eu entendesse suficientemente. Minha expectativa foi satisfeita, agora descrevo o processo de busca, a informação obtida (na ordem em que foi obtida, *top-down* e apresento a remontagem com objetivo de explicar como o exemplo do tutorial funciona.

Do tutorial, os pre-requisitos: tenho instalados git e vs-code, não tenho Docker Desktop mas tenho a ferramenta em linha de comando (CLI).

Do tutorial, o *get the app*: em princípio não entendi do que se tratava. Parece um projeto de alguma coisa... sigo em frente;

Do tutorial, o *build the app image*: criar e preencher o `Dockerfile`, para mim, significa codificar a especificação (contida em um arquivo) da imagem (outro arquivo, que representa/codifica o que pretendo executar usando Docker). `docker build ...` é o comando para criar a imagem a partir da especificação.

Do tutorial, o *start an app container*, `docker run ...` é o comando que executa o container (container é a imagem, talvez refira-se, mais especificamente, à imagem que o Docker carrega na memória do computador). O container tem acesso à porta 3000 de 127.0.0.1 (acho que tem um `:3000` a mais na linha do exemplo).

Do tutorial, ainda em *start an app container*, abrir o navegador no computador e digitar na barra de endereço: `localhost:3000` permite o acesso à aplicação.

A aplicação é um servidor web que mostra ítens, acho que uma lista deles, e permite acrescentar ítens. Executar uma aplicação como esta requer um servidor web (ex. Apache, nginx, ...), algum tipo de persistência (um arquivo texto ou um banco de dados), talvez acesso ao sistema de arquivos local (como não testei a aplicação, não sei se eu fechar a aplicação (abortar `docker run...`) e abrir de novo (executar um novo `docker run...`) preserva ou não os ítens)... só que eu não instalei nada disso, então tenho novas perguntas:

- Que servidor web é usado e como ele foi instalado?
- Que tipo de persistência é usada e como foi instalada?
- Quando e como o servidor web e a persistência são instalados?
 
Repassando o tutorial a partir do início, entrei no repositório github do projeto da aplicação (https://github.com/docker/getting-started-app/tree/main/src) mas não me inspira idéias, o conteúdo do `Dockerfile` traz idéias: O que é `node:18-alpine`? Fui atrás, encontrei referências: 

- https://hub.docker.com/layers/library/node/18-alpine/images/sha256-d51f2f5ce2dc7dfcc27fc2aa27a6edc66f6b89825ed4c7249ed0a7298c20a45a?context=explore
- https://hub.docker.com/_/alpine
- https://alpinelinux.org/about/
- https://pkgs.alpinelinux.org/packages

`node:18-alpine` é uma imagem para Docker que é usada como base para usuários construírem as imagens dos seus aplicativos.

> Alpine Linux is a Linux distribution built around musl libc and BusyBox. The image is only 5 MB in size and has access to a package repository that is much more complete than other BusyBox based images. This makes Alpine Linux a great image base for utilities and even production applications. Read more about Alpine Linux here and you can see how their mantra fits in right at home with Docker images. (https://hub.docker.com/_/alpine)

Iniciando um novo ramo, que eu tenha entendido, `Dockerfile` é um arquivo de configuração da imagem. Contém palavras que parecem comandos e outras que parecem nomes de ferramentas, parece um *shell script*. O que é `RUN` dentro do `Dockerfile`? Fui atrás, encontrei a referência de todos os comandos que podem ser colocados em um `Dockerfile`: https://docs.docker.com/engine/reference/builder/#run

`RUN` executa o comando sobre a imagem-base e a grava na imagem. O particular comando é: `yarn install --production`. O que é yarn? Fui atrás e encontrei:

> Yarn is a package manager that doubles down as project manager. Whether you work on simple projects or industry monorepos, whether you're an open source developer or an enterprise user, Yarn has your back. (https://yarnpkg.com/) 

Ok, Yarn é um gerenciador de pacotes, então alguma ferramenta foi instalada na imagem. Que ferramenta seria? 

Procurei por `yarn install`, entrei na documentação do Yarn, ele instala o que estiver listado em `package.json`:

> yarn install : Install all the dependencies listed within package.json in the local node_modules folder. (https://classic.yarnpkg.com/lang/en/docs/cli/install/#toc-yarn-install)

`package.json` é um arquivo no repositório github da aplicação, listando o arquivo, vi que ele é muito parecido com o POM do Maven (que é algo que conheço um pouco), então deduzi que as ferramentas são listadas nesse arquivo (ex.: express, sqlite, ...)

Na linha seguinte do `Dockerfile`, `CMD` é um comando. Na referência:

> There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect. The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well. (https://docs.docker.com/engine/reference/builder/#cmd)

Ou seja, este comando executa o servidor web dentro da imagem.

Encontrei as respostas que eu queria:

- Que servidor web é usado e como ele foi instalado?
  - É `node.js`, faz parte da imagem `node:18-alpine`;
  - a aplicação ainda necessita de outras ferramentas, listadas em `package.json`, como `express`;
- Que tipo de persistência é usada e como foi instalada?
  - SQLite;
- Quando e como o servidor web e a persistência são instalados?
  - São instalados na criação da imagem (`docker build...`)

No processo de resposta ainda achei que `CMD` informa o ponto de início da execução do conteúdo da imagem.

Agora que consegui ligar Docker (`build`, `run`) com a aplicação, começa a me fazer sentido entender como a aplicação funciona...

**nota**: É uma questão pessoal (questões pessoais influenciam muito minhas preferências e aversões, consequentemente, com impacto no meu aprendizado): Java Script não é uma linguagem que me atrai. Posto isto...

A aplicação foi escrita em `node.js`. É um framework para criação de servidores e clientes web usando Java Script como linguagem de programação. A execução do programa é assíncrona (isto é, as chamadas de funções de entrada/saída (rede, interface com usuário, interface com armazenamento,...) não bloqueiam a execução do programa (ex.: o programa não "espera" o usuário digitar algo na caixa de entrada para, então, seguir a execução). A infraestrutura para que a linguagem funcione é a de interrupções e funções de *callback*, só que Node oculta esse funcionamento, consequentemente cria a necessidade de uma nova abstração (uma nova narrativa).

O exemplo simples de um servidor escrito sobre Node.js é apresentado em https://nodejs.org/en/about

```javascript
const http = require('http');                      // 1
 
const hostname = '127.0.0.1';
const port = 3000;
 
const server = http.createServer((req, res) => {    // 4 https://nodejs.org/api/http.html#httpcreateserveroptions-requestlistener
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});
 
server.listen(port, hostname, () => {               // 9 https://nodejs.org/api/http.html#serverlisten
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

**nota**: Talvez meus bloqueios sejam com operadores que não conheço, como =>, ou com um programa que não tem *entry point* (ex.: função main). Hora de enfrentar isso.

A chamada de node na linha de comando é algo como `node index.js`, ou seja, executa um script. Que seja o script do servidor simples apresentado acima. Eu não sabia, tinha até dificuldade em ler o que é =>. Procurei, achei a explicação:

> An arrow function expression is a compact alternative to a traditional function expression,...  (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

Na minha interpretação, => é um operador que permite definir funções em tempo de execução. É similar a expressões lambda em Python.

Há várias sintaxes possíveis, as que foram usadas acima são:

```javascript
() => {
  statements
}

(param1, paramN) => {
  statements
}

```

Nos dois casos as funções são anônimas.

A documentação do Node.js explica o que são os objetos `http`, `Server`, ... (https://nodejs.org/api/)

Minha leitura do código-fonte: A linha 1 importa o objeto http (que parece ser algum tipo de classe estática). A linha 4 cria a variável server que aponta para uma instância de Server cuja função de *callback* é criada (com arrow function) e passada como parâmetro. Sempre que este servidor receber uma requisição essa função de *callback* é executada. Sua execução constrói e retorna uma resposta. A linha 9 registra a função de *callback* no loop de eventos.

O aplicativo exemplo do docker é um tanto mais complicado.

A execução começa com `node src/index.js`. O código em `index.js` importa `express` e instancia `app`, que acredito que seja o servidor mínimo. A esse servidor mínimo associa conteúdo estático (do diretório static, index.html está nesse diretório), e extende a URL para servir os outros recursos, como listar os ítens, acrescentar ítens, através de requisições HTTP. Também é instanciado um banco de dados onde os ítens são criados, recuperados e apagados. A interface gráfica (via navegador) usa react-native. Todas as bibliotecas do lado do cliente estão no diretório src/static/js, não carrega de cdn ou qq coisa assim.

Enfim, embora Docker não seja algo executado em dispositivos, a infraestrutura a que os dispositivos se conectam pode usar Docker. Esta também é uma ferramenta muito usada para desenvolvimento de aplicações e é um exemplo de PaaS (https://en.wikipedia.org/wiki/Docker_(software))



