#include "DisplayRolavel.h"

// #define DEBUG_ROLAVEL

DisplayRolavel::DisplayRolavel (int addr, int sda, int scl)
      :SSD1306Wire(addr, sda, scl)  // isto chama o construtor.
                                    // https://stackoverflow.com/questions/120876/what-are-the-rules-for-calling-the-base-class-constructor
    {}
    void DisplayRolavel::limpa () {
      buf = new String (F("<<ini>> "));  // marca de início de buffer
      iniJanela=0;
      iniLen=buf->length();
      fimJanela=iniLen-1;
    }
    void DisplayRolavel::init (int tamanhoBuf, int comprimentoDaRolagem) {
      //tela = new SSD1306Wire(0x3c, sda, scl); // mantido para não dar erros de sintaxe durante a refatoração
      pinMode(16, OUTPUT);
      digitalWrite(16, HIGH);
      // Initialising the UI will init the display too.
      SSD1306Wire::init();  // SSD1306:: faz a desambiguação https://stackoverflow.com/questions/357307/how-to-call-a-parent-class-function-from-derived-class-function

      SSD1306Wire::flipScreenVertically(); // chama a função da classe base especificada na chamada.
      SSD1306Wire::setFont(Lato_Regular_13);
      rola=true;  // rola para o fim da mensagem mais recente quando recebe nova mensagem
      maxBufSize=tamanhoBuf;
      rollLen=comprimentoDaRolagem;
      limpa();
    }
    void DisplayRolavel::setRola (bool r) {
      rola=r;
    }
    void DisplayRolavel::finish() {
      // delete tela;
      delete buf;
    }
    void DisplayRolavel::concatenaMensagem (const String &msg) {
      int comprimentoBuffer=buf->length();
      int comprimentoMsg=msg.length();
      if ((comprimentoBuffer+comprimentoMsg)>maxBufSize) {
        buf->remove (iniLen+1,comprimentoMsg);
      }
      buf->concat (msg);
      if (rola) {
        mostraMaisRecente();
      }
#ifdef DEBUG_ROLAVEL
        Serial.print("concatenaMensagem:");      
        Serial.println (*buf);
#endif
    }
    void DisplayRolavel::mostraMaisRecente() {
      fimJanela=buf->length()-1;
      iniJanela=fimJanela;
      int i=rollLen;  // rollLen é em palavras.
      while ((i>0)&&(iniJanela>0)) {
        if ((buf->charAt(iniJanela)<=' ') || (buf->charAt(iniJanela)=='-')) {
          i--;
        }
        iniJanela--;
      } // while(i)
      if (i==0) iniJanela++;  // apontava para o espaço, agora aponta para o primeiro caracter da primeira palavra
#ifdef DEBUG_ROLAVEL
      Serial.print("mostraMaisRecente:");      
      Serial.println (buf->substring(iniJanela, fimJanela+1));
#endif
      SSD1306Wire::clear();
      SSD1306Wire::drawStringMaxWidth(0,0,128,buf->substring(iniJanela, fimJanela+1)); // a definição de substring exclui o caracter apontado pelo fim, então preciso acrescentar 1. https://www.arduino.cc/reference/en/language/variables/data-types/string/functions/substring/
      SSD1306Wire::display();
    }
    int DisplayRolavel::mostraJanelaAnterior() {
      if (iniJanela>0) {
        fimJanela=iniJanela-1;
        iniJanela=fimJanela;
        int i=rollLen;  // rollLen é em palavras.
        while ((i>0)&&(iniJanela>0)) {
          if ((buf->charAt(iniJanela)<=' ') || (buf->charAt(iniJanela)=='-')) {
            i--;
          }
          iniJanela--;
        }
        if (i==0) iniJanela++;  // apontava para o espaço, agora aponta para o primeiro caracter da primeira palavra
#ifdef DEBUG_ROLAVEL
      Serial.print("mostraJanelaAnterior:");      
      Serial.println (buf->substring(iniJanela, fimJanela+1));
#endif
        SSD1306Wire::clear();
        SSD1306Wire::drawStringMaxWidth(0, 0, 128,buf->substring(iniJanela, fimJanela+1));
        SSD1306Wire::display();
        return 0; // tinha como retroceder
      } 
      return -1; // não tinha como retroceder, já está no início
    }
    int DisplayRolavel::mostraJanelaPosterior() {
      if (fimJanela<buf->length()-2) {
        //fimJanela=buf.length()-1;
        iniJanela=fimJanela+1;
        int i=rollLen;  // rollLen é em palavras.
        while ((i>0)&&(fimJanela<buf->length())) {
          if ((buf->charAt(fimJanela)<=' ') || (buf->charAt(fimJanela)=='-')) {
            i--;
          }
          fimJanela++;
        } // while(i)
        if (i==0) fimJanela--;  // apontava para o espaço, agora aponta para o primeiro caracter da primeira palavra
        SSD1306Wire::clear();
        SSD1306Wire::drawStringMaxWidth(0, 0, 128, buf->substring(iniJanela, fimJanela+1));
        SSD1306Wire::display();
        return 0; // tinha como avançar
      }
      return -1; // não tinha como avançar, já estava no final
    }
