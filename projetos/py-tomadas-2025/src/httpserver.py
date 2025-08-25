"""
O que é:
  Arquivo de configuração e execução do servidor HTTP
O que faz:
  Define rotas e as co-rotinas que são escutadas para
  atendimento das requisições (de rotas)
  Cria o servidor HTTP na variável local app
O que espera-se que esteja neste arquivo:
  Todas as definições de rotas.
"""
import config
from microdot import Microdot, send_file

app = Microdot()
config.app=app

# default route
@app.route('/')
async def index(request):
  return send_file('static/index.html')

# plain text response
@app.route('/hello')
async def index(request):
  return f"Hello from {config.myhostname}.local"

# LEDs

def ledtowebresponse (value):
  if (value) : return 'on'
  else : return 'off'

@app.route('/red')
async def red(request):
  return ledtowebresponse(config.redled.value())

@app.route('/red/on')
async def redon(request):
  config.redled.on()
  return ledtowebresponse(config.redled.value())

@app.route('/red/off')
async def redoff(request):
  config.redled.off()
  return ledtowebresponse(config.redled.value())

@app.route('/green')
async def green(request):
  return ledtowebresponse(config.greenled.value())

@app.route('/green/on')
async def greenon(request):
  config.greenled.on()
  return ledtowebresponse(config.greenled.value())

@app.route('/green/off')
async def greenoff(request):
  config.greenled.off()
  return ledtowebresponse(config.greenled.value())

@app.route('/blue')
async def blue(request):
  return ledtowebresponse(config.blueled.value())

@app.route('/blue/on')
async def blueon(request):
  config.blueled.on()
  return ledtowebresponse(config.blueled.value())

@app.route('/blue/off')
async def blueoff(request):
  config.blueled.off()
  return ledtowebresponse(config.blueled.value())

import config
import display
@app.get('/message')
# GET request parameter
# http://device001.local:5000/message?text="ttt zzz"
# write message text in display
# this example "ttt zzz" is displayed with double
# quotes and space but results in non-fatal error "UnicodeError:"
async def message(request):
  txt=request.args.get('text', None)
  if txt is not None :
    display.message([txt])
  return config.messages

# Static files
# https://github.com/miguelgrinberg/microdot/blob/main/examples/static/static.py
@app.route('/static/<path:path>')
async def static(request, path):
  if '..' in path:
    # directory traversal is not allowed
    return 'Not found', 404
  return send_file('static/' + path)
