#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

child = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
def READ():

	#Updating JSON File & Flask Item Table
	updatejson = "python this.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks', methods=['POST'])
def CREATE():
	 
        addintf = 'sudo vppctl create loopback interface'
        subprocess.call(addintf,shell=True)

	return ''
	
@app.route('/vpp/tasks', methods=['DELETE'])
def DELETE():

	if not request.json or not 'Name' in request.json:
		abort(400)

	task = { 'Name': request.json['Name'] }

	LBintf = str(request.json['Name'])
	deleteintf = 'sudo vppctl delete loopback interface intfc %s' % (LBintf)
	subprocess.call(deleteintf, shell=True)

	return ''

@app.route('/vpp/tasks', methods=['UPDATE'])
def UPDATEflood():

	if not request.json or not 'Flooding' in request.json:
		abort(400)

	task = {'Flooding': request.json['Flooding'] }

	bridge = str(request.json['Flooding'])
	update = 'sudo vppctl set bridge-domain flood %s' % (bridge)
	subprocess.call(update,stdout=subprocess.PIPE, shell=True)
	
	#Updating JSON File & Flask Item Table	
	updatejson = "python this.py"
	subprocess.call(updatejson, shell=True)
	updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
	updatedoutput = updatedchild.communicate()[0]
	tasks = updatedoutput

	return tasks


if __name__ == '__main__':
	app.run(debug=True)