# Overview

This document outlines the system requirements specification, consisting of functional and non-functional requirements, for Project Sama - our guitar temperature and humidity monitoring system.

This system consists of three major components:
- the *remote sensor(s)* that measure local temperature and humidity;
- the *base unit* that controls the remote sensor(s), analyzes and stores sensor data, and serves the web interface; and
- the *web interface* that allows users to monitor environmental conditions

Functional and non-functional requirements will be listed for each major component.

# Functional Requirements

1. **Remote Sensor(s)**
    1. Sensor(s) shall be capable of taking temperature readings.
    1. Sensor(s) shall be capable of taking and humidity readings.
    1. Sensor(s) shall be compatible with BME280 specifications
    1. Sensor(s) shall be cabable of interfacing with a wireless board compatible with ESP8266 specifications
    1. Sensor(s) shall be capable of taking rapid temperature and humidity readings over a short period of time


<br>

1. **Wireless Board**
    1. The wireless board(s) shall be able to connect to a wireless network
    1. The wireless board(s) shall be able to connect to a publish/subscribe broker
    1. The wireless board(s)
    1. The wireless board(s) shall publish averaged readings back to the base unit in a usable data form.
    1. The wireless board(s) shall be capable of remote management by the base unit.

<br>

1. **Raspberry Pi Services**
    1. The base unit shall manage sensor(s) wirelessly.
    1. The base unit shall host a database to store sensor logs.
    1. The base unit shall host the server for the web interface.
    1. The base unit shall posess data analysis capabilities.
    1. The base unit shall be capable of continuous operation without external user intervention.

<br>

1. **Web Server**
    1. Users shall be able to access the web interface from a web browser on their local network.
    1. The web server shall run on the Raspberry Pi unit.
    1. The web server shall communicate with the publish/subscribe broker service running on the Raspberry Pi.
    1. Users shall be able to set  upper and lower bounds (in degrees Fahrenheit or Celsius) for acceptable temperatures ranges.
    1. Users shall be able to set upper and lower bounds (in percent relative humidity) for acceptable humidity ranges.
    1. The web interface shall send a notification if either temperature or humidity drift out of the established acceptable range (see **functional requirements 3.3 and 3.4**).


<br>

1. **Web Dashboard**
    1. The web dashboard shall display the most recent averaged temperature reading.
    1. The web dashboard shall display the most recent averaged humidity reading.
    1. The web dashboard shall display temperature trends consisting of the last ten readings.
    1. The web dashboard shall display humidity trends consisting of the last ten readings.

<br>

# Non-Functional Requirements

1. **Remote Sensor(s)**
    1. Sensor(s) should accurately and reliably record and transmit temperature and humidity readings.
    1. Sensor(s) should operate in a power-efficient manner
    1. Sensor(s) should be capable of operating off of a Micro USB power cable
    1. Sensor(s) should be able to be mounted to a guitar stand or stored in a guitar case.

1. **Base Unit**
    1. The system should take averaged temperature and humidity readings over a time period specified by the users to reduce fluctuation (see **functional requirement 3.6**).
    1. All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run on at minimum a Raspberry Pi 3 Model B.
    1. All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run concurrently with minimal slowdown perceived by the user.
    1. The base unit should be able to restart all services after a reboot without significant user intervention (see **functional requirement 2.5**).
    1. Users should be able to install all necessary files to install and run this service through a simple command line script.

1. **Web Interface**
    1. The web interface should be responsive and usable on a phone screen and/or other touch screen devices (while connected to the user's local network).
    1. Users should be able to access temperature and humidity logs, and either display them graphically or access them as data files.
    1. Users should be able to set up password-authenticated access to the web interface.

## Functional Requirements
### <Name of Feature 1>
| ID | Requirement |
| :-------------: | :----------: |
| FR1 | <Requirement 1> |
| FR2 | <Requirement 2> |
| FR3 | <Requirement 3> |
| … | … | … |