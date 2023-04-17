#----------------------------import classess from modules---------------------------
from machine import Pin, ADC
from time import sleep
import json
import network
import time
from umqtt.simple import MQTTClient
#-------------------------end of import classess from modules-----------------------

pot = ADC(Pin(34)) #create ADC object called pot on GPIO34 
pot.atten(ADC.ATTN_11DB) #able to read voltage in full range(0-3.3V)

SERVER = "mqtt.favoriot.com" 
client = MQTTClient("umqtt_client", SERVER, user="your API Key here", 
                    password="your API Key here")

station = network.WLAN(network.STA_IF) #create network interface 
station.active(True) #activate network interface 
station.disconnect()

if not station.isconnected(): #check if the station is connected to AP 
  print('connecting to network...') #display 'connecting to network...' message 
  station.connect("your ssid", "your password") #connect to an AP 
  time.sleep(3) 
  client.connect()
  
while station.isconnected(): 
  pot_value = pot.read() #to read the pot value and save it in the pot_value variable 
  dat = {"device_developer_id": "your Device Developer ID", "data": {'Voltage:' :pot_value}} 
  data = str(json.dumps(dat)) #parse dat in json format 
  topic = "your API Key here/v2/streams"
  
  client.publish(topic, data) 
  print(pot_value) #print the pot_value 
  time.sleep(3) #the pot_value will display (loop) every 3 seconds
