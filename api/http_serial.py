"""
API REST ARDUINO

Developer : Abel Laaouaj (12-5-2023)

Notes: 
# La funció jsonify() és una funció de Flask que s'utilitza per convertir objectes Python en respostes JSON.
# request.method és una variable de Flask que representa el mètode HTTP utilitzat a la sol·licitud HTTP rebuda pel servidor.
# request.json.get() s'utilitza per extreure valors d'objectes JSON continguts a les sol·licituds HTTP.    
"""

from flask import Flask, jsonify, request
import serial
from serial.tools import list_ports
from datetime import datetime
import time

app = Flask(__name__) # Punt de partida per crear una aplicació web amb flask 
arduino = None

def connect_arduino():
    global arduino
    try:
        ports = list_ports.comports()
        for port in ports:
            if port.device.startswith('/dev/ttyACM'):
                arduino = serial.Serial(port.device, 9600)
                print("Arduino connected on", port.device)
                time.sleep(2)
    except serial.SerialException:
        arduino = None
        print("Arduino not connected")

@app.before_first_request
def setup():
    connect_arduino()

@app.route('/led', methods=['GET', 'PUT'])
def led():
    global arduino
    if arduino is None:
        connect_arduino()
        return 'Arduino not connected', 503
        
    if request.method == 'GET':
        try:
            arduino.write(b'%L?')
            response = arduino.readline().strip().decode()
            value = int(response[-1]) # Tenint en compte que la resposta de l'arduino és '%0/1'
            return jsonify({
                'led': value 
            })
        except serial.SerialException:
            connect_arduino()
            return 'Arduino not connected', 503
    
    elif request.method == 'PUT':
        state = request.json.get('led') # Suposant que la request és 'led:0/1'
        if state is None:
            return 'Missing parameter', 400
        if str(state) not in ['0', '1']:
            return 'Invalid parameter', 400
        try:
            arduino.write(f'%L{state}\n'.encode())
            arduino.readline() # Si l'arduino m'envia alguna cosa l'he de llegir tot, netejant el buffer, i l'ignoro.
            return '', 204
        except serial.SerialException:
            connect_arduino()
            return 'Arduino not connected', 503

@app.route('/potenciometre')
def potentiometer():
    global arduino
    if arduino is None:
        connect_arduino()
        return 'Arduino not connected', 503
    try:
        arduino.write(b'%P?')
        response = arduino.readline().strip().decode()
        value = int(response[1:]) # Suposant que la resposta de l'arduino és '%XXX'
        return jsonify({
            'potenciometre': value
        })
    except:
        connect_arduino()
        return 'Arduino not connected', 503

if __name__ == '__main__':
    app.run(port=5001)



