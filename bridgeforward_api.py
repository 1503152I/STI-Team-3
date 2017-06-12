#!flask/bin/python
from flask import Flask,jsonify,abort,request
import subprocess,os,json

app = Flask(__name__)

@app.route('/todo/bridge', methods=['UPDATE'])
def update_bridge_forward():
	
	if not request.json or not 'State' in request.json:
		abort(400)
	if not request.json or not 'ID' in request.json:
		abort(400)
	
	BRIDGEID = int(request.json['ID'])
	UPDATEBRIDGE = str(request.json['State'])
        addintf = 'sudo vppctl set bridge-domain forward %i %s' % (BRIDGEID, UPDATEBRIDGE)
	subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

	return ''

if __name__== '__main__':
	app.run(debug=True)


