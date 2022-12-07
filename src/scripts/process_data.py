import paho.mqtt.client as mqtt
import json
import pymongo


# connect to mongodb
client = pymongo.MongoClient("localhost", 27017)
db = client.test
collection = db.test_collection


# connect to mosquitto
mosquitto_addr = "localhost"
port =1883


# subscribe to a topic
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('sensor/sensor01')


# receive a published message
def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(data)
    collection.insert_one(data).inserted_id
    # print(collection.count_documents({}))


# connect and loop
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mosquitto_addr, port)
client.loop_forever()