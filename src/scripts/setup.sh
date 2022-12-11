# install mosquitto
sudo apt install -y mosquitto mosquitto-clients
echo "\n" | sudo tee --append /etc/mosquitto/mosquitto.conf
echo "allow_anonymous true" | sudo tee --append /etc/mosquitto/mosquitto.conf
echo "listener 1883" | sudo tee --append /etc/mosquitto/mosquitto.conf
sudo systemctl enable mosquitto.service
sudo systemctl start mosquitto

# start flask site
cd ../flask-site
python3 -m venv flask-site
source flask-site/bin/activate
pip install -r requirements.txt
python3 app.py &