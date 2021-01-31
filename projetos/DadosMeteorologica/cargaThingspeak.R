############################
# Lê o arquivo <nomeDoArquivoAProcessar>.csv, gera o arquivo <nomeDoArquivoAProcessar>-processado.csv.

############################

# Carrega bibliotecas

library(readxl)
library(tidyverse)
library(lubridate)

nomeDoArquivoAProcessar <- "feeds-BME280"

M <- read_csv(paste(nomeDoArquivoAProcessar, ".csv", sep=""))  # https://lubridate.tidyverse.org/, https://stat.ethz.ch/R-manual/R-patched/library/base/html/paste.html

# Determina qual é a primeira hora cheia

horaCheia <- make_datetime(year(M$created_at[1]), month(M$created_at[1]), day(M$created_at[1]), hour(M$created_at[1]))

# Calcula um índice que é o intervalo (tempo decorrido) da data inicial da série na planilha até a data da medida, em horas.

Idx <- (horaCheia %--% M$created_at)/dhours(1)

# Seleciona a DataHoraInicio e calcula temperatura, umidade relativa e pressão médios durante a hora, independente da resolução do dado dentro da hora. Armazena em uma tabela com quatro colunas.

D <- tibble (
  DataHoraInicio = tapply (M$created_at, trunc(Idx), min),  # no script antigo, não declarar col_types na linha 15 vai provocar um erro nesta linha.
  temperaturaMedia = tapply (M$'temperatura', trunc(Idx), mean),
  umidadeMedia = tapply (M$'umidade relativa', trunc(Idx), mean),
  pressaoMedia = tapply (M$'pressão', trunc(Idx), mean)
)

# Cria H, uma tabela, com as colunas Ano, Mes, Dia, HoraInicio de cada linha de D.

H <- tibble (
  Ano = year (D$DataHoraInicio),
  Mes = month (D$DataHoraInicio),
  Dia = day (D$DataHoraInicio),
  HoraInicio = hour (D$DataHoraInicio)
)

# Cria novoM, uma tabela, com a concatenação das tabelas H e D, colocando as colunas lado a lado.

novoM <- bind_cols(H, D);

write_csv (novoM, file = paste(nomeDoArquivoAProcessar, "-processado.csv", sep="")) # separador decimal é ponto, separador de elementos é vírgula, palavras recebem double-quotes.

# write.table (novoM, file = paste(nomeDoArquivoAProcessar, "-processado.csv", sep=""), sep=";", dec=",", quote=FALSE, row.names=FALSE) # separador decimal é vírgula, separador de elementos é ponto-e-vírgula, palavras não recebem double-quotes. Não é possivel ler o arquivo resultante com read_csv. 

diaCheio <- make_datetime(year(M$created_at[1]), month(M$created_at[1]), day(M$created_at[1]), 3) # a hora é 3 por causa da correção do fuso!

# Gera o gráfico de temperatura média diária, para sinalizar o término.

Idx <- (diaCheio %--% novoM$DataHoraInicio)/ddays(1)

# Seleciona a DataHoraInicio e calcula o volume acumulado durante a hora, independente da resolução do dado dentro da hora. Armazena em uma tabela com duas colunas.

G <- tibble (
  DataHoraInicio = tapply (novoM$DataHoraInicio, trunc(Idx), min),  # no script antigo, não declarar col_types na linha 15 vai provocar um erro nesta linha.
  temperaturaMedia = tapply (novoM$'temperaturaMedia', trunc(Idx), mean),
  umidadeMedia = tapply (novoM$'umidadeMedia', trunc(Idx), mean),
  pressaoMedia = tapply (novoM$'pressaoMedia', trunc(Idx), mean)
)


plot (1:dim(G)[1], G$temperaturaMedia, main="Temperatura média diária", xlab="dia", ylab=expression(paste("temperatura(", degree, "C)")));
axis(1, 1:dim(G)[1], G$DataHoraInicio) # https://stackoverflow.com/questions/5182238/replace-x-axis-with-own-values, https://lukemiller.org/index.php/2010/05/modifying-basic-plots-in-r/, https://stackoverflow.com/questions/51799118/writing-the-symbol-degrees-celsius-in-axis-titles-with-r-plotly/51799161


# esboço para leitura do arquivo resultante

# library(readxl)
# library(tidyverse)
# library(lubridate)

# nomeDoArquivoAProcessar <- "fabio-2021-01-24"

# M <- read_csv(paste(nomeDoArquivoAProcessar, "-processado.csv", sep=""))



