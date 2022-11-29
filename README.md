# Sama Squad

The goal for this project is to build a Raspberry Pi-controlled temperature and humidity monitor for guitars. This system will allow a user to access a web-based dashboard displaying current and historic guitar climate information on their local network. The user will also be able to customize some settings, including the desired "normal" humidity range and the logging period and frequency of the sensor(s). More information will be added here as project details are hashed out.

## Team Members and Roles

* [Grant Alphenaar](https://github.com/gdalphenaar/CIS641-HW2-Alphenaar): Supreme Project Commander

## Prerequisites

* BME280 sensor, ESP8266 WiFi board, and ability to connect both components (soldering iron, etc.) - this project has been designed with a D1 mini ESP8266 board connected to a GY-BMEP BME280 sensor, but should work with either:
    * Another compatible ESP8266 and/or BME280
    * Any other device that can publish MQTT messages in the appropriate JSON format
    * If you just want to test this project without putting a physical sensor unit together, the simulation code will simulate the proper MQTT messages

<br>

* Arduino IDE and the necessary libraries
    * List libraries with links

<br>

* Raspberry Pi (preferably, but this project can also run on most "always on" Debian-based systems)
    * Add more details about compatibility

## Run Instructions

* ## Sensor Setup
    * Connect BME280 sensor to ESP8266
    * Create an Arduino Sketch using `sensor.ino`
    * Using Arduino IDE, upload `sensor.ino` to the ESP8266 board