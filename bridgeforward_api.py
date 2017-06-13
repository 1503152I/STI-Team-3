#!flask/bin/python
from flask import Flask,jsonify,abort,request, make_response
from flask.ext.httpauth import HTTPBasicAuth
import subprocess,os,json

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'sti':
        return 'password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

app = Flask(__name__)

@app.route('/todo/bridge', methods=['UPDATE'])
@auth.login_required
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


