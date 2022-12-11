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
    * Note: these instructions assume some familiarity with Raspberry Pi computers

## Run Instructions

0. Sensor Setup
    * Connect the BME280 sensor to the ESP8266 microcontroller
    * This might require a bit of soldering

1. Set Up Raspberry Pi
    1. Note: these instructions were tested using a clean (i.e., fresh install) Raspberry Pi OS 32 bit version x running in headless mode.
    1. Before starting anything else, make a note of your Raspberry Pi's IP address - this address

1. Set up