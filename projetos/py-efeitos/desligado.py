# parece que REPL e (Micro)Python (inicialmente) não foram feitos para executar arquivos .py repetidamente. Algo como exec('script.py') executaria o script e, se o mesmo comando fosse enviado, executaria novamente. Esta solução com exec não funciona e o recomendado é usar import script, que só é executado uma vez. A solução é criar uma função dentro de script.py, importar o arquivo e executar a função, o que codificarei em desligado2.py. Neste arquivo, o código é executado uma só vez usando import desligado.

import machine, neopixel

np=neopixel.NeoPixel(machine.Pin(12),9)
r=(16,0,0)
for i in range(9):
  np[i]=r
np.write()
