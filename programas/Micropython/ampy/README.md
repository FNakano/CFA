# ampy

O **ampy** é uma ferramenta simples que permite enviar arquivos e scripts para a placa que utiliza o MicroPython, além de manipular arquivos de código utilizando a conexão serial. 

## :inbox_tray: Instalação

Para instalar a ferramenta, você precisa ter Python 2.7.x or 3.x instalado. Basta dar o seguinte comando no terminal:

`pip install adafruit-ampy`

ou

`pip3 install --user adafruit-ampy`

## :keyboard: Comandos

Os comandos são no formato `ampy [Opções] COMANDO [Argumentos]`

### Opções

- --port
Substitua "PORTA" pelo nome da porta serial conectada na placa 
`-p PORTA` ou `--port PORTA`

- --help
Manual de ajuda do comando
`--help` 

### Funções

- get
Devolve um dos arquivos que está na placa
`ampy -p PORTA get ARQUIVO`

- ls
Lista os conteúdos que estão na placa ou em seus diretórios
`ampy -p PORTA ls`

- put
Envia um arquivo que está em seu computador para a placa
`ampy -p PORTA put ARQUIVO`

- rm
Remove um arquivo que está na placa
`ampy -p PORTA rm ARQUIVO`

- run
Roda um script e printa a saída
`ampy -p PORTA run ARQUIVO`

Substitua PORTA pela porta serial utilizada para comunicação com a placa e ARQUIVO pelo arquivo correspondente.

## :desktop_computer: Uso

1. Conecte sua placa ao computador e encontre a saída serial na qual sua placa está conectada (geralmente, /dev/ttyUSB0)
2. Dê permissão para que todos os usuários leiam e escrevam a porta.
`sudo chmod 666 /dev/ttyUSB0`
3. Rode o comando escolhido.
Exemplo: `ampy -p /dev/ttyUSB0 put boot.py`

***Observação:*** às vezes, o comando "trava". Caso aconteça, retire o cabo e conecte novamente à placa, repetindo todos os passos de uso.

## :card_index_dividers: Referências bibliográfias

- **adafruit-ampy 1.1.0**. Disponível em <https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy>
- **Install ampy.** Disponível em <https://pypi.org/project/adafruit-ampy/>

