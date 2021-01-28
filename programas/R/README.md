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

Parece que dá para carregar os dados, uma folha de dados por vez. (ainda não sei como funciona para fórmulas e macros).

[Referência](https://stackoverflow.com/questions/7049272/importing-excel-files-into-r-xlsx-or-xls)

[Outra referência](https://github.com/tidyverse/readxl)

de dentro do R, em três passos:

1. Baixar e instalar uma biblioteca com `install.packages("readxl")`
   - só precisa fazer uma vez, aí a biblioteca fica instalada.
2. Carregar a biblioteca com: `library(readxl)`
   - precisa carregar toda vez que iniciar o R, a menos que esteja salva do ambiente (por exemplo, quando sair, escolher salvar o ambiente, da próxima vez aue iniciar o R, a biblioteca estará carregada, e as variáveis, e o histórico de comandos).
3. Armazenar o conteúdo do arquivo do Excel em uma variável: `M <- read_excel("Planilha Dados Pluviômetro.xlsx")` isto carrega a primeira folha de dados da planilha.
   - para ver a documentação: `help(read_excel)` para sair do help, digitar q.
   - [exemplos e código-fonte](https://github.com/tidyverse/readxl)


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

## Quando carrego um Excel, Como trabalho com data e hora?

No caso dos arquivos gerados pelo CEMADEN, Data/Hora estão em um formato padronizado (ISO8601), o que facilita sua carga no R.

Para separar Data/Hora em seus elementos, usar a biblioteca `lubridate`.

1. Instalar lubridate: `install.package(lubridate)`
2. Carregar lubridate: `library(lubridate)`

Com isto, selecionar a hora da coluna Data/Hora é feito assim: `hour(M$'Data/Hora') e o resultado:

<pre>&gt; hour(M$&apos;Data/Hora&apos;)
  [1] 13 13 13 13 13 14 14 14 14 14 15 16 16 16 17 18 19 20 21 22 23  0  1  2  3
 [26]  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  0  1  2  3  4
 [51]  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  0  1  2  3  4  5
 [76]  6  7  8  9 10 11 12 13 14 15 15 15 15 15 15 16 16 16 16 16 16 17 17 17 17
[101] 17 17 18 18 18 18 18 18 19 19 19 19 19 19 20 20 20 20 20 20 21 21 21 21 21
[126] 22 22 22 22 22 22 23 23 23 23 23  0  0  1  1  1  1  1  1  2  2  2  2  2  2
[151]  3  4  5  6  7  8  8  8  8  8  8  9 10 10 10 10 10 10 11 11 11 11 11 11 12
[176] 12 12 12 12 13 14 14 14 14 14 14 15 15 15 15 15 15 16 16 16 16 16 16 17 17
[201] 18 19 20 21 22 23 23 23 23 23 23  0  1  2  3  4  5  6  7  8  9 10 11 12 12
[226] 12 13 14 15 16 17 18 19 20 21 22 23  0  1  2  3  4  5  6  7  8  9 10 11 12
[251] 13 14 14 14 14 14 14 15 15 15 15 16 17 18 19 20 21 22 23  0  1  2  3  4  5
[276]  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  0  1  2  3  4  5  6
[301]  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  0  1  2  3  4  5  6  7
[326]  8  9 10 11 12 13 14 15 16 17 18 18 18 18 18 18 19 19 19 19 19 20 20 21 22
[351] 23  0  1  1  1  2  3  4  5  6  7  8  9 10 11 12 13 13 13 13 13 13 14 15 15
[376] 15 15 15 15 16 16 16 16 16 16 17 18 19 20 20 20 20 20 20 21 21 21 21 21 21
[401] 22 22 23  0  1  2  3  4  5  6  7  8  9 10 10 10 10 11 12 13 14 15 16 17 18
[426] 19 20 21 22 23  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
[451] 20 21 22 23
&gt; 
</pre>

## Como faço para agregar os valores por hora?

### Primeira abordagem

Aproveitando que a folha de dados de 2014 contém somente alguns dias de dezembro, criar uma tabela contendo dia, hora e chuva acumulada na hora fica:

``` R
H <- tibble (
a = tapply(day(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
b = tapply(hour(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
c = tapply(M$'Valor Medida', hour(M$'Data/Hora')+24*day(M$'Data/Hora'), sum)
)
```

**nota**: nesta abordagem, a linha de `H` contém dia, hora e volume medido durante a hora, de hora:00 até hora:59:59.9999....

**nota2**: checar qual a referência da hora (ou fuso, ou timezone).

Os 'truque's que não estão nas referências: 

como são data/hora de um único mês, um número que é 24*dia+hora é suficiente para identificar uma determinada hora em um determinado dia. Os valores de chuva dentro desta hora, queremos acumular. tapply faz isso. Referências:

- https://rdrr.io/r/base/tapply.html
- https://stackoverflow.com/questions/3505701/grouping-functions-tapply-by-aggregate-and-the-apply-family
- https://stat.ethz.ch/R-manual/R-devel/library/base/html/tapply.html
- https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/tapply

Cada 24*dia+hora tem até seis valores (por causa dos intervalos de 10 minutos ou de 1 hora usados pelo instrumento). Se esses valores forem o dia de cada medida, todos os valores são iguais e iguais à média.
 
- fim dos truques.

### Segunda abordagem

trabalhando...

https://www.google.com/search?channel=fs&client=ubuntu&q=R+accumulated+sum
https://stackoverflow.com/questions/40042711/how-to-calculate-cumulative-sum
https://www.google.com/search?channel=fs&client=ubuntu&q=r+integer+part
https://stat.ethz.ch/R-manual/R-devel/library/base/html/Round.html
https://www.google.com/search?client=ubuntu&hs=smr&channel=fs&sxsrf=ALeKk02m8SXEEcwxDn19mO-6hyMQiUPHWQ%3A1611846409350&ei=CdMSYMCCFbTX5OUPnK25oAo&q=lubridate+datediff&oq=lubridate+datediff&gs_lcp=CgZwc3ktYWIQAzIFCAAQywEyBggAEBYQHjoHCAAQRxCwAzoGCCMQJxATOgQIIxAnOggIABCxAxCDAToFCC4QsQM6CwgAELEDEMcBEKMCOggILhCxAxCDAToCCAA6BAgAEAM6BAgAEEM6BQgAELEDOgcIABCxAxBDOgQILhBDOgQIABAKOgQIABANOgYIABANEB46CAgAEA0QChAeUK6VAVjiuAFgqboBaAJwAngAgAH0AYgBxhOSAQYxLjE2LjGYAQCgAQGqAQdnd3Mtd2l6yAEEwAEB&sclient=psy-ab&ved=0ahUKEwiAq6Xl877uAhW0K7kGHZxWDqQQ4dUDCAw&uact=5
https://data.library.virginia.edu/working-with-dates-and-time-in-r-using-the-lubridate-package/

library(readxl)
library(tidyverse)
library(lubridate)
M <- read_excel("Planilha Dados Pluviômetro.xlsx")
H <- tibble (
a = tapply(day(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
b = tapply(hour(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
c = tapply(M$'Valor Medida', hour(M$'Data/Hora')+24*day(M$'Data/Hora'), sum)
)
H %>% print (n=Inf, width=Inf)
M$'Data/Hora'
M$'Data/Hora'[2:200]-M$'Data/Hora'[1:199]

M$'Data/Hora'[1:200]-M$'Data/Hora'[1]
(M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/(24*3600)
int((M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/(24*3600))
trunc((M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/(24*3600))

(M$'Data/Hora'[1:200]-M$'Data/Hora'[1])

as.duration(M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/ddays(1)
trunc(as.duration(M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/ddays(1))
trunc(as.duration(M$'Data/Hora'[1:200]-M$'Data/Hora'[1])/dhours(1))
mean(M$'Data/Hora'[1:200])
max(M$'Data/Hora'[1:200])


## Como faço para imprimir a tabela toda na tela? (a tabela é um tibble)

Imprimir a tabela toda na tela: `H %>% print (n=Inf, width=Inf)`

[Referência](https://r4ds.had.co.nz/tibbles.html)

### Juntando tudo para ter volume acumulado de chuva por hora usando a primeira abordagem

O script inteiro fica:

``` R
library(readxl)
library(tidyverse)
library(lubridate)
M <- read_excel("Planilha Dados Pluviômetro.xlsx")
H <- tibble (
a = tapply(day(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
b = tapply(hour(M$'Data/Hora'), hour(M$'Data/Hora')+24*day(M$'Data/Hora'), mean),
c = tapply(M$'Valor Medida', hour(M$'Data/Hora')+24*day(M$'Data/Hora'), sum)
)
H %>% print (n=Inf, width=Inf)
```

## Como faço para ver todos os comandos que usei durante a seção?

`history()`

## Como faço para salvar em um arquivo todos os comandos que usei durante a seção?

`savehistory('arquivo.txt')`

[Referência](https://stackoverflow.com/questions/2749390/command-history-in-r)

## Tentei instalar tidyverse no Ubuntu/Linux com install.package("tidyverse") mas deu erro, o que faço?

Veja se o erro é o abaixo:

<pre>** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (ggplot2)
ERROR: dependencies ‘httr’, ‘rvest’, ‘xml2’ are not available for package ‘tidyverse’
* removing ‘/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/tidyverse’

The downloaded source packages are in
	‘/tmp/RtmpEGuoep/downloaded_packages’
Warning messages:
1: In install.packages(&quot;tidyverse&quot;) :
  installation of package ‘curl’ had non-zero exit status
2: In install.packages(&quot;tidyverse&quot;) :
  installation of package ‘xml2’ had non-zero exit status
3: In install.packages(&quot;tidyverse&quot;) :
  installation of package ‘httr’ had non-zero exit status
4: In install.packages(&quot;tidyverse&quot;) :
  installation of package ‘rvest’ had non-zero exit status
5: In install.packages(&quot;tidyverse&quot;) :
  installation of package ‘tidyverse’ had non-zero exit status
&gt; library(tidyverse)
Error in library(tidyverse) : there is no package called ‘tidyverse’
</pre>

Instalei programas adicionais no linux, de acordo com a [referência](https://stackoverflow.com/questions/43592316/warning-in-install-packages-installation-of-package-tidyverse-had-non-zero-e)

linha de comando: `sudo apt install libxml2-dev libcurl4-openssl-dev libssl-dev`

... então tentei instalar tidyverse novamente:

<pre>* DONE (rvest)
* installing *source* package ‘tidyverse’ ...
** package ‘tidyverse’ successfully unpacked and MD5 sums checked
** using staged installation
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
*** copying figures
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (tidyverse)

The downloaded source packages are in
	‘/tmp/RtmpEGuoep/downloaded_packages’
&gt; library(tidyverse)
── <b>Attaching packages</b> ──────────────────────────────────────────────────────── tidyverse 1.3.0 ──
<font color="#859900">✔</font> <font color="#268BD2">ggplot2</font> 3.3.3     <font color="#859900">✔</font> <font color="#268BD2">purrr  </font> 0.3.4
<font color="#859900">✔</font> <font color="#268BD2">tibble </font> 3.0.5     <font color="#859900">✔</font> <font color="#268BD2">dplyr  </font> 1.0.3
<font color="#859900">✔</font> <font color="#268BD2">tidyr  </font> 1.1.2     <font color="#859900">✔</font> <font color="#268BD2">stringr</font> 1.4.0
<font color="#859900">✔</font> <font color="#268BD2">readr  </font> 1.4.0     <font color="#859900">✔</font> <font color="#268BD2">forcats</font> 0.5.0
── <b>Conflicts</b> ─────────────────────────────────────────────────────────── tidyverse_conflicts() ──
<font color="#DC322F">✖</font> <font color="#268BD2">lubridate</font>::<font color="#859900">as.difftime()</font> masks <font color="#268BD2">base</font>::as.difftime()
<font color="#DC322F">✖</font> <font color="#268BD2">lubridate</font>::<font color="#859900">date()</font>        masks <font color="#268BD2">base</font>::date()
<font color="#DC322F">✖</font> <font color="#268BD2">dplyr</font>::<font color="#859900">filter()</font>          masks <font color="#268BD2">stats</font>::filter()
<font color="#DC322F">✖</font> <font color="#268BD2">lubridate</font>::<font color="#859900">intersect()</font>   masks <font color="#268BD2">base</font>::intersect()
<font color="#DC322F">✖</font> <font color="#268BD2">dplyr</font>::<font color="#859900">lag()</font>             masks <font color="#268BD2">stats</font>::lag()
<font color="#DC322F">✖</font> <font color="#268BD2">lubridate</font>::<font color="#859900">setdiff()</font>     masks <font color="#268BD2">base</font>::setdiff()
<font color="#DC322F">✖</font> <font color="#268BD2">lubridate</font>::<font color="#859900">union()</font>       masks <font color="#268BD2">base</font>::union()
&gt; 
</pre>

[Referência](https://stackoverflow.com/questions/43592316/warning-in-install-packages-installation-of-package-tidyverse-had-non-zero-e)


**notas para desenvolvedores e usuários do R de antes de 2016** ainda não sei o que é um `tibble`...
*tibble* é o jeito moderno dos dataframes. 

A justificativa que, para mim, faz essa explicação ter algum sentido tem a ver com desenvolvimento de programas: As versões iniciais de R (lá pelos 2000), usavam dataframes como estrutura de armazenamento dos valores nas variáveis, por exemplo, tabelas eram dataframes. À medida que R foi evoluindo, a implementação dos dataframes no programa foi evoluindo, e ficando complicada, às vezes por funcionalidades que poucos aproveitavam. Em um momento, os usuários/mantenedores/programadores de R resolveram limpar o código-fonte, mantendo compatibilidade com versões anteriores. Para isso, criaram o conceito de *tibble*.

[Tidyverse](https://www.tidyverse.org/)
[Tibble no Tidyverse](https://tibble.tidyverse.org/)
[Tibble no R](https://cran.r-project.org/web/packages/tibble/vignettes/tibble.html)

Em primeiro.R usei dataframes quando fiz `read.csv`. Para que as datas fossem carregadas como palavras, ou, Strings, (para que eu pudesse separar ano, mês, dia), precisei procurar uma solução e ir testando, chegando a `as.is=TRUE`. A promessa é que com tibble não seria necessário usar o `as.is`.

Ainda sobre datas e tibbles, a data no arquivo foi lida como um dttm, que é um tibble para data e hora. Tentei aplicar uma função sobre strings, mas o tipo não permite:

<pre>&gt; M[1,7]
<font color="#949494"># A tibble: 1 x 1</font>
  `Data/Hora`        
  <font color="#949494"><i>&lt;dttm&gt;</i></font>             
<font color="#BCBCBC">1</font> 2014-12-19 <font color="#949494">13:10:00</font>
&gt; strsplit(M[1,7],&quot; &quot;)
Error in strsplit(M[1, 7], &quot; &quot;) : argumento modo não caractere
&gt; 
</pre>

Para lidar com datas dentro de *tibbles* precisaria da biblioteca [lubridate](https://r4ds.had.co.nz/dates-and-times.html), então fica seis por meia-dúzia. Ou trabalha com Strings, ou trabalha com *tibble*.

Quanto a lidar com números, o exemplo abaixo:

<pre>&gt; M[1,8]
<font color="#949494"># A tibble: 1 x 1</font>
  `Valor Medida`
           <font color="#949494"><i>&lt;dbl&gt;</i></font>
<font color="#BCBCBC">1</font>            0.2
&gt; M[1,8]+M[2,8]
  Valor Medida
1            2
&gt; M[2,8]
<font color="#949494"># A tibble: 1 x 1</font>
  `Valor Medida`
           <font color="#949494"><i>&lt;dbl&gt;</i></font>
<font color="#BCBCBC">1</font>            1.8
&gt; sum(M[1:200,8]
+ )
[1] 136.2
&gt; 
</pre>

A notação do *tibble* é mais verbosa, o que pode atrapalhar quem usa...

Como carreguei a planilha com algo que usa tibbles, então, para pré-tratar os dados para uma escala horária, melhor usar lubridate...

<pre>&gt; library(lubridate)
Error in library(lubridate) : there is no package called ‘lubridate’
&gt; install.packages(&quot;lubridate&quot;)
Installing package into ‘/home/fabio/R/x86_64-pc-linux-gnu-library/3.6’
(as ‘lib’ is unspecified)
also installing the dependency ‘generics’

tentando a URL &apos;https://cloud.r-project.org/src/contrib/generics_0.1.0.tar.gz&apos;
Content type &apos;application/x-gzip&apos; length 117834 bytes (115 KB)
==================================================
downloaded 115 KB

tentando a URL &apos;https://cloud.r-project.org/src/contrib/lubridate_1.7.9.2.tar.gz&apos;
Content type &apos;application/x-gzip&apos; length 472640 bytes (461 KB)
==================================================
downloaded 461 KB

* installing *source* package ‘generics’ ...
** package ‘generics’ successfully unpacked and MD5 sums checked
** using staged installation
** R
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (generics)
* installing *source* package ‘lubridate’ ...
** package ‘lubridate’ successfully unpacked and MD5 sums checked
** using staged installation
** libs
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_fixed.cc -o cctz/src/time_zone_fixed.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_if.cc -o cctz/src/time_zone_if.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_impl.cc -o cctz/src/time_zone_impl.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_info.cc -o cctz/src/time_zone_info.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_libc.cc -o cctz/src/time_zone_libc.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_lookup.cc -o cctz/src/time_zone_lookup.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/time_zone_posix.cc -o cctz/src/time_zone_posix.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c cctz/src/zone_info_source.cc -o cctz/src/zone_info_source.o
ar rcs libcctz.a ./cctz/src/time_zone_fixed.o ./cctz/src/time_zone_if.o ./cctz/src/time_zone_impl.o ./cctz/src/time_zone_info.o ./cctz/src/time_zone_libc.o ./cctz/src/time_zone_lookup.o ./cctz/src/time_zone_posix.o ./cctz/src/zone_info_source.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c RcppExports.cpp -o RcppExports.o
g++ -std=gnu++11 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c update.cpp -o update.o
gcc -std=gnu99 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c utils.c -o utils.o
gcc -std=gnu99 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c datetime.c -o datetime.o
gcc -std=gnu99 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c period.c -o period.o
gcc -std=gnu99 -I&quot;/usr/share/R/include&quot; -DNDEBUG -I. -I./cctz/src/ -I&quot;/home/fabio/R/x86_64-pc-linux-gnu-library/3.6/Rcpp/include&quot;   -fpic  -g -O2 -fdebug-prefix-map=/build/r-base-jbaK_j/r-base-3.6.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g  -c tparse.c -o tparse.o
g++ -std=gnu++11 -shared -L/usr/lib/R/lib -Wl,-Bsymbolic-functions -Wl,-z,relro -o lubridate.so RcppExports.o update.o utils.o datetime.o period.o tparse.o -L. -lcctz -L/usr/lib/R/lib -lR
installing to /home/fabio/R/x86_64-pc-linux-gnu-library/3.6/00LOCK-lubridate/00new/lubridate/libs
** R
** data
*** moving datasets to lazyload DB
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
*** copying figures
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** checking absolute paths in shared objects and dynamic libraries
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (lubridate)

The downloaded source packages are in
	‘/tmp/RtmpEGuoep/downloaded_packages’
&gt; 
&gt; library(lubridate)

Attaching package: ‘lubridate’

The following objects are masked from ‘package:base’:

    date, intersect, setdiff, union

&gt; year(M[1,7])
Error in as.POSIXlt.default(x, tz = tz(x)) : 
  do not know how to convert &apos;x&apos; to class “POSIXlt”
&gt; 
&gt; M$&apos;Data/Hora&apos;[1]
[1] &quot;2014-12-19 13:10:00 UTC&quot;
&gt; hour(M$&apos;Data/Hora&apos;[1])
[1] 13
</pre>

**atenção**: Para conseguir selecionar uma parte da data/hora, tem que referenciar a variável como `M$'Data/Hora'[1]. Referenciar como `M[1,7]` faz `year(), month(), day(), hour(),...` todas dar erro.

### Tecnicalidades sobre o tibble dttm

<pre>&gt; M$&apos;Data/Hora&apos;[1]
[1] &quot;2014-12-19 13:10:00 UTC&quot;
&gt; M$[1,7]
Erro: &apos;[&apos; inesperado in &quot;M$[&quot;
&gt; M[1,7]
<font color="#949494"># A tibble: 1 x 1</font>
  `Data/Hora`        
  <font color="#949494"><i>&lt;dttm&gt;</i></font>             
<font color="#BCBCBC">1</font> 2014-12-19 <font color="#949494">13:10:00</font>
&gt; as.character(M[1,7])
[1] &quot;1418994600&quot;
&gt; 

</pre>

O valor 1418994600 corresponde à quantidade de milissegundos decorridos desde 1970-01-01 00:00:00, que é [UNIX Epoch](https://en.wikipedia.org/wiki/Unix_time)

Vi isto numa tentativa frustrada de converter o tibble para string, baseada na informação em https://stackoverflow.com/questions/59644534/r-converting-datetime-to-an-actual-string

`toString(M[1,7])` resuta igual. [Ref](https://stat.ethz.ch/R-manual/R-devel/library/base/html/toString.html)

Código-fonte de lubridate no github: https://github.com/tidyverse/lubridate

Documentação sobre timezones em R: https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/timezones

`format(M[1,7])` é mais estranho ainda: São códigos ANSI, no estilo dos que é usado para apresentar a saída colorida no terminal do Linux.

<pre>&gt; M[1,7]
<font color="#949494"># A tibble: 1 x 1</font>
  `Data/Hora`        
  <font color="#949494"><i>&lt;dttm&gt;</i></font>             
<font color="#BCBCBC">1</font> 2014-12-19 <font color="#949494">13:10:00</font>
&gt; as.character(M[1,7])
[1] &quot;1418994600&quot;
&gt; format(M[1,7])
[1] &quot;\033[38;5;246m# A tibble: 1 x 1\033[39m&quot;                          
[2] &quot;  `Data/Hora`        &quot;                                            
[3] &quot;  \033[3m\033[38;5;246m&lt;dttm&gt;\033[39m\033[23m             &quot;       
[4] &quot;\033[38;5;250m1\033[39m 2014-12-19 \033[38;5;246m13:10:00\033[39m&quot;
&gt; 
</pre>

Essa tentativa foi inspirada por: https://stackoverflow.com/questions/41385646/error-in-posixlt

https://tibble.tidyverse.org/articles/types.html
https://bookdown.org/mikemahoney218/LectureBook/working-with-dates-and-times.html
https://lubridate.tidyverse.org/
https://r4ds.had.co.nz/tibbles.html
https://r4ds.had.co.nz/dates-and-times.html
https://cran.r-project.org/web/packages/tibble/vignettes/tibble.html
https://tibble.tidyverse.org/

Tem uma bagunça de representações de datas em R, e uma bagunça de dúvidas e respostas:

https://stackoverflow.com/questions/41385646/error-in-posixlt


