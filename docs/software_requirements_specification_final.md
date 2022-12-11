# Overview

This document outlines the system requirements specification, consisting of functional and non-functional requirements, for Project Sama - our guitar temperature and humidity monitoring system.

This system consists of three major components:
- the *remote sensor(s)* that measure local temperature and humidity;
- the *base unit* that controls the remote sensor(s), analyzes and stores sensor data, and serves the web interface; and
- the *web interface* that allows users to monitor environmental conditions

Functional and non-functional requirements will be listed for each major component.

# Software Requirements
<Describe the structure of this section>

## Functional Requirements
### 1. Remote Sensors
| ID | Requirement |
| -- | ----------- |
| FR1.1 | Sensor(s) shall take temperature readings in Celsius |
| FR1.2 | Sensor(s) shall take humidity readings measured as percent relative humidity|
| FR1.3 | Sensor(s) shall use I2C for communication with the controller |
| FR1.4 | Sensor(s) shall be compatible with BME280 specifications |
| FR1.5 | Sensor(s) shall be cabable of interfacing with a wireless board compatible with ESP8266 specifications |
| FR1.6 | Sensor(s) shall be capable of taking rapid temperature and humidity readings over a short period of time |
| FR1.7 | Sensor(s) shall be capable of taking averaged temperature and humidity readings |

### 2. Wireless Board(s)
| ID | Requirement |
|--- | ----------- |
| FR2.1 | Board(s) shall be able to connect to a wireless network |
| FR2.2 | Board(s) shall be able to connect to a publish/subscribe broker |
| FR2.3 | Board(s) shall be compatible with ESP8266 specifications |
| FR2.4 | Board(s) shall be able to publish on a specified topic name |
| FR2.5 | Board(s) shall publish averaged readings back to the base unit in JSON form. |
| FR2.6 | Board(s) shall be capable of operating off of continuous wall power |


### Raspberry Pi
| ID | Requirement |
| -- | ----------- |
| FR3.1 | The Raspberry Pi shall be able to connect to a wireless network |
| FR3.2 | The Raspberry Pi shall host a publish/subscribe broker service for sensor communication |
| FR3.3 | The Raspberry Pi shall host the server for the web interface. |
| FR3.4 | The Raspberry Pi shall be able to operate with or without a connected monitor |
| FR3.5 | The Raspberry Pi shall be capable of continuous operation without external user intervention. |

### Web Server
| ID | Requirement |
| -- | ----------- |
| FR4.1 | Users shall be able to access the web interface from a web browser on their local network. |
| FR4.2 | The web server shall run on the Raspberry Pi unit. |
| FR4.3 | The web server shall be capable of interfacing with a publish/subscribe broker |
| FR4.4 | The web server shall be capable of subscribing to new sensors |
| FR4.5 | The web server shall be capable of unsubscribing from sensors |
| FR4.6 | The web server shall be capable of storing user settings |

### Web Dashboard
| ID | Requirement |
| -- | ----------- |
| FR5.1  | The web dashboard shall display the most recent averaged humidity reading |
| FR5.2  | The web dashboard shall display the most recent averaged temperature reading |
| FR5.3  | Users shall be able to select Fahrenheit or Celsius for the display temperature |
| FR5.4  | The web dashboard shall provide conversion between Celsius and Fahrenheit units |
| FR5.5  | Users shall be able to set upper and lower bounds (in degrees Fahrenheit or Celsius) for acceptable temperatures ranges. |
| FR5.6  | Users shall be able to set upper and lower bounds (in percent relative humidity) for acceptable humidity ranges. |
| FR5.7  | The web dashboard shall display a visual alert if humidity exceeds set upper bound (see ***FR5.5***) |
| FR5.8 | The web dashboard shall display a visual alert if humidity falls below set lower bound (see ***FR5.5***) |
| FR5.9  | The web dashboard shall display a visual alert if temperature exceeds set upper bound (see ***FR5.4***) |
| FR5.10  | The web dashboard shall display a visual alert if temperature falls below set lower bound (see ***FR5.4***) |
| FR5.11 | The web server shall be able to add and remove new sensors |

## Non-Functional Requirements

### Remote Sensors
| ID | Requirement |
| -- | ----------- |
| NFR1.1 | Sensor(s) should accurately and reliably record temperature and humidity readings |
| NFR1.2 | Sensor(s) should accurately and reliably publish temperature and humidity readings |
| NFR1.3 | Sensor(s) should be tolerant to measurement failure |
| NFR1.4 | Sensor(s) should take averaged readings to minimize the effect of random fluctuations (see ***FR1.7***) |
| NFR1.5 | Sensor(s) should operate in a power-efficient manner |
| NFR1.6 | Sensor should be connected to the wireless board with secure wiring |
| NFR1.7 | Sensor(s) should be cheap to purchase (see ***NFR2.4***) |

### Wireless Board(s)
| ID | Requirement |
|--- | ----------- |
| NFR2.1 | Board(s) should be powerable through Micro USB power (see ***FR2.5***) |
| NFR2.2 | Board(s) should operate in a power-efficient manner |
| NFR2.3 | Board(s) should be small enough to fit close to a guitar stand |
| NFR2.4 | Board(s) should be cheap to purchase (see ***NFR1.7***) |
| NFR2.5 | Board(s) should be programmable using the Arduino IDE |
| NFR2.6 | Board(s) shall require minimal external libraries |
| NFR2.7 | Board(s) should publish new readings every 30 seconds |
| NFR2.8 | Board(s) should take 20 averaged readings across 5 seconds every 25 seconds (see ***NFR1.4***) |

### Raspberry Pi Services
| ID | Requirement |
| -- | ----------- |
| NFR3.1 | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run on at minimum a Raspberry Pi 3 Model B. |
| NFR3.2 | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run concurrently with minimal slowdown perceived by the user. |
| NFR3.3 | The base unit should be able to restart all services after a reboot without significant user intervention (see **FR2.5**). |
| NFR3.4 | Users should be able to install all necessary files to install and run this service through a simple command line script. |
| NFR3.5 | The Raspberry Pi should use a Mosquitto MQTT broker for publish/subscribe interfacing |

### Web Server
| ID | Requirement |
| -- | ----------- |
| NFR4.1 | The web server should be capable of running for long periods on the Raspberry Pi without exhausting memory  |
| NFR4.2 | The web server should generate minimal network traffic |
| NFR4.3 | The web server should be written using the Flask framework |
| NFR4.4 | The web server should require minimal external libraries |
| NFR4.5 | The web server should be capable of opening a web socket to the served dashboard pages |
| NFR4.6 | The web server should load its settings from an external JSON file |

### Web Dashboard
| ID | Requirement |
| -- | ----------- |
| NFR5.1 | The web dashboard should be responsive and usable on a phone screen and/or other touch screen devices (while connected to the user's local network). |
| NFR5.2 | The web dashboard should make effective use of color to denote temperature and humidity status
| NFR5.3 | The web dashboard should be easy to navigate |
| NFR5.4 | The web dashboard should be intuitive to operate with minimal familiarity |
| NFR5.5 | The web dashboard should have the main dashboard view as the home page |
| NFR5.6 | The web dashboard should have a minimal number of pages |
| NFR5.7 | The web dashboard should have a page for users to change settings |
| NFR5.8 | the web dashboard should have a page for user management of sensors |

# Change Management Plan

# Traceability links

The following tables provide links between Use Case Diagrams, Class Diagrams, and Activity diagrams, along with the requirements that are satisfied by those diagrams. Note that, due to the heavy interconnectedness among many of the requirements for this system, each artifact satisfies a great number of requirements.

## Use Case Diagram Traceability

There are three major use cases in this system:
1. Monitoring the current environmental conditions
2. Interacting with the dashboard and changing "cosmetic" settings
3. Adding or removing sensors

| Artifact ID | Artifact Name | Requirement ID | Notes |
| ----------- | ------------- | -------------- | ----- |
| [UCD1](../artifacts/use_case_diagrams/UCD1.png) | Monitor Environmental Conditions | FR1.1, FR1.2, FR1.6, FR1.7, FR2.4, FR3.2 | The "passive" part of the system: once the dashboard and MQTT broker are properly set up, the broker waits for messages from the sensors and passes them on without user interaction  |
| [UCD2](../artifacts/use_case_diagrams/UCD2.png) | Interact with Dashboard | FR3.1, FR3.2, FR3.3, FR4.1, FR4.2, FR4.3, FR4.4, FR4.5, FR5.11, FR5.1, FR5.2, FR5.3, FR5.4, FR5.5, FR5.6, FR5.7, FR5.8, FR5.9, FR5.10, FR5.11, NFR5.7, NFR5.8 | The bulk of the user's interaction with the dashboard, consisting of viewing it, changing temperature units, and setting temperature and humidity thresholds |
| [UCD3](../artifacts/use_case_diagrams/UCD3.png) | Add or Remove Sensors | FR4.3, FR4.4, FR4.5, FR5.11 | The other main use case involving user interaction: here, the user adds or removes sensors from the dashboard view |

## Class Diagram Traceability

Here, there are two class diagrams, of which the second is a more detailed subset of the first. The first class diagram provides a very high-level overview of the system as a whole. The second class diagram breaks the dashboard - represented as a single class in the first class diagram - into its three component pages, each represented as a class. This serves to show the further delegation of responsibilities that each component of the dashboard is responsible for.

| Artifact ID | Artifact Name | Requirement ID | Notes |
| ----------- | ------------- | -------------- | ----- |
| [CD1](../artifacts/class_diagrams/CD1.png) | System Class Diagram | FR1.1, FR1.2, FR1.5, FR1.6, FR1.7, FR2.1, FR2.2, FR2.4, FR2.5, FR3.1, FR3.2, FR3.3, FR4.1, FR4.2, FR4.3, FR4.4, FR4.5, FR4.6, FR5.1, FR5.2, FR5.3, FR5.4, FR5.5, FR5.6, FR5.7, FR5.8, FR5.9, FR5.10, FR5.11 | The main class diagram providing a high-level view of the entire system |
| [CD2](../artifacts/class_diagrams/CD2.png) | Web Dashboard Class Diagram |FR5.1, FR5.2, FR5.3, FR5.4, FR5.5, FR5.6, FR5.7, FR5.8 FR5.9, FR5.10, FR5.11, NFR5.2, NFR5.5, NFR5.7, NFR5.8 | A class diagram of just the web dashboard, showing specific classes and responsibilities |

## Activity Diagram Traceability

Here, there are 6 main activities:
1. Taking a temperature reading
2. Taking a humidity reading
3. Changing humidity upper and lower bounds
4. Changing temperature upper and lower bounds
5. Changing between Fahrenheit and Celsius
6. Adding and removing sensors

| Artifact ID | Artifact Name | Requirement ID | Notes |
| ----------- | ------------- | -------------- | ----- |
| [AD1](../artifacts/activity_diagrams/AD1.png) | Take Humidity Reading | FR1.2, FR1.6, FR1.7, FR2.2, FR2.4, FR2.5, FR3.2, FR5.1, FR5.7, FR5.8 | One half of the monitoring loop, along with **AD2** |
| [AD2](../artifacts/activity_diagrams/AD2.png) | Take Temperature Reading | FR1.1, FR1.6, FR1.7, FR2.2, FR2.4, FR2.5, FR3.2, FR5.2, FR5.9, FR5.10 | The other half of the monitoring loop, along with **AD1** |
| [AD3](../artifacts/activity_diagrams/AD3.png) | Change Humidity Bounds | FR5.5| Change the threshold at which humidity is in the "danger zone" |
| [AD4](../artifacts/activity_diagrams/AD4.png) | Change Temperature Bounds | FR5.6, NFR5.2, NFR5.7 | Change the threshold at which temperature is in the "danger zone" |
| [AD5](../artifacts/activity_diagrams/AD5.png) | Change Temperature Units | FR5.3, FR5.4, NFR5.2, NFR5.7  | Toggle between Fahrenheit and Celsius |
| [AD6](../artifacts/activity_diagrams/AD6.png) | Add or Remove Sensors | FR2.2, FR2.3, FR3.2, FR5.11, NFR5.8 | The main management loop - adding and removing sensors from the dashboard |

# Software Artifacts

See individually linked artifacts in the traceability tables.