EditorPP é um editor de texto com código-fonte aberto, escrito em Python e que estou configurando para agilizar meu processo de anotação de atividades e construção de documentação formal (relatórios, artigos, ...) .

Este README é a primeira tentativa de gerar documentação formal a partir das anotações. O objetivo desta anotação é satisfazer o interesse das pessoas que conversaram comigo e também perceberam que poderiam tirar proveito de uma ferramenta como esta. Como esta documentação é, também, um trabalho em andamento, quem acompanhá-la verá mudanças grandes ao longo do tempo. A fim de registrar essas mudanças, uso `Git` como controlador de versões e `Github` como canal de divulgação. Bom divertimento!

## Introdução

Faz uns anos que tenho me ocupado de estudar ferramentas que pudessem agilizar a construção de documentação formal. Seguem algumas considerações pessoais:

Documentação que considero boa tem objetivos claros, detalha escolhas *de projeto* (quando relevantes para o objetivo), traz resultados e, quando o autor quiser, comentários. O formato pode ser o de um artigo, tutorial, manual (de usuário, de desenvolvedor,...), livro ou capítulo de livro,... o que, na opinião de quem fizer, melhor atender ao objetivo.

Também percebi que trechos de documentos formais podem ser reaproveitados de maneira lícita, por exemplo, quando os *projetos* são suficientemente próximos.

Sim, na minha experiência, geralmente, documentação formal está associada a um *projeto* ou *plano*. Estes podem, ou não, ter documentação formal associada. Quando têm documentação, referenciar-se ao *projeto* ou *plano* traz clareza e facilita escolhas mas, na vida, há acasos (contingências), que nos impedem ou nos favorecem a agir.

Apesar de ter explicado apenas superficialmente (ainda), usarei como *elemento de partida das anotações* as atividades (individuais) diárias, indexadas por data em que a atividade foi anotada. 

As associações entre as anotações usam representação de conhecimento e web semântica (explicação breve: baseadas em triplas Sujeito-Predicado-Objeto, com vocabulários controlados : ontologias, no jargão da web semântica). É uma escolha de projeto, tem justificativa, mas não vou apresentá-la neste momento.

As anotações podem ser revisitadas e reescritas. Frequentemente me vejo na situação de arrepender-me de não ter guardado a versão anterior de algum documento que modifiquei, por exemplo, porque a versão anterior continha uma lista de links que seria útil para um novo *projeto* mas que removi da versão atual porque não era pertinente no documento final. Conclusão: controle de versão é interessante, embora eu ainda não saiba como vou recuperar a informação (porque vou acabar esquecendo que está lá).

A coleção de requisitos e de escohas de projeto apresentadas acima mostra claramente (para mim) que precisarei de um editor de texto que facilite a inserção de triplas. Estas devem ser inseridas de maneira a ser facilmente localizadas (regex) e transformadas em grafos de conhecimento (construir ferramenta específica). Esses grafos podem ser enriquecidos (construir ferramenta específica) e consultados, através de SPARQL (ferramenta da web semântica que já existe).

Este documento pode ser a base para um artigo, tutorial, ... sei lá o quê!

Neste momento, desejo dar algumas respostas diretas.

 

## Q&A

1. O editor é original ou baseia-se em outro trabalho?
    Baseia-se em https://techvidvan.com/tutorials/text-editor-notepad-project-python/ . Fiz alguns ajustes (porque mesmo sendo o original de 2022, em algum momento deixou de funcionar, mas o conserto estava documentado nos comentários - começo a ver vantagem em ter anotado isso...)

2. Como faço para instalar e executar o EditorPP?
	O EditorPP tem requisitos de sistema. Basicamente, `Python3` e a biblioteca `TkInter`. Siga as instruções de https://techvidvan.com/tutorials/text-editor-notepad-project-python/ para instalação do TkInter, baixe a [pasta contendo os fontes do editor](./EditorPP) e, do terminal, a partir do diretório EditorPP, execute `python3 -m text_editor`.

## Registro histórico



