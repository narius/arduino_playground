# This is a small flask page to turn on and off leds
import serial
from flask import Flask
from flask import render_template
import serial
import code
import io
import time

ser = serial.Serial('/dev/cu.usbserial-1410', timeout=10, baudrate=9600)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/ledBlue_on')
def ledBlue_on():
    ser.write(b'blue_on')
    return render_template('hello.html')

@app.route('/ledBlue_off')
def ledBlue_off():
    ser.write(b'blue_off')
    return render_template('hello.html')
