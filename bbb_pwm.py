import Adafruit_BBIO.PWM as PWM
import xml.etree.ElementTree as ET
import time

PWM.start("P8_13",100,1000)
while True:
 try:
  tree= ET.parse('ven.xml')
  root = tree.getroot()
  data=root.findtext('value')
  print('Current Value from Grid =',data)
  y= float(data)
  if y<51:
     dc = y/0.6
  else:
     dc = (y/2.5) + 64


  if dc>100:
     dc=100
  print('Duty Cycle =',dc)


  PWM.set_duty_cycle("P8_13",dc)
 except:
  print("file not found")

