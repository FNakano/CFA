"""
O que é: Arquivo de início de execução do aplicativo.
O que faz:
  Executa a inicialização de todos os módulos globais (ao aplicativo)
  Mostra informação sobre wifi no display OLED mas não a atualiza
O que espera-se que esteja neste arquivo:
  definição da co-rotina principal (main()) e sua execução
  (asyncio.run(main()))
"""

import config   # set this app global variables
import led      # setup built-in LEDs
import wifi     # setup wifi communication
import i2c      # setup i2c bus
import display  # setup display

display.message([config.myhostname, config.wifi_if.ifconfig()[0]])
led.off()

# going async...

import asyncio
import aiorepl
import httpserver

async def main():
    print("Starting tasks...")

    # Start other program tasks.

    tm = asyncio.create_task(config.app.start_server()) # criar esta tarefa para executar microdot

    # Start the aiorepl task.
    repl = asyncio.create_task(aiorepl.task())

#    await asyncio.gather(t1, repl)  # mesmo sem ter gather tm o servidor microdot funciona
    await asyncio.gather( repl, tm) # colocar as tarefas no loop de "processos"


asyncio.run(main())  # executar o loop de "processos"

