## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Nov. 6, 2022

Time: 5PM

Discussion points:

* Got sensor working and taking environmental readings *over WiFi* now
    * For now, just using Node-RED to test basic dashboarding and connectivity
    * Haven't tested on an actual Pi yet, but this is working in a Debian VM

<br>

* Settled on MQTT messaging for communication between sensors and Pi
    * Mosquitto MQTT broker on Pi
    * Paho MQTT for Python-based stuff

<br>

* Got simulated data working in a simple script ([see here](../tests/simulate/simulate_mqtt.py))
    * Also uses MQTT publishing for accurate simulations
    * Can be easily tweaked to mirror any changes on the sensor firmware

<br>

Goals for next week (include responsibilities):

* Use MQTT to interface between sensor and database (GA)
    * Starting with simulated data

<br>

* Connect simple web server to database
    * Again, using simulated data
