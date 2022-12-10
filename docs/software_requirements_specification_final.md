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
| FR1.3 | Board(s) shall be compatible with ESP8266 specifications |
| FR2.4 | Board(s) shall be able to publish on a specified topic name |
| FR2.5 | Board(s) shall publish averaged readings back to the base unit in a usable data form. |
| FR2.6 | Board(s) shall be capable of operating off of continuous wall power |


### Raspberry Pi
| ID | Requirement |
| -- | ----------- |
| FR3.1 | The Raspberry Pi shall be able to connect to a wireless network |
| FR3.2 | The Raspberry Pi shall host a publish/subscribe broker service for sensor communication |
| FR3.3 | The Raspberry Pi shall host the server for the web interface. |
| FR3.4 | The Raspberry Pi shall posess data analysis capabilities. |
| FR3.5 | The Raspberry Pi shall be capable of continuous operation without external user intervention. |

### Web Server
| ID | Requirement |
| -- | ----------- |
| FR4.1 | Users shall be able to access the web interface from a web browser on their local network. |
| FR4.2 | The web server shall run on the Raspberry Pi unit. |
| FR4.4 | The web server shall be capable of interfacing with a publish/subscribe broker |
| FR4. |

### Web Dashboard
| ID | Requirement |
| -- | ----------- |
| FR5.1  | The web dashboard shall display the most recent averaged temperature reading |
| FR5.2  | The web dashboard shall display the most recent averaged humidity reading |
| FR5.3  | Users shall be able to select Fahrenheit or Celsius for the display temperature |
| FR5.4  | The web dashboard shall provide conversion between Celsius and Fahrenheit units |
| FR5.5  | Users shall be able to set upper and lower bounds (in degrees Fahrenheit or Celsius) for acceptable temperatures ranges. |
| FR5.6  | Users shall be able to set upper and lower bounds (in percent relative humidity) for acceptable humidity ranges. |
| FR5.6  | The web dashboard shall display a visual alert if temperature exceeds set upper bound (see ***FR5.4***) |
| FR5.8  | The web dashboard shall display a visual alert if temperature falls below set lower bound (see ***FR5.4***) |
| FR5.9  | The web dashboard shall display a visual alert if humidity exceeds set upper bound (see ***FR5.5***) |
| FR5.10 | The web dashboard shall display a visual alert if humidity falls below set lower bound (see ***FR5.5***) |
| FR5.11 | The web server shall be able to add and remove new sensors|

## Non-Functional Requirements

### Remote Sensors
| ID | Requirement |
| -- | ----------- |
| NFR | Sensor(s) should accurately and reliably record temperature and humidity readings |
| NFR | Sensor(s) should accurately and reliably publish temperature and humidity readings |
| NFR | Sensor(s) should be tolerant to measurement failure |
| NFR | Sensor(s) should take averaged readings to minimize the effect of random fluctuations (see ***FR1.7***) |
| NFR | Sensor(s) should operate in a power-efficient manner |
| NFR | Sensor should be connected to the wireless board with secure wiring |
| NFR | Sensor(s) should be cheap to purchase (see ***NFR...***) |

### Wireless Board(s)
| ID | Requirement |
|--- | ----------- |
| NFR | Board(s) should be powerable through Micro USB power (see ***FR2.5***) |
| NFR | Board(s) should operate in a power-efficient manner |
| NFR | Board(s) should be small enough to fit close to a guitar stand |
| NFR | Board(s) should be cheap to purchase (see ***NFR...***) |
| NFR | Board(s) should be programmable using the Arduino IDE |
| NFR | Board(s) shall require minimal external libraries |
| NFR | Board(s) should publish new readings every 30 seconds |
| NFR | Board(s) should take 20 averaged readings across 5 seconds every 25 seconds (see ***NFR...***) |

### Raspberry Pi Services
| ID | Requirement |
| -- | ----------- |
| NFR | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run on at minimum a Raspberry Pi 3 Model B. |
| NFR | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run concurrently with minimal slowdown perceived by the user. |
| NFR | The base unit should be able to restart all services after a reboot without significant user intervention (see **functional requirement 2.5**). |
| NFR | Users should be able to install all necessary files to install and run this service through a simple command line script. |
| NFR | The Raspberry Pi should use a Mosquitto MQTT broker for publish/subscribe interfacing |

### Web Server
| ID | Requirement |
| -- | ----------- |
| NFR | The web server should be capable of running for long periods on the Raspberry Pi without exhausting memory  |
| NFR | The web server should generate minimal network traffic |
| NFR | The web server should be written using the Flask framework |
| NFR | The web server should require minimal external libraries |
| NFR | The web server should be capable of opening a web socket to the served dashboard pages |

### Web Dashboard
| ID | Requirement |
| -- | ----------- |
| NFR | The web dashboard should be responsive and usable on a phone screen and/or other touch screen devices (while connected to the user's local network). |
| NFR | The web dashboard should make effective use of color to denote temperature and humidity status
| NFR | The web dashboard should be easy to navigate |
| NFR | The web dashboard should be intuitive to operate with minimal familiarity |
| NFR | The web dashboard should have the main dashboard view as the home page |
| NFR | The web dashboard should have a minimal number of pages |
| NFR | The web dashboard should have a page for users to change settings |
| NFR | the web dashboard should have a page for user management of sensors |

# Change Management Plan

# Traceability links

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| ----------- | ------------- | -------------- |
| ... | ... | ... |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| ------------- | -------------- |
| ... | ... | ... |

## Activity Diagram Traceability

to the file and to those requirements impacted>
| Artifact ID | Artifact Name | Requirement ID | Notes |
| ----------- | ------------- | -------------- | ----- |
| ... | ... | ...| ... |

# Software Artifacts