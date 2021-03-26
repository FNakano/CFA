## 2021-01-27-202634

da forma como a tabela está armazenada (na memória do R), `M[1,7]` e `M$'Data/Hora'[1]` ou são coisas diferentes, ou é a mesma coisa tratada diferente. 




Tentei instalar tidyverse mas deu erros

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

install.packages("readxl")
ls
ls()
pwd()
dir()
M <- read_excel("Planilha Dados Pluviômetro.xlsx")
library(readxl)
M <- read_excel("Planilha Dados Pluviômetro.xlsx")
dim(M)
colnames(M)
M$"Município"[1]
M$"Data/Hora"[1]
M[1,2]
M[1,1]
getwd()
excel_sheets(M)
excel_sheets(https://stackoverflow.com/questions/7049272/importing-excel-files-into-r-xlsx-or-xlsx)
excel_sheets("Planilha Dados Pluviômetro.xlsx")
help (read_excel)
M[1,7]
year(M[1,7])
strsplit(year(M[1,7])," ")
strsplit(M[1,7]," ")
M[1,8]
M[1,8]+M[2,8]
M[2,8]
sum(M[1:200,8]
)
library(lubridate)
install.packages("lubridate")
library(lubridate)
year(M[1,7])
M[1,7]
ymd_hms(M[1,7])
plot (M[1:100,7])
M[1:100,7]
print(M[1:100,7])
print(M[1:100,7], len=100)
help (print)
print(M[1:100,7], width=100)
M[10:100,7]
hour(M[10:100,7])
tibble(
  a = lubridate::now() + runif(1e3) * 86400,
  b = lubridate::today() + runif(1e3) * 30,
  c = 1:1e3,
  d = runif(1e3),
  e = sample(letters, 1e3, replace = TRUE)
)
library(tidyverse)
install.packages("tidyverse")
library(tidyverse)
install.packages("tidyverse")A
library(tidyverse)
hour(M[10:100,7])
history()
savehistory("history.txt")

https://mail.google.com/mail/u/1/#inbox
https://drive.google.com/drive/u/1/folders/1SuG3xVAT8ejjmV8nrBcl1tfkovKw5iy_
https://mail.google.com/mail/u/0/#inbox
https://web.whatsapp.com/
https://github.com/FNakano/CFA/tree/master/programas/R
https://github.com/santanajods/domotic-swot
https://stackoverflow.com/questions/7049272/importing-excel-files-into-r-xlsx-or-xls
https://github.com/tidyverse/readxl
https://www.google.com/search?channel=fs&client=ubuntu&q=R+tibble
https://tibble.tidyverse.org/
https://www.tidyverse.org/
https://cran.r-project.org/web/packages/tibble/vignettes/tibble.html
https://r4ds.had.co.nz/dates-and-times.html
https://r4ds.had.co.nz/tibbles.html
https://lubridate.tidyverse.org/index.html
https://www.google.com/search?channel=fs&client=ubuntu&q=Error+in+as.POSIXlt.default%28x%2C+tz+%3D+tz%28x%29%29+%3A++++do+not+know+how+to+convert+%27x%27+to+class+%E2%80%9CPOSIXlt%E2%80%9D+lubridate
https://stackoverflow.com/questions/41385646/error-in-posixlt
https://www.reddit.com/r/RStudio/comments/9eny68/difficulty_with_dates_and_getting_day_of_the_week/
https://www.google.com/search?client=ubuntu&hs=v6F&channel=fs&sxsrf=ALeKk02axzx5V05Ce7Rot-4bfnuBS--aEQ%3A1611781022804&ei=ntMRYOm8MIzR5OUP08SoqAU&q=r+tibble+working+with+dttm&oq=r+tibble+working+with+dttm&gs_lcp=CgZwc3ktYWIQAzoHCAAQRxCwAzoHCCMQsAIQJ1CpzAJY2e8CYNj4AmgBcAJ4AIABfIgBqA2SAQQwLjE1mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjpg8eagL3uAhWMKLkGHVMiClUQ4dUDCAw&uact=5
https://r4ds.had.co.nz/tibbles.html
https://www.google.com/search?channel=fs&client=ubuntu&q=1%3A+In+install.packages%28%22tidyverse%22%29+%3A+++installation+of+package+%E2%80%98curl%E2%80%99+had+non-zero+exit+status
https://stackoverflow.com/questions/43592316/warning-in-install-packages-installation-of-package-tidyverse-had-non-zero-e
https://www.google.com/search?channel=fs&client=ubuntu&q=R+list+history
https://stackoverflow.com/questions/2749390/command-history-in-r
https://www.google.com/search?client=ubuntu&hs=waH&channel=fs&sxsrf=ALeKk005_t2W0DSZJo1NMtyFQNGdQK_B8A%3A1611786727066&ei=5-kRYMTIA5675OUP0rar8As&q=lubridate+year%28%29+Error+in+as.POSIXlt.default%28x%2C+tz+%3D+tz%28x%29%29+%3A++++do+not+know+how+to+convert+%27x%27+to+class+%E2%80%9CPOSIXlt%E2%80%9D&oq=lubridate+year%28%29+Error+in+as.POSIXlt.default%28x%2C+tz+%3D+tz%28x%29%29+%3A++++do+not+know+how+to+convert+%27x%27+to+class+%E2%80%9CPOSIXlt%E2%80%9D&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoFCAAQywFQwY8DWK-KBGCSjgRoAnACeACAAYABiAGaC5IBBDAuMTKYAQCgAQGgAQKqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwiE2Me6lb3uAhWeHbkGHVLbCr4Q4dUDCAw&uact=5
https://stackoverflow.com/questions/41385646/error-in-posixlt
https://www.reddit.com/r/RStudio/comments/9eny68/difficulty_with_dates_and_getting_day_of_the_week/
https://lubridate.tidyverse.org/
https://www.google.com/search?channel=fs&client=ubuntu&q=tibble+dttm
https://bookdown.org/mikemahoney218/LectureBook/working-with-dates-and-times.html
https://tibble.tidyverse.org/articles/types.html
https://cran.r-project.org/web/packages/tibbletime/tibbletime.pdf
https://cran.r-project.org/web/packages/tibbletime/readme/README.html
https://www.google.com/search?channel=fs&client=ubuntu&q=posixlt.default
https://stackoverflow.com/questions/41385646/error-in-posixlt
https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/as.POSIX*
https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/timezones
https://www.google.com/search?channel=fs&client=ubuntu&q=LUBRIDATE+SOURCE
https://github.com/tidyverse/lubridate/tree/master/src
https://www.google.com/search?channel=fs&client=ubuntu&q=R+coerse+to+string
https://stat.ethz.ch/R-manual/R-devel/library/base/html/toString.html
https://www.google.com/search?channel=fs&client=ubuntu&q=tibble+dttm+to+string
https://stackoverflow.com/questions/59644534/r-converting-datetime-to-an-actual-string

## 2021-01-29-210813

Carregando csv gerado pelo thingspeak...

<pre>&gt; setwd(&quot;dados-Guarulhos&quot;)
&gt; M &lt;- read_csv(&quot;feeds-BME280.csv&quot;)

<font color="#2AA198">──</font> <b>Column specification</b> <font color="#2AA198">────────────────────────────────────────────────────────</font>
cols(
  created_at = <font color="#DC322F">col_character()</font>,
  entry_id = <font color="#859900">col_double()</font>,
  field1 = <font color="#859900">col_double()</font>,
  temperatura = <font color="#859900">col_double()</font>,
  `umidade relativa` = <font color="#859900">col_double()</font>,
  pressão = <font color="#859900">col_double()</font>,
  latitude = <font color="#B58900">col_logical()</font>,
  longitude = <font color="#B58900">col_logical()</font>,
  elevation = <font color="#B58900">col_logical()</font>,
  status = <font color="#DC322F">col_character()</font>
)

&gt; M[1,1]
<font color="#949494"># A tibble: 1 x 1</font>
  created_at             
  <font color="#949494"><i>&lt;chr&gt;</i></font>                  
<font color="#BCBCBC">1</font> 2020-05-26 16:44:30 -03
&gt; ymd_hms(M[1,1])
[1] &quot;2020-05-26 19:44:30 UTC&quot;
&gt; 

</pre>

embora o read_csv do tidyverse, que usa tibble, não leia a primeira coluna como um dttm (acredito que seja por causa do timezone -03, ymd_hms lê e converte para UTC.

## 2021-01-30-185504

Aconteceu alguma coisa: atualização de biblioteca do R, instabilidade no algoritmo de tipagem, falha de operador, ... o que não funcionava ontem funcionou hoje. Até gastei um tempo escrevendo sobre o provavel problema. Para não jogar fora, vem para cá.

## Incompatibilidades inesperadas

Carreguei um arquivo CSV contendo informação de data, da plataforma ThingSpeak. O formato, em caracteres, é ligeiramente diferente do presente no XLSX que usei como base até agora: a data contém informação de fuso no formato (+,-)(NN). Acrescentando a isso que `read_excel` e `read_csv` tratam datas de forma ligeiramente diferente. O primeiro trouxe a data em formato `<dttm>`, o segundo trouxe uma sequência de caracteres. A sequência de caracteres, convertida por `ymd_hms()` do lubridate traz o resultado em `Posixlt(?)`. `tapply` e `min` do pacote R:base tratam cada tipo de maneira diferente, então o meu *script*, que deveria ser uma pequena variação do *script* em "Juntando tudo...", pode se tornar em uma grande bagunça, a menos que eu invista esforço para, além de fazer as contas, manter o formato compatível.

Depois de umas horas de trabalho:

<pre>&gt; M &lt;- read_csv(paste(nomeDoArquivoAProcessar, &quot;.csv&quot;, sep=&quot;&quot;), 
+ col_types = list(col_datetime(format=(&quot;%Y-%m-%d %H:%M:%S %z&quot;)), col_double(), col_double(), col_double(), col_double(), col_double(), col_logical(), col_logical(), col_logical(), col_character())) # https://lubridate.tidyverse.org/, https://stat.ethz.ch/R-manual/R-patched/library/base/html/paste.html
&gt; M
<font color="#949494"># A tibble: 113,823 x 10</font>
   created_at          entry_id field1 temperatura `umidade relati… pressão
   <font color="#949494"><i>&lt;dttm&gt;</i></font>                 <font color="#949494"><i>&lt;dbl&gt;</i></font>  <font color="#949494"><i>&lt;dbl&gt;</i></font>       <font color="#949494"><i>&lt;dbl&gt;</i></font>            <font color="#949494"><i>&lt;dbl&gt;</i></font>   <font color="#949494"><i>&lt;dbl&gt;</i></font>
<font color="#BCBCBC"> 1</font> 2020-05-26 <font color="#949494">19:44:30</font>        1 <u style="text-decoration-style:single">468</u>878        21.8             34.4  <u style="text-decoration-style:single">92</u>685.
<font color="#BCBCBC"> 2</font> 2020-05-26 <font color="#949494">19:44:51</font>        2 <u style="text-decoration-style:single">489</u>460        21.9             33.8  <u style="text-decoration-style:single">92</u>689.
<font color="#BCBCBC"> 3</font> 2020-05-26 <font color="#949494">19:45:12</font>        3 <u style="text-decoration-style:single">510</u>143        22.0             33.9  <u style="text-decoration-style:single">92</u>692.
<font color="#BCBCBC"> 4</font> 2020-05-26 <font color="#949494">19:45:58</font>        4 <u style="text-decoration-style:single">556</u>603        21.9             33.7  <u style="text-decoration-style:single">92</u>691.
<font color="#BCBCBC"> 5</font> 2020-05-26 <font color="#949494">19:46:19</font>        5 <u style="text-decoration-style:single">577</u>250        21.9             33.8  <u style="text-decoration-style:single">92</u>687.
<font color="#BCBCBC"> 6</font> 2020-05-26 <font color="#949494">19:46:40</font>        6 <u style="text-decoration-style:single">597</u>896        21.9             33.9  <u style="text-decoration-style:single">92</u>697.
<font color="#BCBCBC"> 7</font> 2020-05-26 <font color="#949494">19:47:03</font>        7 <u style="text-decoration-style:single">618</u>579        21.9             34.0  <u style="text-decoration-style:single">92</u>695.
<font color="#BCBCBC"> 8</font> 2020-05-26 <font color="#949494">19:47:24</font>        8 <u style="text-decoration-style:single">642</u>031        22.0             33.7  <u style="text-decoration-style:single">92</u>690.
<font color="#BCBCBC"> 9</font> 2020-05-26 <font color="#949494">19:47:44</font>        9 <u style="text-decoration-style:single">662</u>738        22.0             33.7  <u style="text-decoration-style:single">92</u>697 
<font color="#BCBCBC">10</font> 2020-05-26 <font color="#949494">19:48:05</font>       10 <u style="text-decoration-style:single">683</u>396        22.0             33.6  <u style="text-decoration-style:single">92</u>689.
<font color="#949494"># … with 113,813 more rows, and 4 more variables: latitude </font><font color="#949494"><i>&lt;lgl&gt;</i></font><font color="#949494">,</font>
<font color="#949494">#   longitude </font><font color="#949494"><i>&lt;lgl&gt;</i></font><font color="#949494">, elevation </font><font color="#949494"><i>&lt;lgl&gt;</i></font><font color="#949494">, status </font><font color="#949494"><i>&lt;chr&gt;</i></font>
&gt; ymd_hms(&quot;2020-05-26 16:55:23 -03&quot;)
[1] &quot;2020-05-26 19:55:23 UTC&quot;
&gt; print(ymd_hms(&quot;2020-05-26 16:55:23 -03&quot;))
[1] &quot;2020-05-26 19:55:23 UTC&quot;
&gt; M[1,1]
<font color="#949494"># A tibble: 1 x 1</font>
  created_at         
  <font color="#949494"><i>&lt;dttm&gt;</i></font>             
<font color="#BCBCBC">1</font> 2020-05-26 <font color="#949494">19:44:30</font>
</pre>

#### Referências

https://www.google.com/search?channel=fs&client=ubuntu&q=tibble+read+csv
https://readr.tidyverse.org/reference/read_delim.html
https://www.google.com/search?channel=fs&client=ubuntu&q=lubridate
https://lubridate.tidyverse.org/
https://stat.ethz.ch/R-manual/R-patched/library/base/html/paste.html
https://www.google.com/search?channel=fs&client=ubuntu&q=degree+symbol+in+R+plot
https://lukemiller.org/index.php/2010/05/modifying-basic-plots-in-r/
https://stackoverflow.com/questions/51799118/writing-the-symbol-degrees-celsius-in-axis-titles-with-r-plotly/51799161
https://www.google.com/search?client=ubuntu&hs=dWN&channel=fs&sxsrf=ALeKk01X5SWwHC7Uk5PJmwtPT-bcrh0lBw%3A1611968404514&ei=lK8UYOr7HsC55OUPt46K0AI&q=+tibbles+and+aggregate+functions&oq=+tibbles+and+aggregate+functions&gs_lcp=CgZwc3ktYWIQAzoHCAAQRxCwAzoECAAQQzoCCAA6BggAEAcQHjoFCC4QywE6BQgAEMsBOgsIABDHARCvARDLAToGCAAQFhAeOggIABAWEAoQHjoICCEQFhAdEB46BQghEKABOgQIIRAVOgcIIRAKEKABUOehCFis2QlgidwJaANwAngAgAGbBIgBjyiSAQwwLjMxLjAuMS4xLjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwjqlY-husLuAhXAHLkGHTeHAioQ4dUDCAw&uact=5
https://stackoverflow.com/questions/64769842/how-to-aggregate-a-tibble-by-rows-and-columns
https://www.guru99.com/r-aggregate-function.html
https://www.guru99.com/r-aggregate-function.html#10
https://jennybc.github.io/purrr-tutorial/bk01_base-functions.html
https://www.google.com/search?client=ubuntu&hs=DcN&channel=fs&sxsrf=ALeKk03J9kntlspmjbfszgjm9OxQn4G4Qw%3A1611968750302&ei=7rAUYOCMEsKm5OUP1NCloAU&q=tibble+group_by+versus+tapply&oq=tibble+group_by+versus+tapply&gs_lcp=CgZwc3ktYWIQAzoHCAAQRxCwA1DDNliJcWCjdGgFcAJ4AIAB3wGIAaUUkgEGMS4xNy4ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjgu4DGu8LuAhVCE7kGHVRoCVQQ4dUDCAw&uact=5
https://rstudio-pubs-static.s3.amazonaws.com/46399_ae360f3ec8644c9d9892994a12b0df8d.html
https://stackoverflow.com/questions/23878678/understanding-difference-in-results-between-dplyr-group-by-vs-tapply
https://www.google.com/search?client=ubuntu&hs=o02&channel=fs&sxsrf=ALeKk03t9aCaAuTTjMxRFMZbCDyHPnaFQg%3A1611968997991&ei=5bEUYODxO96_5OUP0I-H2Aw&q=lubridate+relation+to+tibble+dttm&oq=lubridate+relation+to+tibble+dttm&gs_lcp=CgZwc3ktYWIQAzoHCAAQRxCwAzoICAAQsQMQgwE6BQguELEDOgsIABCxAxDHARCjAjoFCAAQsQM6CAguELEDEIMBOgQIIxAnOgYIIxAnEBM6BAguEEM6BAgAEEM6BwgAELEDEEM6AggAOgQIABAKOgUIABDLAToGCAAQFhAeOggIABAWEAoQHjoECAAQDToHCAAQChDLAToGCAAQDRAeOgUIIRCgAToHCCEQChCgAToICCEQFhAdEB5QicEdWJHWHmDb2h5oDHACeAGAAb0DiAGaOJIBCjAuMzIuNC4zLjKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=psy-ab&ved=0ahUKEwig-I28vMLuAhXeH7kGHdDHAcsQ4dUDCAw&uact=5
https://www.google.com/search?channel=fs&client=ubuntu&q=lubridate+as_datetime
https://r4ds.had.co.nz/dates-and-times.html
https://lubridate.tidyverse.org/reference/as_date.html
https://www.google.com/search?channel=fs&client=ubuntu&q=lubridate+as_datetime+origin+not+working
https://stackoverflow.com/questions/40959726/lubridate-as-date-and-as-datetime-differences-in-behavior

## <a id="2021-03-26-110826" href="#2021-03-26-110826">2021-03-26-110826</a>

