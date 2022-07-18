## Desligado.py

```python
import machine, neopixel
```

No micropython, importa os objetos e funções para comunicar com o controlador (como `Pin`)


```python
np=neopixel.NeoPixel(machine.Pin(12),9)
```

Cria (instancia) a representação da matriz de LEDs, que recebe dados enviados pelo pino 12 do microcontrolador e tem 9 LEDs. A instância é usada através do identificador `np`. Referência: https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html. `np` é um array de 9 elementos. Cada elemento é acessado por um índice numérico de zero a 8. Referência sobre arrays: https://www.w3schools.com/python/python_arrays.asp

```python
r=(16,0,0)
```

Cria uma t-upla que, quando passada como cor, representa vermelho de baixa intensidade. As intensidades vão de 0 a 255, os canais (de cor) são (R,G,B). Referência sobre t-uplas: https://www.w3schools.com/python/python_tuples.asp

```python
for i in range(9):
```

Define um loop que é repetido 9 vezes, com i valendo de 0 a 8. Referência sobre loops em Python: https://www.w3schools.com/python/python_for_loops.asp

```python
  np[i]=r
```

Define a cor do i-ésimo LED da matriz como vermelho de baixa intensidade. Primeiro as cores de todos os LEDs são definidas, depois, enviadas para a matriz todas de uma vez.

```python
np.write()
```

Envia as cores para a matriz.

## Desligado2.py

Listagem: 

```python
# Define uma função para ser executada.
# Baseado em https://forum.micropython.org/viewtopic.php?t=4192#p26506


import machine, neopixel

def my_test():
  np=neopixel.NeoPixel(machine.Pin(12),9)
  r=(16,0,0)
  for i in range(9):
    np[i]=r
  np.write()

# importa com import desligado2
# executa com desligado2.my_test()

```

`def mytest():` indica que o bloco de código que se segue é a especificação (definição) da função `my_test()`. Quando uma função é definida, seu conteúdo não é executado. Referência: https://www.w3schools.com/python/python_functions.asp

### my_test()

A explicação sobre o conteúdo de `my_test()` está em `desligado.py` portanto e explicação sobre o conteúdo está na referência de `desligado.py`.

## Efeitos.py


### apaga() e sem_energia()

As funções `apaga()`, `sem_energia()` seguem o mesmo modelo: define uma cor, aplica nos 9 LEDs e transmite para a matriz. A explicação é a mesma de `desligado.py`.

### aleatorio()

A função `aleatorio()` usa a função `getrandbits(5)` para gerar, aleatoriamente, um número. Referência: http://docs.micropython.org/en/latest/library/random.html. O número gerado tem 5 bits, consequentemente seu valor vai de 0 a 63. Desta forma, na linha `np[i]=(random.getrandbits(5), random.getrandbits(5), random.getrandbits(5))`, a cor do i-ésimo LED é ajustada para algum número entre 0 e 63 no canal vermelho, outro número no canal verde e outro número no canal azul.

### animan(n)

A função `animan(n)` contém um loop que executa `n` vezes a função `anima()`.

### anima()

A função `anima()` tem um loop dentro de outro loop (loops aninhados). A execução dessa função faz o loop externo executar o loop interno uma vez para cada ítem da lista [0, 1, 2, 5, 9, 8, 7, 6, 3]. O loop interno executa os comandos internos (representados por # comandos internos...) 9 vezes.

```python
def anima():
  #...
  for i in [0, 1, 2, 5, 9, 8, 7, 6, 3]: # para cada valor de i, executa o bloco a seguir
    for j in range(9): # para cada valor de j, executa o bloco a seguir
      # comandos internos...
# ...
```
 
O loop externo indica, na variável `i`, o LED da matriz que deve ser aceso. O loop interno ajusta as cores de todos os 9 LEDs da matriz, indicando o LED ajustado com a variável `j`. Se `j` e `i` forem iguais, o j-ésimo LED deve ser aceso, se `j` e `i` forem diferentes o j-ésimo LED deve ser apagado. É o que a sequência de comandos internos faz:

```python
      if i==j :
        # https://www.w3schools.com/python/python_conditions.asp
        np[j]=b
      else :
		np[j]=z
```

a variável `b` codifica a cor azul, a variável `z` codifica a cor preta (apagado).

Apenas para reforçar a idéia, a definição de `anima()` pode ser escrita, em Português:

```
Para cada LED da corrida :
  Acenda o LED do momento (e apague os outros) :
  Transmita as cores para a matriz
```

