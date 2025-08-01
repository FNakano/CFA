# ACH2157

## Diretrizes

- Na disciplina:
  - nossos objetivos: aprender algo
    - construir objetos físicos (ex. dispositivos);
    - construir sistemas (simples) de informação;
    - programação web;
    - bancos de dados;
    - programação;
    - segurança(!);
    - soft skills;
  - uso aprendizagem por projeto;
  - haverá algumas aulas expositivas;
    - serão apresentados, com algum detalhamento, projetos e componentes;
  - atendimento a questões pontuais de cada projeto durante as aulas práticas;
  - são ítens de avaliação:
    - Frequência às aulas - critério rígido
    - Entrega e qualidade da documentação
      - Diário
      - Relatório
      - Apresentações de andamento (inicial, intermediária, final) - combinar datas!
    - Participação e evolução individual na reunião semanal comigo (feito durante a aula)
      - sprint planning
      - previous sprint review
      - sprint(s) retrospective
    - Opinião dos colegas
      - o que fez, o que entregou
      - como interagiu com os colegas de grupo durante a execução do projeto
    - combinem comigo se preferem que essa informação seja ou não compartilhada entre os colegas de grupo
  
- O projeto deve incluir (ié requisitos funcionais):
  - construção e programação de um dispositivo físico usando ESP32;
  - comunicação através ou de wifi ou de bluetooth;
  - site de desenvolvimento e documentação no Github;
  
Comunicação comigo (ex. envio de mensagens e tarefas) através do e-disciplinas.

## Tópicos para referência

### Abstrações usuais para desenvolvimento e documentação

- diagramas de blocos
- modelo de camadas
- UML (fluxograma, diagrama de mensagens, BPM, ...)

nota: o diagrama em si permite múltiplas interpretações, logo, aquilo que desejamos comunicar com o diagrama precisa ser escrito e acompanhá-lo.
nota: conhecer esses modelos influencia na maneira como pensamos (planejamos projetos, atividades, ...) que, por sua vez influencia como usamos esses modelos (ié modelo espiral)

### Proposta de método para desenvolvimento de algo "a partir do zero" - isto é bastante vago e flexível

- Convém ter em mente SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- Especificidade: Ter em mente que o "tempo de melhor qualidade" não é o do fim do semestre;
- Princípios (ou requisitos (os que você quiser))
  - motivacionais (ex. algo ligado a jogos ou a música, ...)
  - funcionais (ex. que linguagem de programação usar)
  - o que mais você achar importante (ex. o que você sente quando se dedica a esse algo, ...)
- Explorar o que existe, que elementos precisa, que elementos você tem à disposição;
  - testes exploratórios (seguir tutoriais, fazer seus próprios testes (e incluí-los como testes unitários?), ...
- Definir e ir refinando o "algo";
- Reiniciar esse processo;
  - anotar em diário;
  - controle de versões (git)

### Escritos em geral

Para quem estamos escrevendo? (documentação, programa, ...)
  - ex de resposta: usuário "final", desenvolvedor (usuário da biblioteca), mantenedor (do programa), ...
Qual o objetivo da documentação dada a categoria de pessoas para quem estamos escrevendo?
Depois de definir o objetivo, escolher, de 5W2H (What, Why, Who, Where, When, How, How much), quais elementos fazem sentido para a documentação
  - ex. O que é o objeto documentado;
  - ex. Quando o objeto foi construído (ou quando a documentação foi escrita, ...);
  - ex. Por que o objeto foi construído;
  - ex. Onde o objeto foi construído;
  - ex. Quem construiu o objeto (ou quem documentou o objeto);
  - ex. Quanto custou (ou quanto recurso (peças, tempo, ...) usou);
  - ex. Como o objeto foi construído;
Objetos específicos podem pedir (ié, opcional de bom tom) ítens ou formatos de documentação específicos
  - ex. relatório (introdução, objetivo, método, resultados, conclusões e comentários);
  - ex. tutorial ( mais ênfase nos testes e nas alternativas de falha e correção);
  - ex. FAQ (pergunta-resposta);
  - ex. código-fonte, moldes, listas de material, testes unitários, testes de integração, fotografias, vídeos, ....

### Escritos específicos

Diário
  - Para quem: você mesmo
  - Objetivo: acumular informação suficiente para permitir escrever uma boa documentação (relatório, artigo, ...)
  - Fomato
    - Elementos fixos: Data (2025-07-30T23:30); O que fez (ié começa com verbo na primeira pessoa como ajustei os protótipos das funções `calculaRetorno` e `armazenaResultado` para ajustar à forma como fulano definiu/usou)
    - Elementos importantes: comandos, linhas de comando, links para referências com uma breve explicação, problemas e, quando pertinente, soluções 
    - Elementos opcionais: livre

Manual para usuário (às vezes implantação)

Manual para manutenção

Manual para duplicação

Manual para desenvolvedor (da próxima camada, de aperfeiçoamentos, ...)

Manual para implantação (deployment)

...

