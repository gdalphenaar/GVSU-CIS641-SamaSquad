## Meeting minutes

Team name: Sama Squad

Members present: Grant Alphenaar (GA)

Date: Sunday, Nov. 20, 2022

Time: Noon

Discussion points:

* Full(?) flow from sensor to database is complete:
    * Finalized JSON format
    * Database properly connecting to all relevant services
    * (As expected), database works with simulated sensor data as well

<br>

* Cleaned up sensor code quite a bit
    * Not an Arduino/C++ expert, so it's a bit messy and probably a bit inefficient

<br>

Goals for next week (include responsibilities):

* Work on getting multiple sensors working
* Work on setting up ESP8266 soft access point for user configuration
* Find the best way to get the "recent readings" average - preferably without needing a second database table
