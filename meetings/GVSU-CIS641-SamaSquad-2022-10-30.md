## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Oct. 30, 2022

Time: Noon, over lunch

Discussion points:

* Got sensor working and taking environmental readings
    * Currently transmitting only over serial (wired USB) connection - wireless coming soon(tm)

<br>

* Instead of the sensor just blasting data or the Pi activating the sensor, we might be able to use a pub/sub system
    * Mosquitto MQTT broker

<br>

* Flask-MQTT and other options for connecting MQTT pub/sub to a db:
    * https://flask-mqtt.readthedocs.io/en/latest/
    * https://www.hivemq.com/blog/mqtt-sql-database/

<br>

* Found a way to use QEMU to emulate a Pi in a VM - takes a long time to install from source, but I *think* the Pi emulation side should be pretty smooth
    * Though a basic vanilla Debian VM might be close enough without the hassle / overhead of emulation...

<br>

Goals for next week (include responsibilities):

* See if MQTT is the most viable strategy (responsibility: GA)
    * https://randomnerdtutorials.com/esp32-mqtt-publish-bme280-arduino/
    * https://mosquitto.org/
    * https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/

* Explore pub/sub using a quick-and-dirty Node-RED dashboard (responsibility: GA)
    * Will not be the final product - just a POC prototype
