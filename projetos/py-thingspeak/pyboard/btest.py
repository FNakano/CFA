# mip.install("github:robert-hh/BME280")
# see data in graphic format at
# https://thingspeak.mathworks.com/channels/3399532

import config
import wifi
import i2c
import display
import requests
import json
import bme280_float as bme

b=None

def init ():
  global b
  b=bme.BME280(i2c=config.i2c)

def displayval():
  global b
  b.read_compensated_data()
  display.message(b.values)

def displayresp(r):
  if r.status_code==200 :
    d=json.loads(r.text)
    display.message([d["created_at"], d["field1"], d["field2"], d["field3"]])
  else :
    display.message(["http stat", str(r.status_code)])
      

def send():
  global b
  d=b.read_compensated_data()
  token="URK6ZA1E62Z5NF0N"
  url= f"https://api.thingspeak.com/update.json?api_key={token}&field1={d[0]}&field2={d[1]}&field3={d[2]}"
  return requests.get(url)  # should not send secrets by GET request but its easier... 


init()
# displayval() # measure and display
r=send() # measure again and send
displayresp(r)
# CRITICAL: Always close the connection to free up system memory
r.close()



