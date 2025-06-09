i2c no ESP32

Canais de hardware: https://docs.micropython.org/en/latest/esp32/quickref.html#hardware-i2c-bus

Canais de software: https://docs.micropython.org/en/latest/esp32/quickref.html#software-i2c-bus

O que é bit banging

Curiosidade - (em algum momento) a taxa de transferência do i2c por hardware é/foi maior que a do i2c por software: https://forum.micropython.org/viewtopic.php?t=8443

Erros de interpretação:
  
![Foto mensagem de erro](./Captura%20de%20tela%20de%202024-10-11%2017-25-06.png)

A mensagem de obsolescência acima leva algumas pessoas (eu, inclusive) a perguntar se i2c por hardware tornou-se obsoleto (o que não faz sentido). A explicação que faz a mensagem fazer sentido está em https://forum.micropython.org/viewtopic.php?t=9940 . Para resumir: Em algum momento havia apenas `machine.I2C` e a configuração de i2c por hardware ou por software era feita selecionando um canal. No ESP32, canais 0 e 1 são i2c por harware e canal -1 i2c por software. Em alguma mudança de versão o uso do canal -1 tornou-se obsoleto pois foi incorporada a classe `softI2C`, o que dá ensejo à mensagem *Warning: I2C(-1, ...) is deprecated, use SoftI2C(...) instead*. A mensagem não quer dizer que `I2C` tornou-se obsoleto, mas que o uso do comando `I2C` **com argumento** `-1` tornou-se obsoleto.

informação adicional em:

- https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP#i2c
- https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP#multiprograma%C3%A7%C3%A3o-com-esp32
- https://github.com/FNakano/CFA/tree/master/projetos/I2C
- https://github.com/FNakano/CFA/tree/master/projetos/py-I2C
