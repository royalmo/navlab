"""
API REST DATABASE

Api que permet accedir a la base de dades per llegir i escriure dades a la taula mostres per protocol http.
"""

import sqlite3
from flask import Flask, Response, request, jsonify
import os
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(CURRENT_DIR, '..', 'app', 'navlab.db')

app=Flask(__name__)

@app.route('/led',methods=['GET'])
def get_led_data():
	"""
	Retorna les n dades mes recents del led.
	n es pot especificar a la request i, en cas contrari n=1. 
	"""
	n_max=500
	r=request.json
	try:
		n=r['values']
	except: 
		n=1
	if type(n)!=int:
		return Response(status=400)
	if n>n_max:
		response=jsonify({'values_limit': n_max})
		response.status_code = 416
		return response
	conn = sqlite3.connect(DATABASE_PATH)
	select=conn.execute(f"select date, value from sample where monitor_key='led' order by date DESC limit {n};").fetchall()
	conn.close()
	s=[{'time':e[0],'led':e[1]} for e in select]
	return jsonify(s)

@app.route('/potenciometre',methods=['GET'])
def get_potenciometre_data():
	"""
	Retorna les n dades mes recents del potenciòmetre.
	n es pot especificar a la request i, en cas contrari n=1. 
	"""

	n_max=500
	r=request.json
	try:
		n=r['values']
	except: 
		n=1
	if type(n)!=int:
		return Response(status=400)
	if n>n_max:
		response=jsonify({'values_limit': n_max})
		response.status_code = 416
		return response
	conn = sqlite3.connect(DATABASE_PATH)
	select=conn.execute(f"select date, value from sample where monitor_key='potenciometre' order by date DESC limit {n};").fetchall()
	conn.close()
	s=[{'time':e[0],'potenciometre':e[1]} for e in select]
	return jsonify(s)

@app.route('/led',methods=["POST"])
def input_led():
	"""
	Guarda un valor del led a la base de dades. 
	Com a paràmetres de la request ha de rebre la representació en string d'un objecte datetime i un valor string de '0' o '1'.
	"""
	if not os.path.isfile(DATABASE_PATH):
		return Response(status=503)
	try:
		r=request.json
		value=str(r['led'])
		time=r['time']
		if not (value=='1' or value=='0'):
			return Response(status=400)
		formatted_time=datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').strftime("%Y-%m-%d %H:%M:%S")
	except : #json invalid or datetime invalid
		return Response(status=400)
	conn = sqlite3.connect(DATABASE_PATH)
	conn.execute(f"insert into sample (monitor_key, date, value) values('led','{formatted_time}','{value}');") 
	conn.commit()
	conn.close()
	return Response(status=204)


@app.route('/potenciometre',methods=["POST"])
def input_potenciometre():
	"""
	Guarda un valor del potenciòmetre a la base de dades.
	Com a paràmetres de la request ha de rebre la representació en string d'un objecte datetime i un valor int entre 0 i 255.
	"""
	if not os.path.isfile(DATABASE_PATH):
		return Response(status=503)
	try:
		r=request.json
		value=int(r['potenciometre'])
		time=r['time']
		if not (value>=0 and value<=255):
			return Response(status=400)
		formatted_time=datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').strftime("%Y-%m-%d %H:%M:%S")
	except : #json invalid or datetime invalid
		return Response(status=400)
	conn = sqlite3.connect(DATABASE_PATH)
	conn.execute(f"insert into sample (monitor_key, date, value) values('potenciometre','{formatted_time}','{value}');")
	conn.commit()
	conn.close()
	return Response(status=204)


if __name__=="__main__":
	app.run(port=5002)

