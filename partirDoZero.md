# Projeto indefinido

projeto indefinido: o que fazer quando, no momento, é difícil e necessário definir um projeto

## Introdução

Este documento pretende apresentar uma estratégia e pretende ser um guia para elaboração de projetos.

Aqui penso em um projeto como um conjunto com três elementos: proposta, execução e relatório. A elaboração de cada um dos elementos e do conjunto pode ser feita em espirais, revisitando cada elemento e acrescentando informação até que se encontre um projeto suficientemente definido e coeso.

O conteúdo de cada elemento e uma breve explicação é apresentada abaixo.

1. proposta: com objetivo, introdução, método, resultados esperados, indicadores de progresso (dei um passo à frente!) e sucesso (terminei!) e cronograma; 
2. execução: de acordo com o cronograma e monitorando os indicadores de progresso e sucesso;
   - pode haver relatórios intermediários ou um diário de atividades;
3. relatório final: com objetivo, introdução, método, resultados, conclusão e comentários;
   - objetivo, introdução, método podem ser diferentes da proposta para o relatório, cabe justificar nos comentários e conclusões;
   - resultados podem ser diferentes dos resultados esperados, cabe explicar nos comentários e conclusões;
   - o resultado pode ser um programa, neste caso, espera-se que o código-fonte e a documentação desse programa seja anexada ao relatório (como um link)
   - se houver dados gerados, convém apresentar no relatório uma amostra ou um link para o conjunto de dados;
     
A estratégia consiste em, dado um *grande* projeto com objetivo, método, resultados esperados, ... pouco claros, definir sub-projetos cujos resultados *possam contribuir* para esclarecer o objetivo, método, resultados esperados, ... do *grande* projeto. Cada sub-projeto, preferencialmente, deve ter curta duração e usar poucos recursos, entre eles, o seu esforço e tempo. A cada *volta* sobre propor, executar e relatar, seja um sub-projeto novo, seja um sub-projeto em andamento (nova versão), atualizar o texto do *grande* projeto até que este esteja suficientemente definido e coeso. 

Para ter algo no *grande* projeto (não deixar a folha em branco), pode ser conveniente usar um objetivo vago como *explorar o firmware/software/hardware do ESP32 para, ao final, construir algo interessante/relevante* e usar o projeto como um *container* de sub-projetos curtos e ir criando esses sub-projetos. Entenda *criar sub-projetos* como propor, executar e relatar dentro de um período curto como um dia ou uma semana - ou um *sprint* .  Caso sejam sub-projetos de curtíssima duração, cujo relatório pretende-se entreguar na próxima reunião, a proposta não precisa conter resultados esperados, indicadores de progresso e sucesso e cronograma pois o relatório final do sub-projeto, contendo seus resultados, será apresentado.

Uma pergunta que pode ocorrer é: *se faço sub-projetos durante a fase de proposta então, ao final de todos os sub-projetos não obtenho o projeto pronto?*. Se os sub-projetos contemplam (testam) todas as integrações usadas no projeto (por exemplo em desenvolvimento incremental) a resposta é *sim* mas se as integrações não forem testadas no específico uso do projeto então a resposta é *não* e pode haver imprevistos que demandarão tempo e trabalho. 

Outra pergunta/observação: *É permitido remover informação?* A resposta é *sim*, destacando que essa escolha requer justificativa e revisão de objetivos. A fim de mostrar que houve tempo e trabalho dedicado ao projeto quando há remoções, convém ter um diário, documentação de sub-projetos e/ou versões anteriores do projeto. Ainda assim, o projeto final pode ser insuficiente.

Vamos a um exemplo...

## Exemplo

Este *projeto indefinido* específico começou sem um objetivo muito claro e com vários ramos:
  
1. Explorar alternativas simples, portáteis e baratas de fornecimento de energia para placas de desenvolvimento ESP32;
   - motivado por perguntas de colegas;
   - motivado pela experiência de uso de pilhas, baterias diversas e powerbanks;
   - essa exploração deve incluir um teste (benchmark) de duração realista para o tipo de projeto da disciplina;
   - o projeto [py-TestSupplyPower](/projetos/py-TestSupplyPower) busca responder este ponto;
2. *Experimentar usar aiorepl e microdot simultaneamente*... Isto é algo que não consegui fazer quando tentei faz alguns meses. Na época fui ingênuo, pensando que todas as funções de todos os módulos funcionariam e que não haveria problemas de integração entre aiorepl e microdot. O contexto a esperar é o *inverso*: alguma(s) funções de algum(ns) módulos não funcionam, e há problemas de integração.
   - o subprojeto 2 ganhou um filho: [py-Path](projetos/py-Path)  
   - poder usar o micropython do dispositivo enquanto ele executa um programa *maior* (um servidor HTTP) pode ser útil, por exemplo, para depurar o programa *maior* ou mesmo elimininar algum *bug* sem interromper a operação (ié desligar, eliminar e religar o dispositivo);
  - isto acabou sendo uma retomada do projeto [py-MicrodotAndWebREPL](/projetos/py-MicrodotAndWebREPL)
3. *Explorar ESPCAM* se é possível usar com micropython, webrepl, asyncio, servidor web,... ( ESPCAM não tem porta USB).
   - programar ESPCAM não é confortável pela falta de porta USB e não é confortável porque a maioria dos tutoriais usa linguagem C.
   - falhar ao hackear a câmera do ESPCAM, ao ponto de inutilizá-la, é barato comparado com falhar com uma webcam, um celular ou uma câmera fotográfica;
4. *Retomar [py-Tomadas](./projetos/py-tomadas) e [controlar tomadas pela internet](./projetos/ControlarTomadaPelaInternet)* Juntar e atualizar framework (usar aiorepl, microdot)

### Resultado (para apresentar em 2025-08-28)

https://github.com/FNakano/CFA2025-SampleProject


 
