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

@auth.error_handler(403)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.route('/vpp/tasks', methods=['POST'])
@app.login_required
def CREATE():
	
	if not request.json or not 'local' in request.json:
		abort(400)
	if not  request.json or not 'remote' in request.json:
		abort(400)
	if not request.json or not 'nn' in request.json:
		abort(400)
	
	task = { 'local': request.json['local'], 'remote': request.json['remote'], 'nn': request.json['nn'] }

	local = str(request.json['local'])
	remote = str(request.json['remote'])
	nn = str(request.json['nn'])

        vxlan = 'sudo vppctl create vxlan tunnel src %s dst %s vni %s' % (local, remote, nn)
        subprocess.call(vxlan,shell=True)

	return ''
	
@app.route('/vpp/tasks', methods=['DELETE'])
@app.login_required
def DELETE():

        if not request.json or not 'local' in request.json:
                abort(400)
        if not  request.json or not 'remote' in request.json:
                abort(400)
        if not request.json or not 'nn' in request.json:
                abort(400)

        task = { 'local': request.json['local'], 'remote': request.json['remote'], 'nn': request.json['nn'] }

        local = str(request.json['local'])
        remote = str(request.json['remote'])
        nn = str(request.json['nn'])

	deletevxlan = 'sudo vppctl create vxlan tunnel src %s dst %s vni %s del' % (local, remote, nn)
	subprocess.call(deletevxlan, shell=True)

	return ''



if __name__ == '__main__':
	app.run(debug=True)
