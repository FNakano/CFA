## Desligado.py

O que faz quando o arquivo é importado: Acende todos os LEDs da matriz com vermelho de baixa intensidade.

Como importar o arquivo: `import desligado`

Modo de usar: Abrir o arquivo num editor de texto, copiar o texto, colar no REPL (o que executa os comandos). Se sobrar uma linha por executar, apertar ENTER.

## Desligado2.py

O que faz quando o arquivo é importado: cria a função `my_test()`.

Como importar o arquivo: `import desligado2`

### my_test()

Quando executada, acende todos os LEDs da matriz com vermelho de baixa intensidade.

Modo de usar:

```python
desligado2.my_test()
```

## Efeitos.py

O que faz quando o arquivo é importado: cria as funções `apaga()`, `sem_energia()`, `anima()`, `animan(n)`, `aleatorio()`.

Como importar o arquivo: `import Efeitos`

### apaga()

Apaga todos os LEDs da matriz.

```python
Efeitos.apaga()
```

### sem_energia()

Acende todos os LEDs da matriz com vermelho de baixa intensidade. Para quem assisitiu Ultraman, é o sinal de que ele ficou sem energia.

```python
Efeitos.sem_energia()
```

### anima()

Efeito animado com um LEDs acendendo azul em efeito de corrida dando uma volta.

```python
Efeitos.anima()
```

### animan(n)

Repete ´n´ vezes o efeito de anima.

```python
Efeitos.animan(20)
```

### aleatorio()

Acende cada LED da matriz com uma cor gerada aleatoriamente

```python
Efeitos.aleatorio()
```
