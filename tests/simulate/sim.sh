#!/bin/bash

source env/bin/activate

for sensor in 01 77 03
do
    python3 simulate_mqtt.py "sensor/sensor$sensor" "test" --period 3 --mqtt_host "192.168.1.83" &
done