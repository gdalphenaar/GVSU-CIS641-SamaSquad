#!/bin/bash

source env/bin/activate

for sensor in 01 02 03
do
    python3 simulate.py "sensor$sensor" --period 3 --mqtt_host "0.0.0.0" &
done