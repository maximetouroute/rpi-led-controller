from flask import Flask
from flask import request






import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def shutdownLeds(strip):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, 0)
            strip.show()

def singleColor(strip, color):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
        

# MAIN CODE


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

app = Flask("MAXIME")



@app.route('/')
def routeHello():

        rainbow(strip, 20, 1)
	return "Hello World!"

@app.route('/shut')
def routeShutdown():
        shutdownLeds(strip)
	return "Success shutting down"

@app.route('/single/red')
def routeRed():
        singleColor(strip, Color(0,100,0))
	return "Success"

@app.route('/single/green')
def routeG():
        singleColor(strip, Color(10,10,0))
	return "Success"

@app.route('/single/blue')
def routeB():
        singleColor(strip, Color(0,0,100))
	return "Success"

@app.route('/colorControl', methods=['POST'])
def routeColorControl():
        print("COLOR CONTROL")
        print (request.is_json)
        j = request.get_json()
        print(j['green'])
        print(j['red'])
        print(j['blue'])
        print("ho")
        print(j)
        singleColor(strip, Color(int(j['green']), int(j['red']), int(j['blue'])))
        return "Success"



