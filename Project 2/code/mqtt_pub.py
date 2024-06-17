import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("/kel6/room/temperature")

def on_message(client, userdata, message):
    readings=str(message.payload.decode("utf-8"))
    print("message received " ,readings)
    JsonReadings=json.loads(readings)
    print("Temperature=",JsonReadings["Temp"])
    if JsonReadings["Temp"]>1:
        client.publish("/kelompok_1/room/led","On")
    else:
        client.publish("/kelompok_1/room/led","Off")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="adios",password="adios")
client.connect("167.172.87.186", 1883, 60)
client.loop_forever()