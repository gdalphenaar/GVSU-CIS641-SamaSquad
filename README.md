# Sama Squad

The goal for this project is to build a Raspberry Pi-controlled temperature and humidity monitor for guitars. This system will allow a user to access a web-based dashboard displaying current and historic guitar climate information on their local network. The user will also be able to customize some settings, including the desired "normal" humidity range and the logging period and frequency of the sensor(s). More information will be added here as project details are hashed out.

## Team Members and Roles

* [Grant Alphenaar](https://github.com/gdalphenaar/CIS641-HW2-Alphenaar): Supreme Project Commander

## Prerequisites

* BME280 sensor, ESP8266 WiFi board, and ability to connect both components (soldering iron, etc.) - this project has been designed with a D1 mini ESP8266 board connected to a GY-BMEP BME280 sensor, but should work with either:
    * Another compatible ESP8266 and/or BME280
    * Any other device that can publish MQTT messages in the appropriate JSON format

* Arduino IDE

* Raspberry Pi (preferably, but this project can also run on most "always on" Linux-based systems with few - if any - tweaks required)
    * Note: these instructions assume some familiarity with Raspberry Pi computers as well as the Arduino IDE

## Instructions

0. Set Up Sensor
    1. Before starting anything else, the sensors should be connected. Start by connect the BME280 sensor to the ESP8266 microcontroller - this might require a bit of soldering.
    1. At this point, set the sensor aside - we don't have enough information to get it fully set up and configured just yet.
<br/><br/>
1. Set Up Raspberry Pi
    1. Note: these instructions were tested using a clean (i.e., fresh install) Raspberry Pi OS 62 bit released 09-22-2022 running in desktop mode, but was ultimately set up in headless mode.
    1. Before starting anything else, make a note of your Raspberry Pi's IP address - this address will be used for connecting the sensors to the MQTT broker and will be used to access the dashboard. To get the IP address, run `hostname -I` and you should get an IP address of the form `192.168.1.xxx`. If starting the Raspberry Pi in headless mode, run `ping raspberrypi.local` and you should see the unit's IP address pinged.
    1. To make things easier, you can pre-enable SSH and enter WiFi credentials in the Raspberry Pi Imager before writing the OS to a Micro SD card.
    1. `git clone` this repo (i.e., [https://github.com/gdalphenaar/GVSU-CIS641-SamaSquad.git](https://github.com/gdalphenaar/GVSU-CIS641-SamaSquad.git)) to the folder of your choice on the Raspberry Pi. For convenience, I used `/Documents/MQTT-Sensors.
    1. From this folder, navigate to `/src/scripts` and run `setup.sh`. This will download the Mosquitto MQTT broker and start the web dashboard. At this point, you can navigate to the IP address you found earlier at port 8080 in a web browser. You'll see nothing at this point, because no sensors have been set up.
<br/><br/>
1. Set Up Sensors
    1. Create a sketch in Arduino IDE using `/src/sensors/sensor.ino` and import the necessary external libraries.
    1. Replace `WIFI_SSID` and `WIFI_PASSWORD` with your WiFi network and credentials, respectively.
    1. Replace `MQTT_HOST` with the IP address of your Raspberry Pi. Keep `MQTT_PORT` as 1883, unless you changed the MQTT listener port.
    1. Replace `MQTT_PUB_NAME` with the name/ID you want this sensor to publish under. Remember this name, as this is what you will use to make the dashboard listen to the sensors
    1. Compile and upload the code to the board. If desired, you can turn the serial monitor on in Arduino IDE at 9600 baud to see the published readings from the sensor, along with a `pub ack` signaling successful receipt of the readings.
    1. Repeat this process for each sensor you want to use.
<br/><br/>
1. Verify Dashboard Functionality
    1. Navigate back to the web dashboard. At this point, it should still be empty, but we will add the first sensor now.
    1. Navigate to **Manage Sensors** in the top right corner of the interface. Enter the sensor name that you used for `MQTT_PUB_NAME` in the Sensor ID field. In the Sensor Name field, give this sensor a more memorable name - for example, "Living Room".
    1. Click Add Sensor and navigate back to the **Dashboard** using the link in the top right. You should now see you sensor.
<br/><br/>
1. Configure Settings.
    1. The dashboard comes configured with some "safe-for-guitars" temperature and humidity ranges, but should you wish to do so, you can change them on the **Settings** page linked in the top right.
    1. By default, the sensors measure and transmit in Celsius. Should you desire, you can change to Fahrenheit in on the **Settings** page as well.
<br/><br/>
1. Remove a Sensor
    1. Should you need to remove a sensor, you can do that from the **Manage Sensors** page as well. Now that you have a sensor added, you should see a sensor listed on the management page.
    1. Clicking **Remove Sensor** will unsubscribe the dashboard from that topic. Note that until powered off or otherwise taken offline, the sensor itself will continue to publish under its specified ID.
<br/><br/>
1. Final Notes
    1. You should now be ready to use the dashboard to start monitoring temperature and humidity for your guitars!
    1. A green sensor panel indicates that both temperature and humidity are within the configured ranges.
    1. If either temperature or humidity strays outside of the configured ranges (either above or below), however, the panel will light up red and the problematic metric will be highlighted further.