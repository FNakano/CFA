## Objetivo

Ligar e desligar tomadas.

## Objetivos específicos

Apresentar um programa que se aproxime de Blynk e de WebThings (Mozilla Web of Things) usando MicroPython (e REPL ou WebREPL).

## Introdução 

[Blynk](https://blynk.io/)

[WebThings](https://webthings.io/)

[Mozilla Web of Things](https://hacks.mozilla.org/2019/04/introducing-mozilla-webthings/)

[Tomada](/projetos/ControlarTomadaPelaInternet)


## Resultados

### Testes executados

### Vestível

### Dispositivo

Apresentar diagrama ou tabela de ligações e foto. Caso seja idêntico a algum projeto anterior, citar o projeto anterior, que DEVE conter esta informação.

Fotos e vídeos

### Código usado

```python
ldr=machine.ADC(0)
print(ldr.read())
```


```python
pR=machine.Pin(15, machine.Pin.OUT)
pG=machine.Pin(12, machine.Pin.OUT)
pB=machine.Pin(13, machine.Pin.OUT)
pR.on()
pR.off()

```

## Discussão e Conclusão

-----------------

# Estrutura

## Objetivo

Um parágrafo, sem detalhes de implementação (que devem ser detalhados na introdução)

## Objetivos específicos

Vários ítens, indicando diferenciais (que devem ser detalhados na introdução)

## Introdução 

Referencial, produtos similares, diferenciais, ... em detalhes

## Materiais e métodos

### Listas de equipamentos e materiais

### Etapas do desenvolvimento

- Instalar IDE;
- Construir programa inicial;
- Construir vestível inicial;
- Refinar (ou usar SCRUM,...)
- ...

## Resultados

### Testes executados

Fotos, vídeos e instruções sobre como reproduzir os testes e usar o produto

### Vestível

Diagramas e fotos

### Dispositivo

Apresentar diagrama ou tabela de ligações e foto. Caso seja idêntico a algum projeto anterior, citar o projeto anterior, que DEVE conter esta informação.


### Programa

História sobre o desenvolvimento do programa, resumo de sua organização e interface (API);
Link para documentação para desenvolvedores que quiserem modificar ou acrescentar funcionalidades;
Link para documentação para desenvolvedores que quiserem usar o programa (API);

## Discussão e Conclusão

