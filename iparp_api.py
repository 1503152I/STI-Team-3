#!flask/bin/python
from flask import Flask,jsonify,abort,request,make_response
from flask.ext.httpauth import HTTPBasicAuth
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'sti':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify( { 'error': 'Unauthorized Access' } ), 403)


sub = subprocess.Popen('cat readresults.json',stdout=subprocess.PIPE,shell=True)
results = sub.communicate()[0]

tasks = results

@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
@auth.login_required
def get_tasks():
	return tasks

@app.route('/todo/api/v1.0/tasks/', methods=['POST'])
@auth.login_required
def create_tasks():
	task = {
		'Flags': request.json['Flags'],
		'IP4': request.json['IP4'],
		'Interface': request.json['Interface'],
		'Ethernet': request.json['Ethernet']
	}
	flag= str(request.json['Flags'])
	ipaddr= str(request.json['IP4'])
	interface= str(request.json['Interface'])
	eth= str(request.json['Ethernet'])

	insert= "sudo vppctl set ip arp %s %s %s %s" % (flag, interface, ipaddr, eth)
	csub= subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
	coutput= csub.communicate()[0]

	cupdate= "python showiparp.py"
	subprocess.call(cupdate,shell=True)

	nsub= subprocess.Popen('cat readresults.json',stdout=subprocess.PIPE,shell=True)
	newresults= nsub.communicate()[0]
	newtasks = newresults

	return newtasks

@app.route('/todo/api/v1.0/tasks/', methods=['DELETE'])
@auth.login_required
def del_task():
	task = {
		'Flags': request.json['Flags'],
		'IP4': request.json['IP4'],
		'Interface': request.json['Interface'],
		'Ethernet': request.json['Ethernet'] 
	}

	flag= str(request.json['Flags'])
	ipaddr= str(request.json['IP4'])
	interface= str(request.json['Interface'])
	eth= str(request.json['Ethernet'])

	delete= "sudo vppctl set ip arp %s delete %s %s %s" % (flag, interface, ipaddr, eth)
	dsub = subprocess.Popen(delete,shell=True,stdout=subprocess.PIPE)
	doutput= dsub.communicate()[0]

	dupdate= "python showiparp.py"
	subprocess.call(dupdate,shell=True)

	nsub= subprocess.Popen('cat readresults.json',stdout=subprocess.PIPE,shell=True)
	newresults= nsub.communicate()[0]
	newtasks = newresults

	return newtasks

if __name__ == '__main__':
	app.run(debug=True)
