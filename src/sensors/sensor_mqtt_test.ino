#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <ESP8266WiFi.h>
#include <Ticker.h>
#include <AsyncMqttClient.h>
#include <ArduinoJson.h>

// wifi settings
#define WIFI_SSID "YOUR SSID HERE"
#define WIFI_PASSWORD "YOUR PASSWORD HERE"
WiFiEventHandler wifiConnectHandler;
WiFiEventHandler wifiDisconnectHandler;
Ticker wifiReconnectTimer;

// raspberry pi mosquitto mqtt broker
#define MQTT_HOST "MQTT ADDRESS HERE"
#define MQTT_PORT 1883
#define MQTT_PUB_NAME "SENSOR NAME HERE"
AsyncMqttClient mqttClient;
Ticker mqttReconnectTimer;

// BME280 I2C
Adafruit_BME280 bme;

// timing cycle information
unsigned long previousMillis = 0;  
const long interval = 25000;       

void onWifiConnect(const WiFiEventStationModeGotIP& event) {
  Serial.println("Connected to Wi-Fi.");
  mqttClient.connect();
}

void onMqttConnect(bool sessionPresent) {
  Serial.println("Connected to MQTT.");
}

void onMqttPublish(uint16_t packetId) {
  Serial.print("\npub ack\n");
}

// custom sensor readings structure
struct sensorReadings {
  float temp;
  float humd;
};

// Comtake averaged sensor readings
struct sensorReadings getAverages() {

  struct sensorReadings readings;
  float total_temp, total_humd = 0;

  // take 20 readings .25 seconds apart (over the course of 5sec)
  for (int i = 0; i < 20; i++) {
    float current_temp = bme.readTemperature();
    float current_humd = bme.readHumidity();

    total_temp += current_temp;
    total_humd += current_humd;
    delay(250);
  }

  // average temp and humd readings
  readings.temp = (total_temp/20);
  readings.humd = (total_humd/20);

  return readings;
}


/*********************************
SETUP
*********************************/
void setup() {
  Serial.begin(9600);
  Serial.println();

  // Initialize BME280 sensor
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  wifiConnectHandler = WiFi.onStationModeGotIP(onWifiConnect);
  mqttClient.onConnect(onMqttConnect);
  mqttClient.onPublish(onMqttPublish);
  mqttClient.setServer(MQTT_HOST, MQTT_PORT);
  mqttClient.setCredentials("", "");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
}


/*********************************
MAIN LOOP
*********************************/
void loop() {
  char output[100];
  unsigned long currentMillis = millis();
  // Every X number of seconds (interval = 10 seconds)
  // it publishes a new MQTT message
  if (currentMillis - previousMillis >= interval) {
    // Save the last time a new reading was published
    previousMillis = currentMillis;

    Serial.begin(9600);

    struct sensorReadings averages;
    averages = getAverages();

    // prepare JSON to publish
    StaticJsonDocument<100> payload;
    payload["sensor"] = MQTT_PUB_NAME;
    payload["temp"] = averages.temp;
    payload["humd"] = averages.humd;
    serializeJson(payload, output);
    serializeJsonPretty(payload, Serial);

    uint16_t packetIdPub = mqttClient.publish(MQTT_PUB_NAME, 1, true, output);
  }
}