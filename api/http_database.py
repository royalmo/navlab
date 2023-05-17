import sqlite3
from flask import Flask, Response, request, jsonify
import os
from datetime import datetime

DATABASE_PATH='../app/database.bd'

app=Flask(__name__)

@app.route('/status',methods=['GET'])
def status():
	return {'database_available':os.path.isfile(DATABASE_PATH),'server_time':datetime.now()}


@app.route('/data',methods=['GET'])
def get_data():
	if not os.path.isfile(DATABASE_PATH):
		return Response(status=503)
	conn = sqlite3.connect(DATABASE_PATH)
	data=conn.execute(f"select * from mostres").fetchall()
	return jsonify(data)


@app.route('/led',methods=["POST"])
def input_led():
	if not os.path.isfile(DATABASE_PATH):
		return Response(status=503)
	try:
		r=request.json
		value=r['led']
		time=r['time']
		if not (value=='1' or value=='0'):
			return Response(status=400)
		datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
	except : #json invalid or datetime invalid
		return Response(status=400)
	conn = sqlite3.connect(DATABASE_PATH)
	conn.execute(f"insert into mostres values('led','{time}','{value}');") #el trigger fa saltar exception
	conn.commit()
	conn.close()
	return Response(status=204)


@app.route('/potenciometre',methods=["POST"])
def input_potenciometre():
	if not os.path.isfile(DATABASE_PATH):
		return Response(status=503)
	try:
		r=request.json
		value=r['potenciometre']
		time=r['time']
		print(type(value))
		if not (value>=0 and value<=1024):
			return Response(status=400)
		datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
	except : #json invalid or datetime invalid
		return Response(status=400)
	conn = sqlite3.connect(DATABASE_PATH)
	conn.execute(f"insert into mostres values('potenciometre','{time}','{value}');") #el trigger fa saltar exception
	conn.commit()
	conn.close()
	return Response(status=204)


if __name__=="__main__":
	app.run(host="0.0.0.0",port='8000',debug=True)
