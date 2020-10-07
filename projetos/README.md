# Estratégia de desenvolvimento de dispositivos

*Esta é uma anotação sobre uma estratégia pessoal. Tem me sido útil. É meu desejo que também lhe seja útil de alguma forma.*

## Orientação geral, pessoal e individual

### Anotações

Eu anoto sites acessados, livros consultados, idéias, problemas, soluções, datas. Isto poupa o tempo para procurar (de novo) 'aquele site que tinha aquele trecho de programa ou aquele produto que resolve aquele problema'. Por exemplo, no formato de um diário. Na opinião do autor, tê-lo no computador em arquivos texto torna mais rápida a recuperação da informação e seu reúso, por exemplo, em relatórios.

Anotar no computador permite que as ferramentas de buscas de texto em arquivos (por exemplo *grep*) sejam usadas, o que ajuda na recuperação da informação. 

### Atividade

Tem aquela pilha de atividades por fazer mas não tem motivação para fazer alguma delas. Tente:

- se tem vontade de fazer alguma outra coisa, faça, e anote para não esquecer que fez;
- começe alguma das atividades da pilha - quem sabe ela evolui bem - anote;

Fazer algo é melhor que ficar 'discutindo consigo mesmo' ou 'culpando-se por não fazer'. Tente manter-se ativo.

Quando quiser definir uma atividade, por exemplo em um plano, procure que ela tenha estas características: Specific, Measurable, Achievable, Realistic, Time-bound: SMART

Se uma atividade é muito complexa, divida-a em atividades menos complexas

Se uma atividade recai em usar um exemplo ou tutorial, então use-o. Procure manter seu dispositivo compatível com os exemplos pois isso permite testar o dispositivo com o exemplo (compilar, enviar, ver funcionar). Adaptando a idéia de testes unitários.

## Versões

Quando conseguir um programa/dispositivo com uma evolução que você julgar importante, guarde uma versão com todos os programas acessórios ANTES de começar a implementar a próxima funcionalidade ou melhoria. *Implementar a próxima funcionalidade pode 'quebrar' as funcionalidades já existentes*.

Para juntar vários exemplos de código de um jeito rápido: todos os exemplos têm um método setup e um método loop. Copiar e colar os códigos só não dá certo (em uma boa parcela das tentativas) por isso. Então renomeie o setup e o loop dos exemplos (de forma a lembrar de onde veio) e então escreva um novo setup e um novo loop com a sequência de chamadas de todos os setup e todos os loop.

Copiar e colar os conteúdos dos setups e dos loops também funciona, mas você termina com um grande setup e um grande loop. Trechos longos de código, às vezes misturando funcionalidades, costumam requerer mais atenção para depurar e mais digitação do programador.

### Hábitos

Mesmo usando alguns minutos por dia em algo, e lembrando do que fez ou onde parou, esse algo progride um pouco. Criar o hábito de dedicar-se a esse algo pode ajudar a completá-lo.

Há quem crie hábitos pelo estabelecimento de uma rotina, outros, escolhendo horário e duração fixos, outros, associando atividades, dando-se recompensas, ...

Comigo tem funcionado ter reuniões semanais em que metas para a semana são combinadas. É claro que em uma semana ou outra a reunião não acontece, em uma semana ou outra não se atinge a meta. No primeiro caso, trocar informação com o grupo é importante: mande e-mail. No segundo caso, apareça na reunião e diga a todos que não deu. À medida que as metas forem diminuindo (é o esperado quando se aproxima da conclusão), manter o hábito fica mais difícil, talvez por ser menos necessário. Para mim, esse é o sinal para finalizar com o que tem. Esse restinho de disposição vai para ajustar entregáveis, documentação e relatório.

### Projetos 

[Relógio Conectado](RelogioConectado/README.md) é um relógio de pulso que se conecta ao celular por Bluetooth. Ele registra toques em botões e horários em que ocorreram. Criei em torno da temática de anotações, atividades e hábitos.


## 2020-10-03-182254

Uma boa condução de um projeto - da concepção até a entrega dos resultados prometidos no projeto -, na minha opinião, está relacionada ao equilíbrio entre *estudar*, *elaborar* e *fazer*.

Frequentemente propõe-se algo sem ter todas as soluções necessárias, ou, até, sem ter todas as atividades definidas e detalhadas, ... há contextos em que é aceitável, noutros, inevitável, e há gradações. O extremo, acredito, reflete-se no argumento:

> ...pode deixar que a gente faz...

... e este argumento é a proposta e o plano de atividades.

Meu objetivo aqui não é elaborar sobre o argumento extremo, mas usá-lo para reforçar uma constatação: `Durante a execução de um projeto, sempre há algo a estudar`. Chamo isto *estudar*. Ele está relacionado a `buscar elementos, subsídios, conhecimento,...`.

À medida que os elementos são encontrados, há o trabalho de compor os elementos de maneira que algo ,outro algo, que acredita-se que seja a solução necessária, seja feito. Chamo isto *elaborar*.

Testar os elementos encontrados, testar as composições dos elementos, testar se a composição é a solução necessária, incorporar a solução necessária ao produto. Chamo isto *fazer*.

Proporções desequilibradas entre *estudar*, *elaborar* e *fazer* podem levar a bons resultados ao custo de desgaste físico e mental, ou como reflexo de sorte ou traços de genialidade. Por exemplo: é possível chegar a bons resultados *fazendo* muito, *estudando* muito e *elaborando* mal. Outro exemplo: *fazer* pouco, *estudar* muito e *elaborar* bem. Na minha opinião, é a condução de quem pensa muito e acerta com poucas tentativas. Outro exemplo: *fazer* muito, *estudar* muito, *elaborar* muito.

Outras proporções, que eu tenha observado, levam a resultados diferentes do planejado, ou levam a resultados aquém do prometido.

---

### Alcance e continuidade

Acredito que todos que se engajam em um projeto desejam que o resultado do projeto, ou o projeto em si, gere benefícios e beneficie a maior quantidade de pessoas possível. Para os outros perceberem o benefício do que lhes é oferecido, no contexto da disciplina, eles devem conseguir entender o que se conseguiu fazer, como foi feito, como reproduzir. A documentação do projeto é o instrumento disponível para alcançar os outros. A boa documentação facilita que o outro use o que você fez.

A cada turma, o grupo todo é renovado. Sem boa documentação, o novo grupo inicia seu período aproximadamente no mesmo estágio do grupo anterior. Dispendendo aproximadamente o mesmo tempo e esforço, supondo que a tecnologia não mude, os resultados do novo grupo e do grupo anterior terão aproximadamente a mesma qualidade.

Acredito que não precise ser assim. O novo grupo pode construir a partir do que o grupo anterior deixou. Acredito que seja importante dispor de boa documentação, onde para ser boa, requer ser concisa, correta e concentrada (em um repositório).

A administração da coleção de documentos acumulados no tempo acaba sendo do docente, que é o único membro permanente do grupo. Ele também usa a documentação e, pela característica de sua função, é capaz de comparar formas de documentação. Em decorrência dessa função, é conveniente que ele decida como a documentação deve ser feita e forneça modelos e exemplos de uso.

