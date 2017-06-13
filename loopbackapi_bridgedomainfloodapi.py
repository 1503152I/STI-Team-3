#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, url_for
import subprocess
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

child = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
@app.login_required
def READ():

	#Updating JSON File & Flask Item Table
	updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks', methods=['POST'])
@app.login_required
def CREATE():
	 
        addintf = 'sudo vppctl create loopback interface'
        subprocess.call(addintf,shell=True)

	return ''
	
@app.route('/vpp/tasks', methods=['DELETE'])
@app.login_required
def DELETE():

	if not request.json or not 'Name' in request.json:
		abort(400)

	task = { 'Name': request.json['Name'] }

	LBintf = str(request.json['Name'])
	deleteintf = 'sudo vppctl delete loopback interface intfc %s' % (LBintf)
	subprocess.call(deleteintf, shell=True)

	return ''

@app.route('/vpp/tasks', methods=['PUT'])
@app.login_required
def UPDATEflood():

	if not request.json or not 'Flooding' in request.json:
		abort(400)

	task = {'Flooding': request.json['Flooding'] }

	bridge = str(request.json['Flooding'])
	update = 'sudo vppctl set bridge-domain flood %s' % (bridge)
	subprocess.call(update,stdout=subprocess.PIPE, shell=True)
	
	#Updating JSON File & Flask Item Table	
	updatejson = "python showbridgedomain.py"
	subprocess.call(updatejson, shell=True)
	updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
	updatedoutput = updatedchild.communicate()[0]
	tasks = updatedoutput

	return tasks


if __name__ == '__main__':
	app.run(debug=True)
