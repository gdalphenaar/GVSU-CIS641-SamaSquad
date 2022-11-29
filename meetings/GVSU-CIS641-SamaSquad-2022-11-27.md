## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Nov. 27, 2022

Time: Around dinner time

Discussion points:

* Got web socket between MQTT client and Flask working
    * JavaScript SocketIO + Flask-SocketIO
    * "Lazy" approach - only take the most recent reading without any database connection
    * Have database only for archiving purposes

<br>

* Soft access point isn't *quite* working
    * Ended up somewhat moving on, though this is still definitely on the table if there's time at the end
    * Issue: WiFi and MQTT connection methods rely somewhat on constants, and loading data from EEPROM to a constant isn't quite working

<br>

Goals for next week (include responsibilities):

* Work on getting multiple sensors working (responsibility: GA)
* Work on setting up ESP8266 soft access point for user configuration (responsibility: GA)
* Trend line? (responsibility: GA)
