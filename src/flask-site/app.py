# based on the Flask-MQTT example: https://flask-mqtt.readthedocs.io/en/latest/usage.html#interact-with-socketio


import logging, eventlet, json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from datetime import datetime


app = Flask(__name__)
app.config['SECRET'] = 'sama'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = '0.0.0.0'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLEAN_SESSION'] = True
app.config['MQTT_KEEPALIVE'] = 30
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_TLS_ENABLED'] = False


eventlet.monkey_patch()
mqtt = Mqtt(app)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@app.route('/')
def index():

    # load settings from config
    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)

    return render_template('index.html',
        sensors=settings['sensors'],
        cpt_temp=settings['cutpoints_temp'],
        cpt_humd=settings['cutpoints_humd'],
        unit=settings["unit"],
        current_temp = current_temp,
        current_humd = current_humd
    )


@app.route('/settings')
def settings():

    # load settings to show on page
    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)

    return render_template(
        'settings.html',
        cpt_temp = settings['cutpoints_temp'],
        cpt_humd = settings['cutpoints_humd'],
        unit     = settings['unit']
    )


@app.route('/manage')
def add():

    # read sensors from settings
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
        settings = json.loads(data)
        sensors  = settings['sensors']

    return render_template('manage.html', sensors=sensors)


# handle new topic/sensor subscription
@socketio.on('subscribe')
def handle_subscribe(json_str):

    # get new sensor from socket.io message
    new_sensor = json.loads(str(json_str))

    # load sensors list settings.json
    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)
        sensors  = settings['sensors']

    # add new sensor
    sensors.append(new_sensor)
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)

    mqtt.subscribe(new_sensor['id'])


# set humidity cutpoints
@socketio.on('set_humd_cpt')
def set_humd_ctp(msg):

    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)

    settings['cutpoints_humd'] = json.loads(str(msg))

    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)


# set temperature cutpoints
@socketio.on('set_temp_cpt')
def set_temp_cpt(msg):

    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)

    settings['cutpoints_temp'] = json.loads(str(msg))

    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)


# change temperature units
@socketio.on('change_unit')
def change_units(unit):

    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)

    settings['unit'] = unit

    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)


# reset and unsubscribe to all
@socketio.on('unsubscribe')
def handle_unsubscribe(sensor):

    # load sensors list settings.json
    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)
        sensors  = settings['sensors']

    # remove matching sensor
    for i in range(len(sensors)):
        if sensors[i]['id'] == sensor:
            sensors.remove(sensors[i])
            break

    # save settings
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=2)

    # and unsubscribe
    mqtt.unsubscribe(sensor)


# if server is shut down or mqtt connection lost, resubscribe on mqtt (re)connect
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):

    # load and subscribe to sensors on initial connection to mqtt
    with open('settings.json', 'r') as file:
        data = file.read()
        settings = json.loads(data)
        sensors  = settings['sensors']
    for sensor in sensors:
        mqtt.subscribe(sensor['id'], 2)

    # global variables for current temp and humidity
    global current_temp
    global current_humd
    current_temp = dict()
    current_humd = dict()

    # start off NA
    for sensor in sensors:
        current_temp[sensor['id']] = 'N/A'
        current_humd[sensor['id']] = 'N/A'


# send new mqtt message through socket
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

    # fill current temp / humidity with most recent value
    current_temp[data['topic']] = round(json.loads(data['payload'])['temp'], 1)
    current_humd[data['topic']] = round(json.loads(data['payload'])['humd'], 1)
    socketio.emit('mqtt_message', data=data)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, use_reloader=False, debug=False)
    # socketio.run(app, host='0.0.0.0', port=8080, use_reloader=False, debug=True)
