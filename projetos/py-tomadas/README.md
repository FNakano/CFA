## Objetivo

Ligar e desligar tomadas.

## Objetivos específicos

Apresentar um programa que se aproxime de Blynk e de WebThings (Mozilla Web of Things) usando MicroPython (e REPL ou WebREPL).

## Introdução 

Automação residencial, ou, domótica, é cada vez mais presente.

Empresas provêm hospedagem de serviços, guias para construção e gerenciamento de dispositivos, como [Blynk](https://blynk.io/), [WebThings](https://webthings.io/), [Mozilla Web of Things](https://hacks.mozilla.org/2019/04/introducing-mozilla-webthings/).

Uma funcionalidade básica nas casas que agora estão sendo automatizadas são tomadas de energia elétrica. Automatizar seu funcionamento provavelmente é um dos primeiros passos para automatizar uma residência.

Um projeto de automatização de tomadas, feito pelos autores deste repositório e baseado em Blynk é apresentado em [Tomada](/projetos/ControlarTomadaPelaInternet). Neste projeto, a empresa Blynk tem acesso às mensagens, o que permite à empresa conhecer os hábitos dos clientes.

Outros sistemas, que mantém a comunicação dentro da casa que foi automatizada, foram propostos. Um deles é Mozilla Web of Things, que, em 2019, foi rebatizado WebThings e que foi parcialmente descontinuado. 

O ambiente de negócios está cada vez mais volátil, com empresas e produtos surgindo e desaparecendo em intervalos de um ou dois anos. 

Ambientes de programação estão cada vez mais complexos, com camadas de programas montadas umas sobre as outras, desempenhando tarefas cada vez mais sofisticadas. Quando algum programa é descontinuado, há um problema para os programadores das camadas superiores, que precisam procurar outros programas equivalentes e *migrar* seu programa para usar o programa substituito, frequentemente incorrendo em custos imprevistos (risco financeiro).

Do ponto de vista do ensino de tecnologias, não convém ensinar algo que em pouco tempo fique desatualizado, mesmo que os conceitos sobre os quais a tecnologia foi construída sejam mantidos. Logo, convém usar tecnologias amplamente usadas e mantidas. Python e ambientes suportados por navegadores (HTTP, Javascript) parecem ser suficientemente permanentes. 


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

Um parágrafo, sem  estender-se com explicações (que devem ser apresentadas na introdução)

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

