import time, random, json, argparse
import paho.mqtt.client as mqtt


# get user arguments
parser = argparse.ArgumentParser(
    description='Simulate MQTT pub/sub IoT sensor traffic'
)
parser.add_argument(
    'topic',
    type=str,
    help='topic to publish on'
)
parser.add_argument(
    '--period',
    type=int,
    default=30,
    help='publishing period in seconds'
)
parser.add_argument(
    '--start_temp',
    type=float,
    default=20.0,
    help='starting temperature value'
)
parser.add_argument(
    '--start_humd',
    type=float,
    default=45.0,
    help='starting humidity value'
)
parser.add_argument(
    '--mqtt_host',
    type=str,
    default='localhost',
    help='MQTT host addresss'
)
parser.add_argument(
    '--mqtt_port',
    type=int,
    default=1883,
    help='MQTT port'
)
args = parser.parse_args()


# simulate pub/sub messages from sensor
while True:

    # make mqtt connection
    client = mqtt.Client()
    client.connect(args.mqtt_host, args.mqtt_port)

    # add some randomness to readings
    rand_t = random.uniform( -(time.time()%10)/10, time.time()%10/10 )
    rand_h = random.uniform( -(time.time()%10)/10, time.time()%10/10 )

    # '''take''' readings
    temp = round(args.start_temp + rand_t, 2)
    humd = round(args.start_humd + rand_h, 2)

    # compose message
    message = json.dumps({
        "sensor":args.topic,
        "temp":temp,
        "humd":humd
    })

    # publish message on specified topic
    client.publish(args.topic, payload=message, qos=1)

    # print message for debugging
    print(message)

    # wait for specified time period
    time.sleep(args.period)