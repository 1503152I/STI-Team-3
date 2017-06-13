#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

child = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['POST'])
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