<!--- 1. Título --->

# Implementação de Funcionalidades Recorrentes - Proposta

## Objetivo geral (O que fazer)

Construir dispositivos que implementam funcionalidades recorrentes nos (meus) projetos de sensores.

1. Data logger / servidor de arquivos;
2. Desenvolver algoritmo para correção da imprecisão do RTC interno do ESP32;

## Motivação (Por que fazer: Relevância, experiência, conhecimento acumulado, motivação pessoal,...)

Considerando convites que recebo para colaboração em projetos e meus interesses próprios:

- Registro de acerto e tempo de ação/reação em jogos;
- Registro de atividades diárias;
- Registro de medições meteorológicas;
- Actimetria;
- Registro de dados de experimentos de laboratório;

Todos estes projetos têm em comum o armazenamento de informação. Uma informação comum a todos é tempo ou intervalos de tempo.

Adicionalmente, um recurso importante e escasso em dispositivos é energia:

- Frequentemente dispositivos recebem energia através de baterias;
- Frequentemente é característica desejada de dispositivos que se mantenham funcionando por *longos* períodos (alguns dias a alguns anos);
- Frequentemente é conveniente que o dispositivo transmita dados por canal sem fio.
- Transmissão sem fio (por rádio) consome muita energia, mesmo para alcances da ordem de dezenas de metros;

**nota**: cada um desses ítens requer/merece melhor embasamento, mas não está no horizonte de atividades no momento.
**nota**: fiz algumas medidas de duração de bateria. Um ESP32 com bateria 18650 de 2200mAh ativo e com wifi durante o tempo em que permanece ligado, esgota a bateria em cerca de 12h. O mesmo para um ESP32 conectado a um battery pack através da porta USB. Um ESP32 TTGO-Display com display OLED, com bateria de 720mAh, display aceso o tempo todo, sem wifi, sem controle de taxa de atualização, esgota a bateria em cerca de 3h.

## Caso seja parte de uma sequência/cadeia/rede, quais relações com as outras atividades/elos são conhecidas.

Etapa anterior: que sensores são conectados;
Etapa posterior: tratamento e análise dos dados;

## Referências

Ainda não há.

