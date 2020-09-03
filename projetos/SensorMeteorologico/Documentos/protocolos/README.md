# Protocolos

Protocolo é o conjunto de especificações técnicas sobre como a comunicação deve ser feita.

Protocolos podem ser criados por fabricantes de componentes, por associações de fabricantes, por instituições normativas.

Protocolos têm nome, às vezes mais de um, no estilo nome comum e nome técnico. Usarei o nome comum que conheço.

A implementação de um protocolo pode ser em software ou em hardware.

Dispositivos podem ser construídos para comunicar-se em mais de um protocolo.

Protocolos e dispositivos são, na minha opinião, fracamente interdependentes. Conhecer o protocolo permite saber de antemão certos aspectos da interconexão entre os dispositivos que se comunicam usando esse protocolo, quais estados dos sinais são normais, quais são anormais. Não permite saber exatamente como o dispositivo se comunica.

No uso em prototipagem e projeto de dispositivo, esse conhecimento ajuda a localizar e resolver erros de montagem ou de projeto mais rápido e com menos sofrimento.

Neste documento pretendo ensinar a usar, inicialmente de forma não muito científica e centrada na placa de prototipagem, os protocolos de comunicação comumente usados nas plataformas.

## Serial

Tecnicamente, RS232, ou sua sucessora, RS484.

É usado por displays, leitores de impressão digital, 

Foi criado para comunicação entre computadores usando linha de telefonia analógica.
 
## One-wire

Este protocolo, que eu saiba, foi criado pela DALLAS.

É o protocolo dos sensores de umidade e temperatura DHT11 e DHT22, e dos sensores de temperatura DS18B20.

## I2C

A pronúncia recomendada nos documentos (em inglês) é "i square c". Traduzindo, "i ao quadrado c". Já ouvi e uso "i dois c". Vem de *Inter-Integrated Circuit*. Também já ouvi *two-wire*, que acho que era o nome usual antes de haver norma. A biblioteca Arduino chama-se *Wire*.

É usado por muitos acelerômetros (ex. MPU6050, MPU9250), magnetômetros, medidores de pressão atmosférica (BMP180, BMP280, BME280), sensores de gestos e cores, sensores de luminosidade, displays OLED (SSD1306), sensores de CO2 (CCS811), sensores de temperatura e umidade (HDC1080), relógios (DS1307, DS2231).

O protocolo define dois sinais bidirecionais para efetuar a comunicação, comumente designados SDA (Serial DAta) e SCL (Serial CLock). A conexão é completada com um nível de referência (Ground).

Caso o sensor receba energia da placa controladora, deve existir conexão (usualmente com rótulos VCC, 3v3 ou 5V) entre sensor e controlador. Esta conexão não é necessária ao protocolo, embora, sem energia, o sensor não funcionará e consequentemente não se comunicará.

Este protocolo permite conectar vários dispositivos em um barramento. Para isto, simplesmente conectar juntos todos os SDA, separados dos SDA, conectar juntos todos os SCL, separados dos anteriores, conectar juntos todos os GND. Este tipo de conexão é comumente chamada *barramento*. Como o protocolo é I2C, a designação completa é *barramento I2C*.

(o trecho a seguir necessita checagem)

Os sinais são bi-direcionais com saída em alta impedância. Isto quer dizer que fixado um dispositivo, este pode "ler" ou "escrever" no pino que corresponde ao sinal. Saída em alta impedância significa que escrever HIGH no pino equivale a desconectar o pino do circuito (em contraposição a conectar o pino internamente a VCC, o que geralmente é feito quando escreve-se HIGH em um pino de saída). Isto é feito para evitar que não ocorra "curto-circuito" caso dois dispositivos escrevam no mesmo sinal ao mesmo tempo, um escrevendo HIGH e outro escrevendo LOW.

Em circuitos cuja saída é em alta impedância, um resistor conectando o sinal ao VCC (por isso chamado *pull up*) é necessário. Um resistor por sinal, independente da quantidade de dispositivos compartilhando o sinal. Quando ele não é colocado externamente, algum dos dispositivos o conectou internamente. Sem este resistor o sinal não é transmitido corretamente e a conexão não acontece.

O protocolo define *servidor* como o dispositivo que "solicita o controle do barramento". A solicitação de controle é feita escrevendo LOW em SDA e depois LOW em SCL. Depois SCL e SDA são chaveados (transitam de HIGH para LOW para HIGH, ...) de maneira a transmitir informação. Em geral esta informação é uma solicitação de informação para algum *cliente* (sensor), e contém, entre outras coisas o *endereço* do sensor (que, na minha opinião, deveria ser chamado identificador do sensor). Após essa transmissão, o sensor responde. Nessa resposta, o *servidor* escreve em SCL e lê em SDA, e o *cliente* lê SCL e escreve em SDA.

(fim do trecho que necessita checagem)

O protocolo permite 127 endereços. Falando grosseiramente, 127 dispositivos diferentes podem ser conectados ao barramento.

Os endereços são concedidos aos fabricantes de dispositivos pela instituição normativa. Os fabricantes fabricam os sensores com o endereço (completo ou em parte) gravado permanentemente (por isso eu chamaria de identificador do sensor). Consequentemente, todos os BMP280 usam o endereço 0x76, todos os SSD1306 usam o endereço 0x3C, todos os DS1307 usam o endereço 0x68.

Este esquema de endereços é muito restritivo. Por exemplo não permite conectar dois SSD1306 ao mesmo barramento. Embora haja uma instituição regulando as atribuições de endereço, já há coincidências: os relógios da Dallas usam o endereço 0x68 e os acelerômetros da InvSense (ex. MPU9250) também. O que permite o uso dos dois dispositivos no mesmo barramento simultaneamente é a possibilidade de trocar o endereço do acelerômetro para 0x69 por hardware (detalhes na descrição do MPU9250).

O controlador do Arduino UNO e do Arduino Nano (ATMega328) contém hardware específico para I2C. Este hardware usa os pinos A4 e A5 como SDA e SCL, respectivamente. Com isso em vista, a biblioteca *Wire* para Arduino UNO e Nano usa, implicitamente, esses pinos.

Os ESP também contém hardware específico para I2C e, em princípio, permitem conectar qualquer sinal interno a qualquer pino externo. Desta forma qualquer pino do ESP pode ser SDA ou SCL. Por outro lado, há pinos usados internamente, que recebem usos específicos e às vezes não documentados. Isto torna alguns pinos não usáveis para determinados fins. Por exemplo, GPIO16 é usado para retorno do estado de *deep sleep*, alguns pinos têm/necessitam resistores *pull down*. Estes não são boas escolhas para SDA e SCL.

Voltando ao esquema de endereços, por ser muito restritivo, permite localizar todos os dispositivos conectados a um barramento, mesmo que isto não tenha sido previsto no protocolo. Para Arduino: [I2CScanner]() e para ESP: [I2CPinScanner]().

Estes programas permitem saber se os dispositivos estão conectados, quais dispositivos estão conectados, quais pinos servem para SDA e SCL - são ótimas ferramentas para depuração.



## SPI

Pronuncio "esse pê i".

É usado por cartões SD, displays (o LCD do Nokia 3310)



