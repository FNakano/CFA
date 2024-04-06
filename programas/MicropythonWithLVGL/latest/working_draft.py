# o código que mostra como mudar o tamanho da letra está em font.py

import lvgl as lv
from ili9XXX import st7789
import axp202c
axp=axp202c.PMU()
axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
axp.setLDO2Voltage(2800)
disp = st7789(
  mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
  width=240, height=240, factor=4)
from ft6x36 import ft6x36 # https://github.com/lvgl/lv_binding_micropython?tab=readme-ov-file#micropython-bindings-usage
touch = ft6x36(sda=23, scl=32, width=240, height=240, inv_y=True, inv_x=True)

#you can replace the lvgl.grid_fr(x) with pixel width/height
row = [ lv.grid_fr(1), lv.grid_fr(1), lv.GRID_TEMPLATE_LAST ]
column = [ lv.grid_fr(1), lv.grid_fr(1), lv.GRID_TEMPLATE_LAST ]

cont = lv.obj() # cont is the screen
cont.set_size( 240, 240 )
cont.center()
cont.set_layout( lv.LAYOUT.GRID )
cont.set_style_grid_row_dsc_array( row, 0 ) 
cont.set_style_grid_column_dsc_array( column, 0 )

def butt( text, row_x, column_y ):
    btn = lv.button( cont )
    
    label = lv.label( btn )
    label.set_text( text )
    label.center()
    
    btn.set_grid_cell( lv.GRID_ALIGN.STRETCH, row_x, 1, lv.GRID_ALIGN.CENTER, column_y, 1 )
    
    return btn

butt( 'hi1', 0, 0 )
butt( 'hi2', 1, 0 )
butt( 'hi3', 0, 1 )
butt( 'hi4', 1, 1 )

lv.screen_load(cont)
