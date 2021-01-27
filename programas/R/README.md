# R

## Motivação

Aproveitar a oportunidade de analisar dados usando R para documentar etapas de análise, soluções e scripts.

Documentar os pedidos e as soluções feitos por colaboradores.

## Introdução

R é um ambiente para análise estatística. Com ele é possível carregar dados armazenados em tabelas e manipulá-las, por exemplo, fazendo gráficos, aplicando testes e modelos estatísticos em poucos comandos. 

O [site oficial](https://www.r-project.org/) permite o download do programa para Linux, Windows e Mac, da [documentação](https://cran.r-project.org/manuals.html), e permite acompanhar as notícias dos desenvolvedores da ferramenta.

Há muito material gratuito  na internet. Uma busca por `R tutorials` mostra isso. Vou listando abaixo o que encontrei e minha impressão (superficial) sobre o material.

1. [Este link é o primeiro capítulo do material do referido site, que cobre instalação, geração de gráficos análise de regressão e segue aplicando em geoestatística](https://geokrigagem.com.br/geoestatistica-no-r-como-instalar-tutorial/).
2. [Este apresenta a experiência de dois estudantes do IB](http://ecovirtual.ib.usp.br/doku.php?id=ecovirt:roteiro:soft:rprincip).
3. [Este PDF está no e-disciplinas e explica bem as janelas no R-Studio, antes de mostrar e explicar os comandos básicos](https://edisciplinas.usp.br/pluginfile.php/4883125/mod_resource/content/1/Tutorial.pdf).
4. [Este é um tutorial gratuito bastante completo usado para promover livros sobre tópicos mais avançados](http://www.r-tutor.com/r-introduction).

## Como começar com o R?

Depois de baixar e instalar, iniciar e aprender alguns comandos básicos. Na lista acima, [1,3] mostram o passo a passo para baixar, instalar e iniciar. Caso goste do material, siga com ele para os comandos básicos.

[2,4] Iniciam pelos comandos básicos, [4] tem muita informação, avançando sobre tópicos mais complexos.

## De dentro do R, como sei em que pasta estou e que arquivos estão na pasta?

- Em que pasta estou: `getwd()`
- Que arquivos tem na pasta: `dir()`
- Quero ir para *C:\outraPasta*: `setwd("C:\outraPasta"`

## Dá para carregar arquivos do Excel?

Parece que dá para carregar os dados (ainda não sei como funciona para fórmulas e macros).

[Referência](https://stackoverflow.com/questions/7049272/importing-excel-files-into-r-xlsx-or-xls)

de dentro do R, em três passos:

1. Baixar e instalar uma biblioteca com `install.packages("readxl")`
   - só precisa fazer uma vez, aí a biblioteca fica instalada.
2. Carregar a biblioteca com: `library(readxl)`
   - precisa carregar toda vez que iniciar o R, a menos que esteja salva do ambiente (por exemplo, quando sair, escolher salvar o ambiente, da próxima vez aue iniciar o R, a biblioteca estará carregada, e as variáveis, e o histórico de comandos).
3. Armazenar o conteúdo do arquivo do Excel em uma variável: `M <- read_excel("Planilha Dados Pluviômetro.xlsx")`


<pre>&gt; ls()
character(0)
&gt; pwd()
Error in pwd() : não foi possível encontrar a função &quot;pwd&quot;
&gt; dir()
[1] &quot;Planilha Dados Pluviômetro.xlsx&quot;
&gt; M &lt;- read_excel(&quot;Planilha Dados Pluviômetro.xlsx&quot;)
Error in read_excel(&quot;Planilha Dados Pluviômetro.xlsx&quot;) : 
  não foi possível encontrar a função &quot;read_excel&quot;
&gt; library(readxl)
&gt; M &lt;- read_excel(&quot;Planilha Dados Pluviômetro.xlsx&quot;)
&gt; dim(M)                                                                      
[1] 454   8
&gt; colnames(M)
[1] &quot;Município&quot;       &quot;Cód Estação&quot;     &quot;UF&quot;              &quot;Nome da Estação&quot;
[5] &quot;Latutude&quot;        &quot;Longitude&quot;       &quot;Data/Hora&quot;       &quot;Valor Medida&quot;   
&gt; M$&quot;Município&quot;[1]
[1] &quot;MOGI DAS CRUZES&quot;
&gt; M$&quot;Data/Hora&quot;[1]
[1] &quot;2014-12-19 13:10:00 UTC&quot;
&gt; M[1,2]
<font color="#949494"># A tibble: 1 x 1</font>
  `Cód Estação`
  <font color="#949494"><i>&lt;chr&gt;</i></font>        
<font color="#BCBCBC">1</font> 353060704A   
&gt; M[1,1]
<font color="#949494"># A tibble: 1 x 1</font>
  Município      
  <font color="#949494"><i>&lt;chr&gt;</i></font>          
<font color="#BCBCBC">1</font> MOGI DAS CRUZES
&gt; 

</pre>

**nota** ainda não sei o que é um `tibble`...


