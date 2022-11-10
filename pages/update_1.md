title: pub/sub update
short-title: pub/sub update
date: 2022-11-05
published:

in the first substantive update here, I...

* set up a basic debian virtual machine for testing

* connected the bme280 to my wireless network using the esp8266 wireless board

* got the bme280 publishing on a topic

* installed mosquitto mqtt on the virtual machine

* installed Node-RED and set up an incredibly rudimentary dashboard

below, I have some prototype dashboard views. note that these are absolutely nowhere near final, and the final dashboard won't be built using Node-RED - this is just for quick-and-dirty testing purposes. part of the choice of Node-RED is that it's highly compatible with raspberry pi units (and makes dashboard creation super easy with its drag-and-drop interface), making some testing on the actual hardware (coming soon tm) a bit easier.

here we can see the Node-RED dashboard in a desktop browser:

![dashboard-desktop]({{ url_for('static', filename='images/test-dashboard.png') }})

and here - just to verify that the final dashboard will be viewable on any (most) device on the local network, here it is in a phone browser:

![dashboard-mobile]({{ url_for('static', filename='images/dashboard-mobile.png') }})