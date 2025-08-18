# Projeto indefinido

Aqui penso em um projeto como o conjunto:

1. proposta: com objetivo, introdução, método, resultados esperados, indicadores de progresso (dei um passo à frente!) e sucesso (terminei!) e cronograma; 
2. execução: de acordo com o cronograma e monitorando os indicadores de progresso e sucesso;
   - pode haver relatórios intermediários ou um diário de atividades;
3. relatório final: com objetivo, introdução, método, resultados, conclusão e comentários;
   - objetivo, introdução, método podem ser diferentes da proposta para o relatório, cabe justificar nos comentários e conclusões;
   - resultados podem ser diferentes dos resultados esperados, cabe explicar nos comentários e conclusões;
   - o resultado pode ser um programa, neste caso, espera-se que o código-fonte e a documentação desse programa seja anexada ao relatório (como um link)
   - se houver dados gerados, convém apresentar no relatório uma amostra ou um link para o conjunto de dados;
     

**nota**: para projetos/relatórios com objetivos ainda menos claros, pode ser conveniente usar um objetivo vago como *explorar o firmware/software/hardware do ESP32 buscando algo interessante para construir* como um *container* de sub-projetos curtos e ir criando esses sub-projetos. Entenda (criar sub-projetos) como propor executar e relatar dentro de um período curto como um dia ou uma semana - ou um *sprint* nestes sub-projetos (curtos) cujo relatório pretende-se entreguar na próxima reunião, a proposta não precisa conter resultados esperados, indicadores de progresso e sucesso e cronograma pois o relatório final do sub-projeto será apresentado.

Vamos a um exemplo...

## Exemplo

Este projeto específico começou sem um objetivo muito claro e com vários ramos:
  
1. Explorar alternativas de fornecimento de energia para placas de desenvolvimento ESP32;
2. *Experimentar usar aiorepl e microdot simultaneamente*... Isto é algo que não consegui fazer quando tentei faz alguns meses. Na época fui ingênuo, pensando que todas as funções de todos os módulos funcionariam e que não haveria problemas de integração entre aiorepl e microdot. O contexto a esperar é o *inverso*: alguma(s) funções de algum(ns) módulos não funcionam, e há problemas de integração.
   - o subprojeto 2 ganhou um filho: pyPathVariable  
3. *Explorar ESPCAM* se é possível usar com micropython, webrepl, asyncio, servidor web,... ( ESPCAM não tem porta USB).


 
