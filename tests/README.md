### `simulate`

Contains a short program to simulate MQTT pub/sub traffic in the absence of an actual sensor

```
Simulate MQTT pub/sub IoT sensor traffic

positional arguments:
  topic                 topic to publish on
  friendly              friendly name for sensor

optional arguments:
  --period PERIOD
                        publishing period in seconds

  --start_temp START_TEMP
                        starting temperature value

  --start_humd START_HUMD
                        starting humidity value

  --mqtt_host MQTT_HOST
                        MQTT host addresss

  --mqtt_port MQTT_PORT
                        MQTT port
```

Example:

`python3 simulate_mqtt.py "sensor/sensor77" "bedroom" --period=5 --mqtt_host="192.168.1.77"`

simulates a sensor publishing every 5 seconds on the topic "sensor/sensor77" with the friendly name "bedroom" to an MQTT broker on 192.168.1.77 using the default port (1883)