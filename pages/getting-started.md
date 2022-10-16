title: getting started and gathering the essentials
short-title: getting started
date: 2022-10-10
published:

here, I'm getting a few of the necessary components together for this project.

first up, the raspberry pi itself - at some point, I would maybe like to get a nicer case for this, but since it's just serving as the base unit and web server, it can just be tucked away next to my router and doesn't *really* need a case.

![Raspberry Pi]({{ url_for('static', filename='images/rpi.png') }})

next, we have the bme280 sensor and a WiFi board - this will serve as the "main" component of the system, as it's the thing that's responsible for getting the temperature and humidity readings.

![BME280]({{ url_for('static', filename='images/bme.png') }})

last up, we have a board that's capable of battery power - I'm not sure how necessary this is (the bme280 and board can also be powered through micro usb), but it could be cool to enable battery power as well. in fairness, there's no way I'll be able to get my sensor units down to the tiny size that some of the commercial guitar sensors are, but battery power could still be interesting to get working.

![Battery Board]({{ url_for('static', filename='images/battery.png') }})
