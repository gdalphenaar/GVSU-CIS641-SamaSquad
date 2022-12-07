# based on the Flask-MQTT example: https://flask-mqtt.readthedocs.io/en/latest/usage.html#interact-with-socketio


import logging, eventlet, json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = '192.168.1.77'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLEAN_SESSION'] = True
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_TLS_ENABLED'] = False


eventlet.monkey_patch()
mqtt = Mqtt(app)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    sensors = ['sensor/sensor77', 'sensor/sensor01']
    return render_template('index.html',sensors=sensors)


# handle new topic/sensor subscription
@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'], data['qos'])


# reset and unsubscribe to all
@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


# if server is shut down or mqtt connection lost, resubscribe on mwtt (re)connect
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    sensors = ['sensor/sensor77', 'sensor/sensor01']
    for sensor in sensors:
        mqtt.subscribe(sensor)


# send new mqtt message through socket
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode(),
        qos=message.qos,
    )
    socketio.emit('mqtt_message', data=data)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, use_reloader=False, debug=True)
