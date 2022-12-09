# Overview

This document outlines the system requirements specification, consisting of functional and non-functional requirements, for Project Sama - our guitar temperature and humidity monitoring system.

This system consists of three major components:
- the *remote sensor(s)* that measure local temperature and humidity;
- the *base unit* that controls the remote sensor(s), analyzes and stores sensor data, and serves the web interface; and
- the *web interface* that allows users to monitor environmental conditions

Functional and non-functional requirements will be listed for each major component.

# Software Requirements
<Describe the structure of this section>

<!-- # Functional Requirements

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
    1. Users should be able to set up password-authenticated access to the web interface. -->

## Functional Requirements
### Remote Sensors
| ID | Requirement |
| -- | ----------- |
| FR | Sensor(s) shall take temperature readings. |
| FR | Sensor(s) shall record temperature in Celsius |
| FR | Sensor(s) shall take humidity readings. |
| FR | Sensor(s) shall record humidity as relative humidity |
| FR | Sensor(s) shall use I2C for communication with the controller |
| FR | Sensor(s) shall be compatible with BME280 specifications |
| FR | Sensor(s) shall be cabable of interfacing with a wireless board compatible with ESP8266 specifications |
| FR | Sensor(s) shall be capable of taking rapid temperature and humidity readings over a short period of time |

### Wireless Board(s)
| ID | Requirement |
|--- | ----------- |
| FR | The wireless board(s) shall be able to connect to a wireless network |
| FR | The wireless board(s) shall be able to connect to a publish/subscribe broker |
| FR | The wireless board(s) shall be able to publish on a specified topic name |
| FR | The wireless board(s) shall publish averaged readings back to the base unit in a usable data form. |
| FR | Sensor(s) should be capable of operating off of a Micro USB power cable |


### Raspberry Pi
| ID | Requirement |
| -- | ----------- |
| FR | The Raspberry Pi shall manage sensor(s) wirelessly. |
| FR | The Raspberry Pi shall host a database to store sensor logs. |
| FR | The Raspberry Pi shall host the server for the web interface. |
| FR | The Raspberry Pi shall posess data analysis capabilities. |
| FR | The Raspberry Pi shall be capable of continuous operation without external user intervention. |
| FR | The Raspberry Pi shall be able to connect to a wireless network |

### Web Server
| ID | Requirement |
| -- | ----------- |
| FR | Users shall be able to access the web interface from a web browser on their local network. |
| FR | The web server shall run on the Raspberry Pi unit. |
| FR | The web server shall communicate with the publish/subscribe broker service running on the Raspberry Pi. |
| FR | Uses shall be able to select Fahrenheit or Celsius for the display temperature |
| FR | Users shall be able to set  upper and lower bounds (in degrees Fahrenheit or Celsius) for acceptable temperatures ranges. |
| FR | Users shall be able to set upper and lower bounds (in percent relative humidity) for acceptable humidity ranges. |
| FR | The web interface shall send a notification if either temperature or humidity drift out of the established acceptable range (see **functional requirements 3.3 and 3.4**). |

### Web Dashboard
| ID | Requirement |
| FR | The web dashboard shall display the most recent averaged temperature reading. |
| FR | The web dashboard shall display the most recent averaged humidity reading. |
| FR | The web dashboard shall display temperature trends consisting of the last ten readings. |
| FR | The web dashboard shall display humidity trends consisting of the last ten readings. |
| FR | ... |

## Non-Functional Requirements

### Remote Sensors
| ID | Requirement |
| -- | ----------- |
| NFR | Sensor(s) should accurately and reliably record and transmit temperature and humidity readings. |
| NFR | Sensor(s) should be tolerant to measurement failure |
| NFR | Sensor(s) should take averaged readings to minimize the effect of random fluctuations |
| NFR | Sensor(s) should operate in a power-efficient manner |
| NFR | Sensor should be connected to the wireless board with secure wiring |

### Wireless Board(s)
| ID | Requirement |
|--- | ----------- |
| NFR | Board should be powerable through Micro USB power |
| NFR | Board should operate in a power-efficient manner |
| NFR | Board should be small enough to fit |
| NFR |  |
| NFR |  |

### Raspberry Pi Services
| ID | Requirement |
| -- | ----------- |
| NFR | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run on at minimum a Raspberry Pi 3 Model B. |
| NFR | All systems (i.e., dashboard server, control program, and analysis/logging routines) should be able to run concurrently with minimal slowdown perceived by the user. |
| NFR | The base unit should be able to restart all services after a reboot without significant user intervention (see **functional requirement 2.5**). |
| NFR | Users should be able to install all necessary files to install and run this service through a simple command line script. |

### Web Server
| ID | Requirement |
| -- | ----------- |
| NFR |  |
| NFR |  |
| NFR |  |
| NFR |  |
| NFR |  |

### Web Dashboard
| ID | Requirement |
| -- | ----------- |
| NFR | The web interface should be responsive and usable on a phone screen and/or other touch screen devices (while connected to the user's local network). |
| NFR | Users should be able to access temperature and humidity logs, and either display them graphically or access them as data files. |
| NFR | Users should be able to set up password-authenticated access to the web interface. |
| NFR |  |
| NFR |  |

# Change Management Plan

# Traceability links

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| ----------- | ------------- | -------------- |
| … | … | … |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| ------------- | -------------- |
| … | … | … |

## Activity Diagram Traceability

to the file and to those requirements impacted>
| Artifact ID | Artifact Name | Requirement ID |
| ----------- | ------------- | -------------- |
| … | … | … |

# Software Artifacts