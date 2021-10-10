Esta é uma história que dá uma idéia da integração entre SO, ferramentas de desenvolvimento e dispositivos físicos.

Semana passada, no dia primeiro de outubro de 2021, eu estava disposto a programar o ESP07, atualizar umas lâmpadas e tomadas usando webThings.

Quando tentei programar um wittyboard, recebi o erro:

```
esptool.py v3.0
Serial port /dev/ttyUSB0
Connecting........_____....._____....._____....._____....._____....._____....._____
Traceback (most recent call last):
  File "/home/fabio/.arduino15/packages/esp8266/hardware/esp8266/3.0.2/tools/upload.py", line 66, in <module>
    esptool.main(cmdline)
  File "/home/fabio/.arduino15/packages/esp8266/hardware/esp8266/3.0.2/tools/esptool/esptool.py", line 3552, in main
    esp.connect(args.before, args.connect_attempts)
  File "/home/fabio/.arduino15/packages/esp8266/hardware/esp8266/3.0.2/tools/esptool/esptool.py", line 529, in connect
    raise FatalError('Failed to connect to %s: %s' % (self.CHIP_NAME, last_error))
esptool.FatalError: Failed to connect to ESP8266: Timed out waiting for packet header
esptool.FatalError: Failed to connect to ESP8266: Timed out waiting for packet header

```

... e vamos lá tentar entender o que aconteceu...

Um erro parecido aconteceu faz uns anos, estava ligado ao chip CH340, que faz a interface entre USB e serial e é um clone do FTDI232... mas, vamos começar do começo:

Busca na documentação: https://arduino-esp8266.readthedocs.io/en/latest/faq/a01-espcomm_sync-failed.html, na Internet, ... informação não falta!

SÓ que há tanta informação disponível, gerada por pessoas que tiveram problemas parecidos, mas em outras épocas, com outras ferramentas que acabou ficando muito trabalhoso avaliar o que é pertinente ao meu caso...

Menção a projetos ruins, problemas com [estabilidade das fontes de alimentação](https://github.com/espressif/esptool/issues/586, https://github.com/esp8266/Arduino/issues/2428)
, ... acabei também fazendo meus próprios testes:

Testei com ESP8266 versão 2.5.0, 2.6.0; com CH340 no ESP, no arduino (clone do nano); com CP210X e ESP32; com CP210X e AtMega328p (arduino uno). Foi só com o ESP8266 com CH340 que não programa, nem dando reset manual. 

Acho que algum update do ubuntu quebrou o esptool. Se for isso, talvez saia um bugfix para a versão mais recente, mas dificilmente sairá para as mais antigas, imaginei, semana passada.

Há relatos, de dez meses atrás para cá, reportando problemas similares e as soluções dadas: contornar o auto-reset, que não está mais funcionando: https://stackoverflow.com/questions/65173101/esp8266-esptool-fatalerror-failed-to-connect-to-esp8266-timed-out-waiting-for.

No dia 08 de outubro, encontrei o que me pareceu a indicação certa. Poderia ser viés de confirmação, mas a descrição era bem parecida com o que passei, as suspeitas estavam bem alinhadas com as minhas e era um issue recente, de 06 de setembro: https://github.com/espressif/esptool/issues/656. Este apontava para outros, que fui seguindo. Parece que converge para este issue: https://github.com/espressif/esptool/issues/653. 

> "Timed out waiting for packet header" on kernel 5.13.10 (only for CH340 + ESP8266) [fixed in kernels 5.14 & 5.13.14] (ESPTOOL-291)

A conclusão foi:

> radimkarnis commented on 25 Aug

> Thank you everyone for your help with investigating this issue! The bug has been identified to be in the kernel. It should be already reverted and backported.
>
> There will be no action taken from the side of esptool. I will leave this issue open until someone confirms this.

O link para o bug tracker no bugzilla: https://bugzilla.kernel.org/show_bug.cgi?id=214131#c8.

>  Johan Hovold 2021-08-24 11:44:23 UTC
> 
> On Mon, Aug 23, 2021 at 09:14:49AM +0000, bugzilla-daemon@bugzilla.kernel.org wrote:
> > https://bugzilla.kernel.org/show_bug.cgi?id=214131
> > 
> > --- Comment #5 from Paul Größel (pb.g@gmx.de) ---
> > I agree, I couldn't find any enumerate related symptoms here:
> 
> I was able to reproduce the problem here. The device doesn't send a
> zero-length package in case the received data is a multiple of the
> endpoint size so that the bulk transfer doesn't complete (e.g. your
> flashing application may not receive replies).
>
> We need to revert the offending commit until we can figure out how to
> configure the device to send ZLPs.
>
> Thanks again for reporting this, and sorry about the breakage.
> 
> Johan

> Comment 8 Johan Hovold 2021-08-25 07:21:23 UTC

> For the record, I've applied the revert now and it should be backported
> to the stable trees shortly:
>
>	https://git.kernel.org/pub/scm/linux/kernel/git/johan/usb-serial.git/commit/?h=usb-linus&id=df7b16d1c00ecb3da3a30c999cdb39f273c99a2f



Parece que a atualização do kernel que quebrou o CH340 foi feita por volta do dia 20 de agosto e foi revertida uns dois dias depois, mas o kernel que Ubuntu distribui quebrou o CH340 em 01 de outubro e não foi atualizado até agora, dia 8 outubro. 

A consequencia para mim foi:

- ter o trabalho de resgatar uma versão anterior do kernel;
   - ainda bem que tinha alguma à mão;
   - mas em um raspi: um outro computador;
- instalar todo o conjunto de ferramentas;
- testar;

Vendo que funcionou, e que talvez fique assim por um tempo, tive que reorganizar o canto de trabalho.

Ao menos é uma história que dá uma idéia da integração entre SO, ferramentas de desenvolvimento e dispositivos físicos.


