title: mongodb update
short-title: mongodb update
date: 2022-11-17
published:

after tinkering around with things a bit more, I decided to publish the data from the bme280 sensor as a single json file rather than as separate temperature and humidity readings.

this is somewhat advantageous for two main reasons:

* it lets me publish on only one topic, rather than needing two topics (temperature and humidity) per sensor - I haven't gotten around to it quite yet, but this should make adding additional sensors a bit easier

* it keeps the data in json format for easy insertion into a mongodb database, where it can be done in one insert, rather than requiring either two rows in sqlite or multiple pre-operations to get the query ready

I was initially considering using a lightweight sqlite database for data storage here, but I think mongodb might be a slightly better option, and upon further consideration, the "fast and loose" nature of mongodb might work better with streamed data like from a sensor, as the schemaless design is resilient to data missingness or corruption.

here we can see the streamed messages from the bme280 via the esp8266 as they are received:

![dashboard-desktop]({{ url_for('static', filename='images/published-json.png') }})

and here we can see the records in mongodb:

![dashboard-mobile]({{ url_for('static', filename='images/in-mongodb.png') }})