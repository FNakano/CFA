#
# MicroPython SH1106 OLED driver, I2C and SPI interfaces
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Radomir Dopieralski (@deshipu),
#               2017-2021 Robert Hammelrath (@robert-hh)
#               2021 Tim Weber (@scy)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Sample code sections for ESP8266 pin assignments
# ------------ SPI ------------------
# Pin Map SPI
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D7 - GPIO 13  - Din / MOSI fixed
#   - D5 - GPIO 14  - Clk / Sck fixed
#   - D8 - GPIO 4   - CS (optional, if the only connected device)
#   - D2 - GPIO 5   - D/C
#   - D1 - GPIO 2   - Res
#
# for CS, D/C and Res other ports may be chosen.
#
# from machine import Pin, SPI
# import sh1106

# spi = SPI(1, baudrate=1000000)
# display = sh1106.SH1106_SPI(128, 64, spi, Pin(5), Pin(2), Pin(4))
# display.sleep(False)
# display.fill(0)
# display.text('Testing 1', 0, 0, 1)
# display.show()
#
# --------------- I2C ------------------
#
# Pin Map I2C
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D2 - GPIO 5   - SCK / SCL
#   - D1 - GPIO 4   - DIN / SDA
#   - D0 - GPIO 16  - Res
#   - G  - xxxxxx     CS
#   - G  - xxxxxx     D/C
#
# Pin's for I2C can be set almost arbitrary
#
# from machine import Pin, I2C
# import sh1106
#
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
# display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
# display.sleep(False)
# display.fill(0)
# display.text('Testing 1', 0, 0, 1)
# display.show()

from micropython import const
import utime as time
import framebuf


# a few register definitions # sh1106_datasheet.pdf Commands section for details
_SET_CONTRAST        = const(0x81) # 5.Set Contrast Control Register (Double Bytes Command) - Contrast control Mode Set (81H)
_SET_NORM_INV        = const(0xa6) # 8.Set Normal/Reverse Display (A6H - A7H)
_SET_DISP            = const(0xae) # 11.Display OFF/ON (AEH - AFH)
_SET_SCAN_DIR        = const(0xc0) # 13.Set Common Output Scan Direction (C0H - C8H)
_SET_SEG_REMAP       = const(0xa0) # 6.Set Segment Re-map (A0H - A1H)
_LOW_COLUMN_ADDRESS  = const(0x00) # 1.Set Lower Column Address (00H - 0FH)
_HIGH_COLUMN_ADDRESS = const(0x10) # 2.Set Higher Column Address (10H - 1FH)
_SET_PAGE_ADDRESS    = const(0xB0) # 12. Set Page Address (B0H - B7H)


class SH1106(framebuf.FrameBuffer):

    def __init__(self, width, height, external_vcc, rotate=0):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.flip_en = rotate == 180 or rotate == 270
        self.rotate90 = rotate == 90 or rotate == 270
        self.pages = self.height // 8
        self.bufsize = self.pages * self.width
        self.renderbuf = bytearray(self.bufsize)
        self.pages_to_update = 0
        self.delay = 0

        if self.rotate90:
            self.displaybuf = bytearray(self.bufsize)
            # HMSB is required to keep the bit order in the render buffer
            # compatible with byte-for-byte remapping to the display buffer,
            # which is in VLSB. Else we'd have to copy bit-by-bit!
            super().__init__(self.renderbuf, self.height, self.width,
                             framebuf.MONO_HMSB)
        else:
            self.displaybuf = self.renderbuf
            super().__init__(self.renderbuf, self.width, self.height,
                             framebuf.MONO_VLSB)

        # flip() was called rotate() once, provide backwards compatibility.
        self.rotate = self.flip
        self.init_display()

    # abstractmethod
    def write_cmd(self, *args, **kwargs): 
        raise NotImplementedError

    # abstractmethod
    def write_data(self,  *args, **kwargs):
        raise NotImplementedError

    def init_display(self):
        self.reset()
        self.fill(0)
        self.show()
        self.poweron()
        # rotate90 requires a call to flip() for setting up.
        self.flip(self.flip_en)

    def poweroff(self):
        '''3 This function turns the display off. It sends bytearray(b'\x80\xae') to the display.
   \xae translates to binary 10101110. On SH1106 datasheet command table (p.31).
   Command 11. DisplayOFF/ON has the least significant 8 bits equal to \xae. Still did not
   understand bits A0,RD,WR=0,1,0. Where these bits are controlled in i2c commands??
   (note: issuing self.poweroff() disconnects ESP32 from the PC USB. It might be a power surge)
   GOT IT... A0, RD, WR are (among others) signals in the system bus (datasheet, p.4)
   SH1106 chip interfaces communication busses to the (actual) OLED display (LED, glass, contacts)
   SH1106 chip implements protocols compatible with 6800, 8080 processors, SPI and I2C
   Each of these protocols uses a number of connections (wires, pads). Particularly, connections
   IM0, IM1 and IM2 signals to SH1106 chip which protocol to use. if IM0=0, IM1=1, IM2=0
   protocol is i2c.
   While using i2c, some signals {are/are not} used. For example, D7-D2 are not used and are
   high-impedance pins (signed as Hz. Hi-Z might be more informative). Usually, Hi-Z pins are
   input or bidirecional (I/O) pins. These signals may interfere in chip function SO Note 1
   recommends to tie them to either VDD1 or VSS.
   ALSO while using i2c, RD and WR are pulled High or pulled Low (both soldered) so these signals
   can not be changed (TBC). As a consequence, commands 22.Write Display Data, 23.Read Status,
   24.Read Display Data SHOULD NOT BE AVAILABLE IN i2c. (quite strange).
   Unavailability of these commands is patched(?) by Co and D/C behavior: "After the last
   control byte, depending on the D/C bit setting, either a series of display data bytes
   or command data bytes may follow. If the D/C bit was set to 1, these display bytes are
   stored in the display RAM at the address specified by the data pointer. The data pointer
   is automatically updated and the data is directed to the intended sh1106 device. If the D/C
   bit of the last control byte was set to 0, these command bytes will be decoded and the setting
   of the device will be changed according to the received commands."
   My doubt now is: in the 0-th byte of the byte array only \x80 and \x40 values are used.
   What about the other 6-bit? Aren't they used?
        '''
        self.write_cmd(_SET_DISP | 0x00)

    def poweron(self):
        '''3 This function turns
        '''
        self.write_cmd(_SET_DISP | 0x01)
        if self.delay:
            time.sleep_ms(self.delay)

    def flip(self, flag=None, update=True):
        if flag is None:
            flag = not self.flip_en
        mir_v = flag ^ self.rotate90
        mir_h = flag
        self.write_cmd(_SET_SEG_REMAP | (0x01 if mir_v else 0x00))
        self.write_cmd(_SET_SCAN_DIR | (0x08 if mir_h else 0x00))
        self.flip_en = flag
        if update:
            self.show(True) # full update

    def sleep(self, value):
        self.write_cmd(_SET_DISP | (not value))

    def contrast(self, contrast):
        ''' (The code for the lowercase letter "d" is 100 in decimal - there is a problem with
micropython's print function applied to byte arrays...)
>>> config.disp.contrast(100)
bytearray(b'\x80\x81')
bytearray(b'\x80d')

Set contrast is a sort of two-byte command. One byte is the command, its code is \x81 the
next byte is the contrast value - an intensity from 0 to 255. These bytes are sent as two
separate commands. Some notation should be added: command as in micropython documentation of
SH1106, command as in SH1106 datasheet or control bytes as in SH1106 datasheet??
Also, can the contrast value be sent along with the set contrast opcode?? (My test failed.
answer is 'probably no') 
        '''
        if True : # original code
          self.write_cmd(_SET_CONTRAST) # \80, \81
          self.write_cmd(contrast)      # \80, contrast
        else :
          ''' this caused OSError: [Errno 19] ENODEV
probably the display did not acknowledged the i2c message '''
          temp=bytearray(3)
          temp[0] = 0x80  # Co=1, D/C#=0
          temp[1] = _SET_CONTRAST
          temp[2] = contrast
          self.i2c.writeto(self.addr, temp)
        print(temp)

    def invert(self, invert):
        self.write_cmd(_SET_NORM_INV | (invert & 1))

    def show(self, full_update = False):
        # self.* lookups in loops take significant time (~4fps).
        (w, p, db, rb) = (self.width, self.pages,
                          self.displaybuf, self.renderbuf)
        if self.rotate90:
            for i in range(self.bufsize):
                db[w * (i % p) + (i // p)] = rb[i]
        if full_update:
            pages_to_update = (1 << self.pages) - 1
        else:
            pages_to_update = self.pages_to_update
        #print("Updating pages: {:08b}".format(pages_to_update))
        for page in range(self.pages):
            if (pages_to_update & (1 << page)):
                # pages_to_update é um campo de bits. Cada bit corresponde a uma página
                # caso a página tenha sido modificada o bit correspondente é setado.
                # a operação pages_to_update & (1 << page) verifica se o page-ésimo bit
                # está setado, se sim, executa os comandos abaixo, senão, os salta.
                self.write_cmd(_SET_PAGE_ADDRESS | page)
                self.write_cmd(_LOW_COLUMN_ADDRESS | 2) # este 2 hardcoded pode ser relevante
                # segundo o datasheet do sh1106, ele consegue controlar displays de até 132 x 64
                # pixels (colunas x linhas)
                # um display ("propriamente" dito) é um conjunto de pontos luminosos em que cada
                # ponto pode ser controlado individualmente (acender, apagar, mudar de cor, ...)
                # displays que podem ser controlados pelo SH1106 são monocromáticos (então não
                # é possível mudar a cor). Nesses displays e no SH1106 também não é possível
                # controlar a intensidade (contraste) de um particular pixel, embora seja possível
                # controlar a intensidade de todos os pixels (coletivamente), então os pixels
                # acesos no display podem ficar mais intensos (coletivamente).
                # A organização dos pixels no display é o de uma matriz retangular (ié, fisicamente,
                # cada pixel é colocado/construído na matriz retangular. Mais que isso, para selecionar
                # um particular pixel usa-se um par de sinais. No vocabulário usado no datasheet, os
                # sinais chamam-se Common (COM) e Segment (SEG) e mapeiam um para um (biunivocamente)
                # nos pinos do display e nos pinos do SH1106. Como o SH1106 consegue controlar displays
                # de até 132x64, é de se esperar que haja 132 pinos de um tipo e 64 pinos de outro.
                # No caso, verifica-se no datasheet em Pad Configuration que há 132 SEG e
                # 64 COM
                # Até onde sei, os displays OLED atualmente disponíveis no mercado de dimensões
                # em pixels mais próximas de 132x64 são 128x64, de maneira que, suponho, quatro
                # SEG do SH1106 ficam desconectados do display OLED. Ainda nas suposições,
                # é mais provável que sejam os das extremidades e sejam contíguos (numa matriz
                # é pouco provável que a sequencia dos pinos seja diferente da sequencia das
                # linhas ou das colunas)
                # iniciar o endereço de coluna em 2 indica que dois SEG do SH1106 não foram
                # usados e, fazendo as contas, outros dois SEG na outra ponta não foram usa-
                # dos também.
                # IMPORTANTE: displays de tamanho diferente, como 128x32, 70x40 têm outra
                # quantidade de pinos SEG e COM. Em princípio, não há como saber quais
                # pinos são usados. Até agora, não há nada que indique que
                # esses diferentes tamanhos foram considerados. Desta forma, usar displays
                # de outros tamanhos pode não gerar os resultados esperados. Ainda na
                # inspeção do código, o framebuffer é alocado com o tamanho "certo" mas isso
                # não garante que os resultados esperados sejam obtidos.
                # Vou interromper meu estudo aqui pois tenho evidências que indicam que
                # a placa que me interessa usa SSD1306. Estudar SH1106 foi esclarecedor
                # pois tem menos parâmetros que o SSD1306.
                self.write_cmd(_HIGH_COLUMN_ADDRESS | 0)
                self.write_data(db[(w*page):(w*page+w)])
                # segundo o datasheet, cada página tem 8 linhas de pixels, o índice da
                # página não é incrementado automaticamente a cada escrita de dados,
                # o índice de colunas é incrementado a cada escrita de dados. Isto explica
                # que, neste ponto do programa, o loop itere pelas páginas (e não pelas
                # linhas ou pelas colunas)
        self.pages_to_update = 0

    def pixel(self, x, y, color=None):
        if color is None:
            return super().pixel(x, y)
        else:
            super().pixel(x, y , color)
            page = y // 8
            self.pages_to_update |= 1 << page

    def text(self, text, x, y, color=1):
        super().text(text, x, y, color)
        self.register_updates(y, y+7)

    def line(self, x0, y0, x1, y1, color):
        super().line(x0, y0, x1, y1, color)
        self.register_updates(y0, y1)

    def hline(self, x, y, w, color):
        '''
>>> config.disp.hline(0,0,128,1)
>>> config.disp.show()
bytearray(b'\x80\xb0')
bytearray(b'\x80\x02')
bytearray(b'\x80\x10')
bytearray(b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00')
        '''
        super().hline(x, y, w, color)
        self.register_updates(y)

    def vline(self, x, y, h, color):
        super().vline(x, y, h, color)
        self.register_updates(y, y+h-1)

    def fill(self, color):
        super().fill(color)
        self.pages_to_update = (1 << self.pages) - 1

    def blit(self, fbuf, x, y, key=-1, palette=None):
        super().blit(fbuf, x, y, key, palette)
        self.register_updates(y, y+self.height)

    def scroll(self, x, y):
        # my understanding is that scroll() does a full screen change
        super().scroll(x, y)
        self.pages_to_update =  (1 << self.pages) - 1

    def fill_rect(self, x, y, w, h, color):
        super().fill_rect(x, y, w, h, color)
        self.register_updates(y, y+h-1)

    def rect(self, x, y, w, h, color):
        super().rect(x, y, w, h, color)
        self.register_updates(y, y+h-1)

    def ellipse(self, x, y, xr, yr, color):
        super().ellipse(x, y, xr, yr, color)
        self.register_updates(y-yr, y+yr-1)

    def register_updates(self, y0, y1=None):
        # this function takes the top and optional bottom address of the changes made
        # and updates the pages_to_change list with any changed pages
        # that are not yet on the list
        start_page = max(0, y0 // 8)
        end_page = max(0, y1 // 8) if y1 is not None else start_page
        # rearrange start_page and end_page if coordinates were given from bottom to top
        if start_page > end_page:
            start_page, end_page = end_page, start_page
        for page in range(start_page, end_page+1):
            self.pages_to_update |= 1 << page

    def reset(self, res=None):
        if res is not None:
            res(1)
            time.sleep_ms(1)
            res(0)
            time.sleep_ms(20)
            res(1)
            time.sleep_ms(20)


class SH1106_I2C(SH1106):
    def __init__(self, width, height, i2c, res=None, addr=0x3c,
                 rotate=0, external_vcc=False, delay=0):
        self.i2c = i2c
        self.addr = addr
        self.res = res
        self.temp = bytearray(2)
        self.delay = delay
        if res is not None:
            res.init(res.OUT, value=1)
        super().__init__(width, height, external_vcc, rotate)

    def write_cmd(self, cmd):
        '''1) this function uses lower level function i2c.writeto() to send commands to SH1106
display driver. i2cwriteto() sends to a device's i2c address a byte array.
For an SH1106, 0-th byte of the array indicates if the 1-th byte is a command or is
(the first of) a data byte array.
in self.write_cmd, 0-th byte is set to 0x80 which indicates the 1-th byte is a command.
According to SH1106 datasheet (https://cdn.velleman.eu/downloads/29/infosheets/sh1106_datasheet.pdf)
"a command word consists of a control byte, which defines Co and D/C (note1), plus a data
byte (see Fig.7)."
        '''
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)
        print(self.temp)

    def write_data(self, buf):
        '''2) this function uses lower level function i2c.writeto() to send DATA to SH1106
display driver. i2cwriteto() sends to a device's i2c address a byte array.
For an SH1106, 0-th byte of the array indicates if the 1-th byte is a command or is
(the first of) a data byte array.
in self.write_cmd, 0-th byte is set to 0x40 which indicates the 1-th byte is DATA.
According to SH1106 datasheet (https://cdn.velleman.eu/downloads/29/infosheets/sh1106_datasheet.pdf)
"a command word consists of (...) The last control byte is tagged with a cleared most
significant bit, the continuation bit Co. After a control byte with a cleared Co-bit, only
data bytes will follow."
        '''
        self.i2c.writeto(self.addr, b'\x40'+buf)
        print(buf)

    def reset(self,res=None):
        super().reset(self.res)


class SH1106_SPI(SH1106):
    def __init__(self, width, height, spi, dc, res=None, cs=None,
                 rotate=0, external_vcc=False, delay=0):
        dc.init(dc.OUT, value=0)
        if res is not None:
            res.init(res.OUT, value=0)
        if cs is not None:
            cs.init(cs.OUT, value=1)
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        self.delay = delay
        super().__init__(width, height, external_vcc, rotate)

    def write_cmd(self, cmd):
        if self.cs is not None:
            self.cs(1)
            self.dc(0)
            self.cs(0)
            self.spi.write(bytearray([cmd]))
            self.cs(1)
        else:
            self.dc(0)
            self.spi.write(bytearray([cmd]))

    def write_data(self, buf):
        if self.cs is not None:
            self.cs(1)
            self.dc(1)
            self.cs(0)
            self.spi.write(buf)
            self.cs(1)
        else:
            self.dc(1)
            self.spi.write(buf)

    def reset(self, res=None):
        super().reset(self.res)