# Motor de passo

![Montagem](photo1666275262.jpeg)

## Introdução

Como um motor de passo funciona: https://learn.adafruit.com/all-about-stepper-motors


Sobre o motor usado nesta montagem: https://create.arduino.cc/projecthub/debanshudas23/getting-started-with-stepper-motor-28byj-48-3de8c9

### Componentes

| aaa | bbb | ccc |
| --- | --- | --- |
| Arduino (Mega/UNO/Nano...) | --- | --- |
| Driver ULN2003 | geralmente comprado junto com o motor | --- |
| Motor de passo 28BYJ-48 | geralmente comprado junto com o driver | --- |
| Cabo USB para o Arduino | --- | --- |
| Jumpers | --- | --- |



### Ligações

| Arduino | Driver ULN2003 | Motor |
| --- | --- | --- |
| 2 | In1 | --- |
| 3 | In2 | --- |
| 4 | In3 | --- |
| 5 | In4 | --- |
| 5V | VDD | --- |
| GND | GND | --- |
| --- | Soquete do conector branco | Conector branco de 5 fios |

### Programa

```c
// https://create.arduino.cc/projecthub/debanshudas23/getting-started-with-stepper-motor-28byj-48-3de8c9
// Testado com arduino mega em 2022-10-20

#define A 2
#define B 3
#define C 4
#define D 5
 
#define NUMBER_OF_STEPS_PER_REV 512

void setup(){
	pinMode(A,OUTPUT);
	pinMode(B,OUTPUT);
	pinMode(C,OUTPUT);
	pinMode(D,OUTPUT);
}

void write(int a,int b,int c,int d){
	digitalWrite(A,a);
	digitalWrite(B,b);
	digitalWrite(C,c);
	digitalWrite(D,d);
}

void onestep(){
	write(1,0,0,0);
	delay(5);
	write(1,1,0,0);
	delay(5);
	write(0,1,0,0);
	delay(5);
	write(0,1,1,0);
	delay(5);
	write(0,0,1,0);
	delay(5);
	write(0,0,1,1);
	delay(5);
	write(0,0,0,1);
	delay(5);
	write(1,0,0,1);
	delay(5);
}

void loop(){
	int i;
	i=0;
	while(i<NUMBER_OF_STEPS_PER_REV){
		onestep();
		i++;
	}
}

```

### Comentários

O que, no programa, está codificado na função `onestep()` é uma sequência de 8 meio-passos. Num giro, essa sequência se repete. Acredito que seja por isso que o autor do código chamou a função de `onestep()`.
