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

@app.route('/todo/api/v1.0/jobs/', methods=['POST'])
@auth.login_required
def create_tasks():
	if not request.json or not 'src' in request.json:
		abort(400)
	if not request.json or not 'dst' in request.json:
		abort(400)

	csource= str(request.json['src'])
	cdestination= str(request.json['dst'])
	insert = "sudo vppctl create gre tunnel src %s dst %s" % (csource, cdestination)
	csub = subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
	coutput = csub.communicate()[0]
	
	return ''

@app.route('/todo/api/v1.0/jobs/', methods=['DELETE'])
@auth.login_required
def del_tasks():
	if not request.json or not 'src' in request.json:
		abort(400)
	if not request.json or not 'dst' in request.json:
		abort(400)

	dsource= str(request.json['src'])
	ddestination= str(request.json['dst'])
	delete= "sudo vppctl create gre tunnel src %s dst %s del" % (dsource, ddestination)
	dsub = subprocess.Popen(delete,shell=True,stdout=subprocess.PIPE)
	doutput = dsub.communicate()[0]

        return ''

if __name__ == '__main__':
	app.run(debug=True)
