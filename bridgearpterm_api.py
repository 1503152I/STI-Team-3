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


@app.route('/todo/api/v1.0/tasks/', methods=['PUT'])
@auth.login_required
def update_task():
	if not request.json or not 'ID' in request.json:
		abort(400)
	if not request.json or not 'disable' in request.json:
		abort(400)

	ID = str(request.json['ID'])
	disable = str(request.json['disable'])
	update = "sudo vppctl set bridge-domain arp term %s %s" % (ID, disable)
	sub = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
	output= sub.communicate()[0]

	nupdate= "sudo vppctl show bridge"
	nsub= subprocess.Popen(nupdate,shell=True,stdout=subprocess.PIPE)
	nresults = nsub.communicate()[0]
	ntask = nresults
	
	return ntask

if __name__ == '__main__':
        app.run(debug=True)

