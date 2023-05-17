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
from datetime import datetime


app = Flask(__name__) # Punt de partida per crear una aplicació web amb flask 

arduino = serial.Serial('/dev/ttyUSB0', 9600)


@app.route('/led', methods=['GET', 'PUT'])
def led():
    if not arduino.isOpen():
        return 'Arduino not connected', 503
    
    if request.method == 'GET':
        arduino.write(b'%L?')
        response = arduino.readline().strip().decode()
        value = int(response[-1]) # Tenint en compte que la resposta de l'arduino és '%0/1'
        return jsonify({
            'led': value 
        })
    
    elif request.method == 'PUT':
        state = request.json.get('led') # Suposant que la request és 'led:0/1'
        if state is None:
            return 'Missing parameter', 400
        if state not in ['0', '1']:
            return 'Invalid parameter', 400
        arduino.write(f'%L{state}\n'.encode())
        arduino.readline() # Si l'arduino m'envia alguna cosa l'he de llegir tot, netejant el buffer, i l'ignoro.
        return '', 204

@app.route('/potentiometer')
def potentiometer():
    if not arduino.isOpen():
        return 'Arduino not connected', 503
    
    arduino.write(b'%P?')
    response = arduino.readline().strip().decode()
    value = int(response[1:]) # Suposant que la resposta de l'arduino és '%XXXX'
    return jsonify({
        'potentiometer': value
    })

if __name__ == '__main__':
    app.run()

