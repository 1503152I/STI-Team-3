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

sub = subprocess.Popen('cat readresults2.json',stdout=subprocess.PIPE,shell=True)
results = sub.communicate()[0]

tasks = results

@app.route('/todo/api/v1.0/jobs/', methods=['GET'])
@auth.login_required
def get_tasks():
	return tasks

if __name__ == '__main__':
	app.run(debug=True)
