"""
O que é:
  Arquivo de definição de variáveis globais
O que faz:
  Cria variáveis globais (ao aplicativo) Algumas podem
  ser configuradas pelo usuário, outras são internas ao
  programa e são apropriadamente inicializadas durante a
  execução do programa.
O que espera-se que esteja neste arquivo:
  Definição das variáveis globais ao aplicativo.
"""

# User configured global variables (users may modify)
wifi_id = 'lab8'               # nome da rede
wifi_password = 'lab8arduino'  # senha da rede
myhostname = 'device001'       # nome do dispositivo
disp_width = 128               # largura do display OLED
disp_height = 64               # altura do display

# Program internal global variables (users should not modify)
disp=None       # handle for the display
i2c=None        # handle for I2C
redled=None     # handle for a red led
blueled=None    # handle for a blue led
greenled=None   # handle for a green led
wifi_if=None    # handle for the wifi interface
app=None        # handle for Microdot application (web server)
messages=None   # list of messages currently displayed