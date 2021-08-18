#include <DisplayRolavel.h>

DisplayRolavel tela(0x3c, 4, 15, 1000,10);

int operacaoPendente=0;

void IRAM_ATTR callback1(){
  if (operacaoPendente==0) operacaoPendente=1;
}

void IRAM_ATTR callback2(){
  if (operacaoPendente==0) operacaoPendente=2;
}

void setup() {
  Serial.begin(115200);
  Serial.println();
  tela.init(4,15, 1000, 10);
  tela.concatenaMensagem("É verdade que também na história do pensamento filosófico a regra de ouro é mencionada com regularidade impressionante, desde Santo Agostinho até o século XVIII." );
                   //     ^1       ^10       ^20       ^30       ^40        ^50       ^60       ^70       ^80       ^90       ^100      ^110      ^120      ^130      ^140      ^150
  operacaoPendente=0;
  touchAttachInterrupt(T8, callback1, 30);
  touchAttachInterrupt(T9, callback2, 30);
}

#if 1
void loop() {
  switch (operacaoPendente) {
    case 0: break;
    case 1:
#ifdef DEBUG_ROLAVEL
      Serial.println("Atendendo touch para anterior");      
#endif
      tela.mostraJanelaAnterior();
      delay(200); // atraso para não ter várias interrupções em um único toque.
      operacaoPendente=0;
      break;
    case 2:
#ifdef DEBUG_ROLAVEL
      Serial.println("Atendendo touch para posterior");      
#endif
      tela.mostraJanelaPosterior();
      delay(200); // atraso para não ter várias interrupções em um único toque.
      operacaoPendente=0;
      break;
      
  }
}
#endif

#if 0
int volta=1;

void loop() {
  delay(10000);
  if (volta==1) {
    Serial.println ("Vai para janela anterior");
    if (tela.mostraJanelaAnterior()<0) volta=0;
  } else {
    Serial.println ("Vai para janela posterior");
    if (tela.mostraJanelaPosterior()<0) volta=1;
  }
}
#endif


