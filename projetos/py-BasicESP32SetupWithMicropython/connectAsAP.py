import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="Micropython-C3", password='123456789')
# https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/
