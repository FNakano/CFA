# Modelos

## Motivação

Acredito que todos que se engajam em um projeto desejam que o resultado do projeto, ou o projeto em si, gere benefícios e beneficie a maior quantidade de pessoas possível. Para os outros perceberem o benefício do que lhes é oferecido, no contexto da disciplina, eles devem conseguir entender o que se conseguiu fazer, como foi feito, como reproduzir. A documentação do projeto é o instrumento disponível para alcançar os outros. A boa documentação facilita que o outro use o que você fez.

A cada turma, o grupo todo é renovado. O novo grupo inicia seu período aproximadamente com o mesmo conhecimento do grupo anterior. Há uma tendência a passar pelas mesmas dificuldades, fazer as mesmas escolhas,... Ao final, dispendendo aproximadamente o mesmo tempo e esforço, supondo que a tecnologia não mude, os resultados do novo grupo e do grupo anterior terão aproximadamente a mesma qualidade.

Acredito que não precise ser assim. O novo grupo pode construir a partir do que o grupo anterior deixou. Acredito que um elemento necessário para permitir essa evolução seja documentar o projeto com a orientação de transmitir informação ao próximo grupo de forma concisa, correta e concentrada (em um repositório).

A administração da coleção de documentos acumulados no tempo acaba sendo do docente, que é o único membro permanente do grupo. Ele também usa a documentação e, pela característica de sua função, é capaz de comparar formas de documentação. Em decorrência dessa função, é conveniente que ele decida como a documentação deve ser feita e forneça modelos e exemplos de uso.

## Apresentação

Algumas estratégias de documentação foram pensadas e testadas com o objetivo de conter informação suficiente e minimizar esforço e tempo para documentar. Chegou-se a esta, que é composta por:

- Registro de atividades (opcional, fortemente recomendado);
- Proposta;
- Entregável (site);
- Relatório Final (caso as recomendações sejam seguidas, fará parte do site);

### Seções da proposta

No processo de construção da proposta, espera-se que o proponente reflita sobre sua motivação, capacidade de realização, ganhos e chance de sucesso naquilo que propõe fazer; Que se permita pesquisar que recursos necessita e que recursos tem à disposição; Que o que tem em mente é suficientemente claro para ser comunicado por escrito. Espera-se que o tempo e esforço dispendido nesta etapa seja pequeno, e que poupe tempo e esforço cuidando de imprevistos nas etapas seguintes.

1. Título
2. Objetivo Gerais (O que fazer)
3. Motivação (Por que fazer: Relevância, experiência, conhecimento acumulado, motivação pessoal,...)
4. Caso seja parte de uma sequência/cadeia/rede, quais relações com as outras atividades/elos são conhecidas.
5. Referências

A avaliação da proposta por outras pessoas permite coletar opiniões que balizam a relevância e chance de sucesso da proposta.

**nota**: em situações genéricas, seria recomendável escrever o plano de atividades, a fim de refletir sobre o detalhamento das atividades e estimar o tempo de realização. Isto pressupõe experiência nas atividades. Nesta disciplina, como o comum é ter pouca experiência e aprender a usar as ferramentas e componentes simultaneamente a sua aplicação no projeto, escrever o plano de atividades é um uso questionável de tempo e esforço.

### Repositório do projeto

O resultado das atividades. Como os resultados vão evoluindo à medida que as atividades são executadas, é conveniente usar um versionador, como git, e um repositório na nuvem, como github, para que todos possam acessar e trabalhar simultaneamente.

### Seções do relatório final

1. Introdução (parte já foi feita na proposta)
    1. Contextualização (o que se sabe) e Motivação (por que se quer)  (desnecessário, se for o mesmo da proposta)
    1. Revisão Bibliográfica (informação que foi encontrada durante a execução)
        1. Conceitos e Terminologia (glossário)
    3. Organização do relatório (links, please)
2. Objetivos (os gerais foram escritos na proposta, os específicos podem ser acrescentados)
3. Materiais e Métodos ( quais são os ingredientes e o que fazer com eles para chegar nos resultados)
4. Resultados e indicadores de avaliação (resultados dos testes dos entregáveis - cada resultado como uma subseção, para facilitar links para o resultado específico)
    1. Entregáveis previstos (há informação adicional, dependendo do tipo de entregável)
    2. Entregáveis não previstos (soluções para problemas colaterais)
5. Discussão e Conclusão
    1. Consequências lógicas dos resultados (resultados deduzidos);
    3. Dificuldades que levaram às soluções colaterais
    2. Especulações/questionamentos a partir dos resultados (resultados induzidos);
    2. Desdobramentos possíveis (próximos passos, possibilidades, *spin-offs*);
6. Referências

### Informação sobre circuitos e programas (para o desenvolvedor/mantenedor)

Caso o entregável seja um dispositivo, a informação **mínima** sobre o dispositivo é:

- Para cada componente;
    - lista de pinos;
    - fotos;
    - links para os documentos, vídeos e tutoriais que usou para aprender a usar o componente;
- Para a interligação dos componentes;
    - Lista de componentes que serão interligados (essencial);
    - Lista de conexões (essencial);
- Para os programas;
    - Código-fonte 
    - instruções para compilar/transferir para o dispositivo/celular/computador;
    - casos de uso, testes,...

Caso o entregável seja uma placa de circuito impresso, entregar o arquivo do CAD em que foi desenhada e incluir uma foto no relatório.

Informação adicional como fotos, vídeos, diagramas são bemvindos.

### Informação sobre o vestível (para o desenvolvedor/mantenedor)

### Informação sobre o produto (para o usuário/cliente)

### Informação sobre o serviço (para o usuário/cliente)

### Registro de atividades (fortemente recomendado)

Frequentemente repetem-se as mesmas buscas por informação. Por exempo: busca-se a informação para avaliar se um componente pode ser usado, depois a mesma busca para efetivamente usá-lo, depois a mesma busca para incluir a referência no site, depois a mesma busca para incluir no relatório final... 

...OU...

Durante a execução do projeto depara-se com um problema e cria-se uma solução. **Isto é um resultado!**... que geralmente fica de fora do relatório porque na correria de fazer o relatório (sempre de última hora), esquece-se ou omite-se pois o tempo para escrever o relatório é curto.

Nenhuma das duas situações parece ser bom uso do tempo. A primeira desperdiça-o, a segunda despreza o resultado e o tempo gasto para consegui-lo.

A forma que funcionou para mim é a de ter um diário de projeto. Sempre que trabalho em algum projeto, o faço com o diário aberto. Com pouco tempo e esforço, anoto o que interessou ou copio-colo o link e um comentário curto sobre para que me serviu. Geralmente uso alguma palavra de que não esquecerei fácil, para poder recuperar a informação com `grep`, ou com o indexador do Windows.

### Ferramentas recomendadas

O site recomendado como repositório para projetos é o [github](https://github.com/).

Nele as páginas são escritas em uma variação do texto puro que permite formatar títulos e incluir imagens e links: [*markdown 'sabor' Github*](https://docs.github.com/pt/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax).

No jargão do Git/Github, seu projeto estará armazenado em um *repositório*. Ele pode ser considerado uma pasta no computador, ou um site na internet, as duas analogias são válidas.

Quando o repositório é acessado, o (servidor) Github exibe o conteúdo do arquivo `README.md` formatado como instruido no arquivo.

Para documentação dos projetos, este primeiro `README.md` deve conter, no mínimo, os elementos do **relatório final**. Desta forma o esforço de criar o conteúdo do site e o de criar o relatório final é diminuido.

Elementos podem ser acrescentados a esse `README.md` por exemplo: link para as páginas de tutoriais, para vídeos de divulgação ou capacitação, para o código-fonte, ...

O relatório final contém links para a proposta e para o diário do projeto.

Para sua comodidade, é fornecido um repositório com essa estrutura, mas sem conteúdo, que pode ser copiado ou clonado e reiniciado para ser usado como repositório do seu projeto.

O projeto que documentei usando esta ferramenta é [Funcionalidades Recorrentes](../projetos/FuncionalidadesRecorrentes/README.md) e seu sub-projeto [Servidor de Arquivos](../projetos/ServidorDeArquivos/README.md)

### Gerar relatórios em pdf a partir das páginas do repositório

Esta é a recomendação para gerar documentos pdf na disciplina, caso seja solicitado.

Trata-se de uma sistematização para criação dos repositórios github onde os projetos podem ser publicados. Não tem código. Se escrever o repositório sabendo previamente quais são as seções do relatório, construi-lo fica mais rápido. O caso que considero 'sucesso' é este: https://github.com/camilabezerril/ImageCV

O relatório: https://github.com/camilabezerril/ImageCV/blob/master/relatorio.md foi criado com uma seleção de parágrafos e seções da documentação (plano de trabalho, ...) que estão no repositório também. A impressão em pdf, removendo a interface do site do github, é feita do arquivo .md em um repositório local, através do browser, usando o addon para renderizar markdown. Por fim, se necessário, acrescenta folha de rosto, sumário e numeração de páginas num editor pdf como https://www.ilovepdf.com/.

- Instalar o Gitlab Markdown Viewer addon/plugin no navegador;
- exibir no navegador o arquivo .md do repositório **local**;
- imprimir para pdf;
- acrescentar folha de rosto, sumário e numeração de páginas num editor pdf como <https://www.ilovepdf.com/>;

Fórmulas matemáticas (em latex) são renderizadas automaticamente pelo addon/plugin.
    
### Grafos, Gantt e mais...

No momento a melhor solução é usar a ferramenta de edição melhor conhecida por quem for fazer os diagramas, exportar em um formato suportado em navegador (svg, png, jpeg, ...), incluir no repositório e linkar nas páginas.

Usando [mermaid](https://mermaid-js.github.io/mermaid/), é possível gerar o cronograma abaixo...

![gantt](mermaid-diagram-20201001181453.svg)

... a partir desta especificação ('programa'):

```mermaid
gantt
dateFormat  YYYY-MM-DD
title Adding GANTT diagram to mermaid
section A Section
Completed task            :done,    des1, 2014-01-06,2014-01-08
Active task               :active,  des2, 2014-01-09, 3d
Future task               :         des3, after des2, 5d
Future task2               :         des4, after des3, 5d
```
![gantt](mermaid-diagram-20201001183040.svg)

```mermaid
graph TD
  A[Christmas] -->|Get money| B(Go shopping)
  B --> C{Let me think}
  C -->|One| D[Laptop]
  C -->|Two| E[iPhone]
  C -->|Three| F[fa:fa-car Car]
```

<!--- 
O addon funciona em arquivos armazenados no github, não funciona em arquivos locais (2020-10-01-090920)



 --->
 
[link para mermaid online editor](https://mermaid-js.github.io/mermaid-live-editor/)

### Fórmulas matemáticas

No momento a melhor solução é usar a ferramenta de edição melhor conhecida por quem for fazer os diagramas, exportar em um formato suportado em navegador (svg, png, jpeg, ...), incluir no repositório e linkar nas páginas.

<!--- 
a fórmula é renderizada em arquivos locais, não é renderizada em arquivos no github (2020-10-01-090902)


$`\Sigma_{i=1}^{10} i^2`$

```math
\Sigma_{i=1}^{10} i^2
```
 --->



<!--- 
O processo de elaboração da documentação pode ser usado como ocasião para refletir sobre os elementos presentes na documentação e como usá-los para ajudar a aumentar a chance de sucesso do projeto. Por exemplo, em um plano de atividades: A forma mais sucinta de descrever o que será feito de forma que o outro compreenda; Elucidar se os recursos, tanto materiais quanto conhecimento e tempo são suficientes, ou, preparar alternativas; Detalhar suficientemente qual o papel de cada participante,...

Considerando *modelo de documento*, os textos que contém a lista dos elementos que determinados documentos precisam conter, é possível usar os modelos como instrumentos para direcionar a atenção a características importantes para o sucesso do projeto e a avaliação apropriada do desempenho na disciplina. Neste caso, a documentação do projeto demonstra que a equipe dedicou algum tempo e esforço refletindo sobre os elementos da documentação.



As características observadas em todas as etapas de desenvolvimento são `Specific Measurable Attainable Relevant Time-bound` (SMART):

- Specific: Pouco específico (muito vago ou muito amplo, [quem, o que, quando, como, por quê](https://www.smartsheet.com/blog/essential-guide-writing-smart-goals) - dificulta execução) ... específico;
- Measurable: Pouco mensurável (sem resultados ou resultados que dependem de análise qualitativa em que pode haver divergências),..., Muito mensurável
- Attainable: difícil de atingir - a equipe, no projeto, não mostrou elementos suficientes (conhecimento prévio ou etapas de aquisição de conhecimento no próprio projeto) para o avaliador dizer se a equipe consegue atingir
- Relevant: Pouco relevante (traz pouco aprendizado, não cumpre a finalidade do aprendizado na disciplina, limitado, pouco ambicioso);
- Time-bound: Sem prazos definidos, ou prazos muito curtos versus prazos bem definidos e cumpridos;

As características SMART podem ter dependências entre si. Dois exemplos:

1. atividades muito bem especificadas podem ser muito atingíveis, mas pouco relevantes, por outro lado, atividades pouco específicas podem ser muito relevantes, mas com prazos difíceis de definir, ou fracamente definidos. 
2. uma atividade pode ser muito relevante, mas difícil de atingir dado o tempo disponível. Neste caso, é possível dividir a atividade em sub-atividades e dedicar-se a uma sub-atividade ainda relevante e atingível. Simultaneamente, manter a informação que a possibilidade de explorar a atividade foi aventada e que, pelos motivos apresentados, escolheu-se a sub-atividade é informação relevante para os relatórios e para as avaliações.

A avaliação dos ítens permite definir atividades com características equilibradas.

A idéia é aplicável tanto para objetivos 'complexos' quanto para objetivos 'simples'. Quando forem muito simples, aplicar SMART pode usar mais tempo e esforço do que chegar ao objetivo. Neste caso, é melhor fazer. Caso tente fazer e não consiga, talvez alguma característica tenha sido super/sub-estimada.

As etapas de desenvolvimento são:

1. Proposta;
2. Plano de atividades;
3. Site;
    - código-fonte;
    - diagramas, esquemas;
    - tutoriais;
    - materiais de apresentação/divulgação do projeto;
    - diário de projeto, caso seja opção utilizar esta ferramenta;
4. Relatório;

A proposta é maximizar a chance da entrega de um resultado, e que esse resultado mostre que o aluno melhorou suas habilidades interpessoais e/ou técnicas.

- Desenvolvimento de produto? : plano/projeto + relatórios
- Desenvolvimento de serviço? : plano/projeto (business canvas?) + relatórios

*a produção de um produto é um serviço*

*a informação dos relatórios pode ser ajustada para fazer parte de um artigo*

*artigos podem ser de vários tipos, dentre eles, científicos, de divulgação científica, de divulgação para público amplo, ...*

- Quanto tempo, em horas por semana, você estima que pode dedicar a desenvolver o proposto?
- O que você já sabe, já tem ou está seguro que é capaz de aprender, fazer?

## Seções da proposta

No processo de construção da proposta, espera-se que o proponente reflita sobre sua motivação, capacidade de realização, ganhos e chance de sucesso naquilo que propõe fazer; Que se permita pesquisar que recursos necessita e que recursos tem à disposição; Que o que tem em mente é suficientemente claro para ser comunicado por escrito. Espera-se que o tempo e esforço dispendido nesta etapa seja pequeno, e que poupe tempo e esforço cuidando de imprevistos nas etapas seguintes.

1. Título
2. Objetivo (O que fazer)
3. Motivação (Por que fazer: Relevância, experiência, conhecimento acumulado, motivação pessoal,...)
4. Caso seja parte de uma sequência/cadeia/rede, quais relações com as outras atividades/elos são conhecidas.
5. Referências

A avaliação da proposta por outras pessoas permite coletar opiniões que balizam a relevância e chance de sucesso da proposta.

## Seções do plano de atividades

Após a proposta ser aceita, o detalhamento minucioso das etapas de execução, materiais, métodos, prazos e medidas de sucesso, posto por escrito no plano de atividades.

1. Título
2. Resumo
3. Justificativa (cópia da motivação da proposta)
4. Resultados Anteriores (para continuação de projetos anteriores executados pela mesma equipe ou por outra equipe)
5. Objetivos
6. Métodos
7. Detalhamento das atividades a serem desenvolvidas por cada membro da equipe
8. Resultados previstos (entregáveis) e seus respectivos indicadores de avaliação (testes para validar o funcionamento do entregável)
9. Cronograma de execução
10. Outras informações que sejam relevantes para o processo de avaliação.

## Repositório do projeto

O resultado das atividades. Como os resultados vão evoluindo à medida que as atividades são executadas, é conveniente usar um versionador, como git, e um repositório na nuvem, como github, para que todos possam acessar e trabalhar simultaneamente.

### Informação sobre circuitos e programas (para o desenvolvedor/mantenedor)

Caso o entregável seja um dispositivo, a informação mínima sobre o dispositivo é:

- Para cada componente;
    - lista de pinos;
    - fotos;
    - datasheet;
    - diagrama esquemático;
    - PCB;
- Para a interligação dos componentes;
    - Lista de componentes que serão interligados;
    - Lista de conexões;
- Para os programas;
    - Código-fonte 
    - instruções para compilar/transferir para o dispositivo/celular/computador;
    - casos de uso, testes,...
    
### Informação sobre o vestível (para o desenvolvedor/mantenedor)


### Informação sobre o produto (para o usuário/cliente)


### Informação sobre o serviço (para o usuário/cliente)

há outros stakeholders, como os fornecedores

## Seções do relatório

1. Introdução (parte já foi feita no plano de atividades)
    1. ~~Contextualização (o que se sabe) e Motivação (por que se quer)~~ feito na proposta
    1. Revisão Bibliográfica (informação que foi encontrada durante a execução do plano)
        1. Conceitos e Terminologia (glossário)
    2. ~~Questão de pesquisa~~
    3. Organização do relatório
2. ~~Objetivos~~ (feito no plano de atividades)
3. Materiais e Métodos ( quais são os ingredientes e o que fazer com eles para chegar nos resultados)
4. Resultados e indicadores de avaliação (resultados dos testes dos entregáveis)
    1. Entregáveis previstos
    2. Entregáveis não previstos (soluções para problemas colaterais)
5. Discussão e Conclusão
    1. Consequências lógicas dos resultados (resultados deduzidos);
    3. Dificuldades que levaram às soluções colaterais
    2. Especulações/questionamentos a partir dos resultados (resultados induzidos);
    2. Desdobramentos possíveis (próximos passos, possibilidades, *spin-offs*);
    
6. Referências

 --->

