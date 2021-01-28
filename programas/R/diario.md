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


