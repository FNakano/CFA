# Motores

Existe uma variedade de motores. Aqui serão apresentados os motores elétricos mais comuns. Servomotores também serão abordados.

- Motor DC
    - Motor DC com escova
    - Motor DC sem escova
- Motor de passo
    - unipolar
    - bipolar
- Servomotor

## Motor DC

**nota**: aconselha-se não ligar motor à porta USB do computador. A maioria dos motores necessita mais corrente que os 500mA máximos que a porta USB, se for boa, é capaz de fornecer. Acrescente-se que motores, em geral, produzem ruído de chaveamento, Este pode 'sujar' a linha de energia interna ao computador e provocar mau funcionamento.

Motores a corrente contínua (CC, em inglês, direct current - DC). Apenas a título de contraposição, sua construção é um pouco diferente dos motores AC (alternate currrent) usados em liquidificadores e batedeira, e, também, é diferente do motor trifásico.

Em geral motores requerem mais corrente do que uma saída do microcontrolador fornece. Desta forma, ligar o motor diretamente à saída do microcontrolador (e programar a saída de acordo com esse uso) provavelmente não fará o eixo do motor mover-se e, talvez, danifique a saída do microcontrolador (em geral isso não acontece pois as saídas são protegidas contra sobrecorrente, que é o que acontece quando o motor é ligado diretamente à ela).

Um *driver* de motor é o componente que fornece/controla corrente suficiente para fazer o eixo mover-se. O *driver* também pode gerar outros sinais, ou gerá-los na sequência certa para mover o eixo do motor.

O componente geralmente vendido como motor pode conter na mesma caixa, além do motor propriamente dito, uma caixa de redução (engrenagens - para diminuir a velocidade e aumentar a força), e o *driver*. É o caso do servomotor SG90.

Quando o motor tem acoplada uma caixa de redução, convém não empurrar ou puxar o eixo da caixa de redução (que é o eixo externo), com *muita* força pois pode entortar as engrenagens da caixa de redução, fazendo que ela deixe de funcionar. Aqui, a pressão que fazemos para fechar a tampa da lata de tinta para parede já é *muita* força.

### Motor DC com escova

Algumas fontes o chamam *motor de giro*. 

Esses motores têm dois fios através dos quais recebem energia, geralmente de uma bateria ou do *driver*. Recebendo energia, o eixo gira.

O 'motor' que equipa a maioria dos kits de carrinho no mercado, por exemplo: <https://www.eletrogate.com/kit-chassi-2wd-robo-para-arduino?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gclid=Cj0KCQjwtZH7BRDzARIsAGjbK2bnR4AZPYPhr-Fc32DdXLvHS9SJ9fn_qB1b4ve26tP0vn5ofOHQhvEaAvX4EALw_wcB>, além do motor propriamente dito, contém uma caixa de redução.

O *driver* deste motor pode ser um (ou mais) relés, ou uma ponte H, como o L298 e o L293. O controle com relés, geralmente, não permite controlar a velocidade de rotação.

### Motor DC sem escova

Esses motores são usados em disk drivers de CDs, em HDs e em alguns drones (quadri/hexa-cópteros). Ou para girar as mídias ou para girar as hélices. Os motores que movem as cabeças de leitura/gravação de disk drivers costumam ser motores de passo.

São motores que atingem alta rotação, têm alta taxa de conversão (de potência elétrica para potência mecânica) e são leves para a potência que desenvolvem.

O princípio de funcionamento é similar ao de motores trifásicos.

Os *drivers* desses motores, em drones, são chamados Electronic Speed Control (ESC). Eles condicionam o sinal das bobinas para o rotor girar e controlam a velocidade de rotação. O protocolo de comunicação com o controlador é o mesmo do servo SG90 (ao menos no ESC que estudei).

## Motor de passo

Motores de passo são construídos usando vários enrolamentos (bobinas) que podem ser energizadas independentemente. Isto permite controlar o ângulo de rotação do eixo com grande precisão e repetibilidade.

### unipolar
ex. 28byj-48 - o driver mais comum é o UNC2003.

Contém quatro bobinas. Um terminal de cada bobina é ligado em comum (fig). Externamente são 5 fios.

### bipolar
### Servomotor

ex. Tower Pro SG90

<https://www.curtocircuito.com.br/servo-motor-sg90.html>

