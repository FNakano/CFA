# Concatenando os exemplos de aiorepl e microdot
# 2025-08-18

# https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl#usage
import asyncio
import aiorepl

# https://microdot.readthedocs.io/en/latest/intro.html#a-simple-microdot-web-server
from microdot import Microdot

app = Microdot()
from microdot import Microdot, send_file
app = Microdot()


@app.route('/')
async def index(request):
    return send_file('static/index.html')


@app.route('/hello')
async def index(request):
    return 'Hello, world!'

# https://github.com/miguelgrinberg/microdot/blob/main/examples/static/static.py
@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)


async def main():
    print("Starting tasks...")

    # Start other program tasks.

    tm = asyncio.create_task(app.start_server()) # criar esta tarefa para executar microdot

    # Start the aiorepl task.
    repl = asyncio.create_task(aiorepl.task())

#    await asyncio.gather(t1, repl)  # mesmo sem ter gather tm o servidor microdot funciona
    await asyncio.gather( repl, tm) # colocar as tarefas no loop de "processos"


asyncio.run(main())  # executar o loop de "processos"
