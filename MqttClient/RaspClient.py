import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("temp")

def on_message(client, userdata, msg):
    print("Messaggio ricevuto!")
    p = String(msg.payload.decode())
    print(p)

client = mqtt.Client()
client.username_pw_set("username","password")
client.connect("/*Your_Ip*/",1883,60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()