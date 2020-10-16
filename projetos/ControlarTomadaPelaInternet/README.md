# Controlar tomada pela internet

## Introdução (parte já foi feita no plano de atividades ou na proposta)

### ~~Contextualização (o que se sabe) e Motivação (por que se quer)~~ feito na proposta

### Revisão Bibliográfica (informação que foi encontrada durante a execução do plano)

#### Conceitos e Terminologia (glossário)

### Organização do relatório

## Objetivos específicos (O geral foi feito no plano de atividades ou na proposta)

## Materiais e Métodos ( quais são os ingredientes e o que fazer com eles para chegar nos resultados)

Lista de materiais

| Nome | Quantidade | link para foto do componente, de fato, utilizado|
| --- | --- | --- |
| Wittyboard | 1 | [centro-esquerda da foto, conectado ao carregador](IMG_20201011_143947403.jpg) | 
| [Relé Shield](../../componentes/atuadores/rele/README.md) | 3 | [três módulos, abaixo das tomadas, com o relé azul](IMG_20201011_143947403.jpg) |
| Fonte 5V (carregador para celular, battery pack ou equivalente) | 1 | [sobre a tomada do alto](IMG_20201011_143947403.jpg) |
| tomada | 4 | [entre os fios verdes](IMG_20201011_143947403.jpg) |
| plugue | 1 | [já conectado ao cabo de par, parte inferior da foto](IMG_20201011_143947403.jpg) |
| chapadur para apoiar montagem | 1 | [chapa perfurada embaixo dos componentes](IMG_20201011_143947403.jpg) |
| cabo de par 1.0mm | 1 | [branco, enrolado, parte inferior da foto](IMG_20201011_143947403.jpg) |
| segmentos 2.5mm^2 | 1 | [verde, acima e abaixo das tomadas](IMG_20201011_143947403.jpg) |
| Conector Sindal | 1 | [alt text](IMG_20201011_143947403.jpg) |

![Foto dos materiais](IMG_20201011_143947403.jpg)

Preparação

- Instalar Arduino IDE;
    - Instalar pacote para placa ESP8266;
    - Instalar biblioteca Blynk;
        - Baixar e instalar o programa no ESP8266
- Instalar Blynk no celular;
    - Instalar usando o celular e acessando Play Store no Android ou App Store no iOS.
    - Criar o app no Blynk;
- Instalar `curl` 
- Instalar `Java`

## Resultados e indicadores de avaliação 
(resultados dos testes dos entregáveis)

O sistema entregue compreende, além do dispositivo, programas para desktop e para celular. A comunicação utiliza protocolo HTTP e é intermediada pelo servidor blink-cloud.

No desktop o controle do dispositivo é feito usando [curl](README.md#curl), ou [Java](README.md#Java-e-Reason). Clicar nos links para detalhes.

No celular foi instalado Blynk e criado o [app](README.md#app-Blynk)

O dispositivo é programado usando [Arduino IDE](README.md#Programa-Arduino). Circuito e construção são apresentados [abaixo](Circuito-e-montagem).

![Organização do sistema entregue](organizacao.png)

### Entregáveis previstos

- Circuito e montagem;
- Programa Arduino;
- app Blynk;
- curl;

#### Circuito e montagem

#### Programa Arduino

#### app Bynk

[vídeo com teste usando app Blynk no celular](https://youtu.be/cZgetUtyo48)

#### curl

[vídeo com teste usando curl no console do linux](https://youtu.be/jV4n5LRMwzM)


### Entregáveis não previstos (soluções para problemas colaterais)

- Witty Board - descrição e tutorial
- Blynk - descrição e tutorial
    - A entrada analógica do ESP8266, no Blynk, está mapeada no pino d17;
    - Blynk tem alguma questão com o uso da porta analógica padrão e a operação do celular;
- Java e Reason
- Melhorias no protocolo de prototipagem
    - montagem física;
    - tipos de interconexão;
- Melhorias no processo e ferramentas de documentação
    - Reprodução da tela do celular no navegador: <https://play.google.com/store/apps/details?id=info.dvkr.screenstream&hl=pt>

#### Java e Reason



## Discussão e Conclusão

O uso do Witty Board foi muito conveniente. Como ele tem LEDs e LDR, é possível testar acionamento, medição, e comunicação, de ponta a ponta, com o componente desconectado do restante do circuito.

A grande quantidade de entregáveis colaterais aumenta grandemente o valor do resultado.


## Referências

[proposta do projeto](./proposta.md)

[diário do projeto](./diario.md)

