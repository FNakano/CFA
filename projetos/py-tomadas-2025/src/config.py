# User configured global variables (users may modify)
wifi_id = 'lab8'
wifi_password = 'lab8arduino'
myhostname = 'device001'
disp_width = 128
disp_height = 64

# Program internal global variables (users should not modify)
disp=None       # handle for the display
i2c=None        # handle for I2C
redled=None     # handle for a red led
blueled=None    # handle for a blue led
greenled=None   # handle for a green led
wifi_if=None    # handle for the wifi interface
app=None        # handle for Microdot application (web server)
messages=None   # list of messages currently displayed