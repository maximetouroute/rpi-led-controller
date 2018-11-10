# RPI LED CONTROLLER
* Some code to control the leds
* Some code to control it from a local network via HTTP or OSC?


## How to run
sudo FLASK_APP=flasktest.py flask run --host=0.0.0.0


## FLASK
pip install flask

## Python lib
We need to use python 2.7
* flask seems to use python3 by default but doc says it works with python2
* so rm-rf /usr/bin/python3*
* ln -sf /usr/bin/python3 /usr/bin/python2.7
* yeah, that's not really great but it works for now

### Python osc
pip install will install with python 2 so you need to install manually
* git clone github.com/attwad/python-osc/
* run py setup.py test and sudo py setup.py install (IN sudo -s ! so add the alias to bashrc of root user

# LED_Stripe python
- Tutoriel trouvé sur le site *core-electronics*
- Branchements : Le fil vert sur le GPIO 18, le fil rouge sur le 5V et le fil blanc sur GND 
