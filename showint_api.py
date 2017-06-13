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

child = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	
	#Update the json file
	updatejsonfile = "python showinterface.py"
	subprocess.call(updatejsonfile, shell = True)

	#Update the flask item table
	newchild = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
	newoutput = newchild.communicate()[0]
	tasks = newoutput

	return tasks

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():
	
	if not request.json or not 'Name' in request.json:
		abort(400)

	task = {
		'Name': request.json['Name']
	}

	HOSTINTF = str(request.json['Name'])
	addintf = 'sudo vppctl create host-interface name %s' % (HOSTINTF)
	subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

	#Update the json file
        updatejsonfile = "python showinterface.py"
        subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks = newoutput

	return ''

@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def delete_task():

        if not request.json or not 'Name' in request.json:
                abort(400)

        task = {
                'Name': request.json['Name']
        }

        HOSTINTF = str(request.json['Name'])
        deleteintf = 'sudo vppctl delete host-interface name %s' % (HOSTINTF)
        subprocess.call(deleteintf,stdout=subprocess.PIPE, shell = True)

        #Update the json file
        updatejsonfile = "python showinterface.py"
        subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks = newoutput

        return ''

@app.route('/todo/api/v1.0/tasks', methods=['UPDATE'])
@auth.login_required
def update_task():

        if not request.json or not 'Name' in request.json:
                abort(400)
	if not request.json or not 'State' in request.json:
                abort(400)

        task = {
                'Name': request.json['Name'],
		'State': request.json['State']
        }

        HOSTINTF = str(request.json['Name'])
	STATEINTF = str(request.json['State'])
        updateintf = 'sudo vppctl set interface state %s %s' % (HOSTINTF, STATEINTF)
        subprocess.call(updateintf,stdout=subprocess.PIPE, shell = True)

        #Update the json file
        updatejsonfile = "python showinterface.py"
        subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks = newoutput

        return ''


if __name__== '__main__':
	app.run(debug=True)
