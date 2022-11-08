import paho.mqtt.client as mqtt
import time
import random


# set topic names here
# prefaced with `sim` for clarity / testing
topic_temperature = 'sim/temperature'
topic_humidity    = 'sim/humidity'


# address of raspberry pi or VM
mosquitto_addr = "192.168.1.77"
port =1883


# simulate pub/sub messages from sensor - 5 readings followed by a 30-second wait
print('simulation running')
while True:
    client = mqtt.Client()
    client.connect(mosquitto_addr, port)
    # for t in range(5):
    rand_f = random.uniform( -(time.time()%10), time.time()%10 )
    temp = str(round(22 + rand_f, 2))
    humd = str(round(45 + rand_f, 2))
    client.publish(topic_temperature, payload=temp, qos=1)
    client.publish(topic_humidity, payload=humd, qos=1)
    print(temp)
    print(humd)
    time.sleep(1)
    # time.sleep(10)