# install mosquitto
sudo apt install -y mosquitto mosquitto-clients
echo "allow_anonymous true" | sudo tee --append /etc/mosquitto/mosquitto.conf
echo "listener 1883" | sudo tee --append /etc/mosquitto/mosquitto.conf
sudo systemctl enable mosquitto.service
sudo systemctl start mosquitto


# install mongodb
# curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
# echo "deb https://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
# sudo apt update
# sudo apt install -y mongodb-org
# sudo systemctl start mongod