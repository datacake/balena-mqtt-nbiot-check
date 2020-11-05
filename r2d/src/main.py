import time
import paho.mqtt.client as mqtt
from random import randrange

DATACAKE_TOKEN = "PUTYOURTOKENHERE"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dtck/balena-fin-cellular-demo/0e5d7891-7b73-4377-a7f9-f837a12df327/OUTPUT_FIELD")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    random_value = randrange(100)
    random_value += 200
    client.publish("dtck-pub/balena-fin-cellular-demo/0e5d7891-7b73-4377-a7f9-f837a12df327/PM25", random_value)

if __name__ == "__main__":

    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set()
    client.username_pw_set(DATACAKE_TOKEN, password=DATACAKE_TOKEN)
    client.connect("mqtt.datacake.co", 8883, 60)
    client.loop_start()

    while (True):
        random_value = randrange(100)
        client.publish("dtck-pub/balena-fin-cellular-demo/0e5d7891-7b73-4377-a7f9-f837a12df327/PM10", random_value)
        time.sleep(300)
