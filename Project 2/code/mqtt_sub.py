import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) 

def on_connect(client, userdata, flags, rc):
    client.subscribe("/kelompok_1/room/led")

def on_message(client, userdata, message):
    if str(message.payload.decode("utf-8"))=="On":
        GPIO.output(12, GPIO.HIGH) 
    else:
        GPIO.output(12, GPIO.LOW)
    print("message received " ,str(message.payload.decode("utf-8")))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="adios",password="adios")
client.connect("167.172.87.186", 1883, 60)
client.loop_forever()