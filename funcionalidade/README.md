## Motivação

Às vezes deseja-se saber se certa funcionalidade está ou não disponível. 

Satisfazer esse desejo, às vezes, toma tempo, quando as ferramentas de busca que tem-se à disposição fazem algum tipo de busca textual, mesmo que melhorada. Essas buscas levam a resultados aproximados (do texto), que apontam para "um ponto mais distante" de uma eventual resposta satisfatória. 

Aconteceu hoje com mDNS em micropython e ESP32: desejo saber se existe e como habilito mDNS no ESP32 que executa micropython. Com Google, encontro resultados aproximados: o ESP executando o servidor mDNS em C e um desktop executando algum cliente em Python (que não é o que quero. Quero que o ESP execute o servidor mDNS em micropython).

Acredito (mas é uma crença mal fundamentada) que a estrutura da documentação, para que a busca automática dessa resposta seja melhor sucedida, requeira alguma mudança.

## Resultado

Na aplicação do mDNS em ESP32 e micropython, é uma funcionalidade que já funcionou, por volta de 2019, mas que *quebrou* logo em seguida. Suponho isso das referências: https://github.com/micropython/micropython/pull/4951, https://github.com/micropython/micropython/issues/4748, https://github.com/micropython/micropython/issues/4912.

Há soluções que iniciaram antes: https://github.com/cbrand/micropython-mdns/blob/main/examples/service_responder.py#L2, e que são mantidas: https://forum.micropython.org/viewtopic.php?t=3027, https://pypi.org/project/micropython-mdns/, mas não mostra um exemplo sendo executado. Tentei usar esta mas não funcionou.

Para ESP32 e ESP8266, em C, os exemplos da IDE do Arduino resolvem: https://techtutorialsx.com/2016/11/20/esp8266-webserver-resolving-an-address-with-mdns/, https://tttapa.github.io/ESP8266/Chap08%20-%20mDNS.html, https://techtutorialsx.com/2020/04/18/esp32-advertise-service-with-mdns/

Em outras placas baseadas em ESP32 existe a funcionalidade: https://docs.pycom.io/firmwareapi/pycom/network/mdns/


