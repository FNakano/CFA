#ifndef DisplayRolavel_H
#define  DisplayRolavel_H  // constante que, junto com o ifndef, serve para evitar que este header seja incluído mais de uma vez

#include <Wire.h>               // Only needed for Arduino 1.6.5 and earlier
#include "SSD1306Wire.h"        // legacy: #include "SSD1306.h"

#include "Lato13.h"

class DisplayRolavel : public SSD1306Wire { // só detectei a falta do public quando fui testar o código de OTA.
  private:
  /** 
   * buf é o buffer de palavras. É a memória de todas as mensagens que já foram mostradas. Seu tamanho máximo é maxBufSize. Se a soma do comprimento das mensagens tornar-se maior que maxBufSize, então partes das mensagens mais antigas são substituídas pelas mensagens mais recentes, num esquema de fila: FIFO.
   * Janela é a parte do buffer que é mostrada no display. iniJanela é o índice do primeiro caracter que está na janela, fimJanela é o índice do último caracter que está na janela.
   * A Janela pode avançar ou retroceder no buffer. A medida do avanço/retrocesso é de rollLen palavras. 
   * O início do buffer é indicado ao usuário com uma mensagem/palavra definida internamente cujo comprimento é iniLen.
   * O flag rola indica se a janela deve ou não ser rolada para a mensagem mais recente quando uma nova mensagem for recebida. 
   */
    
    String *buf;
    int iniJanela;
    int fimJanela;
    int maxBufSize;
    int rollLen;
    int iniLen;
    bool rola;
    
  public:
  /**
   * O modelo de ESP32 usado e o TTGO-T com display OLED SSD 1306 de 128x64 pixels. A biblioteca gráfica usada como base é a ThingPulse (https://github.com/ThingPulse/esp8266-oled-ssd1306). Com essa biblioteca é possível construir fontes usando o site http://oleddisplay.squix.ch/#/home. 
   * A fonte Lato13 foi construída usando esse site e foi escolhida por ter altura de 16 pixels, o que, acredito, maximiza o uso do display.
   * Dos tipos de comunicação com o display disponíveis na biblioteca gráfica, usou-se I2C com a biblioteca Wire.
   * O construtor desta classe apenas chama o construtor da biblioteca gráfica. 
   */
    DisplayRolavel (int addr, int sda, int scl);
    /** método que limpa o buffer e inicializa as variáveis de controle */
    void limpa ();
    /** método que cria o buffer, liga o display (pino 16 do ESP32 = HIGH), e limpa o buffer. 
     * Buffer é a memória de todas as mensagens que já foram mostradas. Seu comprimento máximo é tamanhoBuf. Se a soma do comprimento das mensagens tornar-se maior que tamanhoBuf, então partes das mensagens mais antigas são substituídas pelas mensagens mais recentes, num esquema de fila: FIFO.
     * O texto mostrado no display pode avançar ou retroceder no buffer. A medida do avanço/retrocesso é de comprimentoDaRolagem palavras.
     */ 
    void init (int tamanhoBuf, int comprimentoDaRolagem);
    /** se true, indica que a janela deve ser rolada para a mensagem mais recente quando uma nova mensagem for recebida. se false, a janela não será rolada quando receber mensagem nova.
     */
    void setRola (bool r);
    /** libera memória - tem que ser usado antes de um novo init. Não é necessário se init for usado uma só vez durante a execução do programa.
    */
    void finish();
    /** concatena nova mensagem no buffer.
     */
    void concatenaMensagem (const String &msg);
    /** mostra mensagem mais recente (vai para o fim do buffer) */
    void mostraMaisRecente();
    /** rola a janela comprimentoDaRolagem palavras para o começo do buffer. Retorna 0 em caso de sucesso (conseguiu retroceder ao menos uma palavra) ou -1 caso não tenha conseguido retroceder (está no início do buffer).
     */
    int mostraJanelaAnterior();
    /** rola a janela comprimentoDaRolagem palavras para o começo do buffer. Retorna 0 em caso de sucesso (conseguiu retroceder ao menos uma palavra) ou -1 caso não tenha conseguido retroceder (está no início do buffer).
     */
    int mostraJanelaPosterior();
};

#endif

