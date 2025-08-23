Convergência de https://github.com/FNakano/CFA/blob/master/partirDoZero.md , https://github.com/FNakano/CFA/tree/master/projetos/ControlarTomadaPelaInternet , https://github.com/FNakano/CFA/tree/master/projetos/py-tomadas , https://github.com/FNakano/CFA/tree/master/projetos/py-MicrodotAndWebREPL e https://github.com/FNakano/CFA/tree/master/projetos/py-aiorepl-microdot

**nota do autor**: A partir do momento em que comecei a escrever esta documentação até o dispositivo desenvolvido estar do jeito que eu acredito ser um *pacote pronto*, levou uma semana.

# Dispositivo conectado para controle de tomadas

## Objetivo(s)

Exemplificar um projeto: elaboração da proposta, execução, elaboração do relatório conforme https://github.com/FNakano/CFA/blob/master/partirDoZero.md

Atualizar os projetos https://github.com/FNakano/CFA/tree/master/projetos/ControlarTomadaPelaInternet , https://github.com/FNakano/CFA/tree/master/projetos/py-tomadas 

Implementar funcionalidades que acho interessantes como execução concorrente de servidor web e terminal de programação e serviço para mostrar mensagens no dispositivo. 

**nota do autor**: o produto extrapola bastante o MVP de controle de tomada que é mais próximo do produto obtido nos projetos que antecederam a este.
 
## Introdução

Existe uma variedade de *smart bulbs* e *smart plugs* no mercado. Esses dispositivos são uma espécie de símbolo da *smartificação*. Sua utilidade é bastante clara, quase lúdica, embora o custo/benefício do dispositivo comparado com interruptores de parede gere discussão.

Do ponto de vista construtivo é um sistema de informação composto por circuito físico, servidor web, interfaces de uso e circulação de informação. 

A reprodução do dispositivo até o teste de uso não traz grandes dificuldades. Por outro lado, reproduzir a metodologia de projeto e construir documentação equivalente para outro projeto, resolver as questões de elaboração das etapas, por exemplo, localizar e corrigir erros, seja no circuito, no programa ou na documentação, requer tempo e pode ser desafiador.


## Método (de execução do projeto)

Usou-se o método descrito em https://github.com/FNakano/CFA/blob/master/partirDoZero.md . O tipo de projeto e forma de documentaçao foram escolhidos com base nas diretrizes da disciplina https://github.com/FNakano/CFA/blob/master/diretrizes.md . 

## Resultados

![](./Captura%20de%20tela%20de%202025-08-23%2010-26-08.png)

Foto representativa do estado de desenvolvimento em 2025-08-23 - Aplicativo iniciado com comando `import startsystem` no Thonny (direita embaixo na foto). Navegador com webrepl e comandos enviados através dele (direita, centro na foto). Navegador com requisição para acender o LED vermelho (esquerda acima na foto). Navegador com requisição para mostrar mensagem no display (direita acima na foto). Dispositivo com LED vermelho aceso e mensagem no display (direita abaixo na foto)


### Resultado do teste de uso

### Como reproduzir este dispositivo

#### Lista de Materiais
#### Montagem
#### Carga do programa
#### Teste de uso


### Manual de usuário

### Manual do desenvolvedor

#### API

## Conclusão e Comentários

O sistema de informação, em especial o programa, poderia ser mais simples. Tornou-se elaborado considerando desenvolvimentos futuros em que podem ser agregadas muito mais funcionalidades em um contexto multiusuário.
