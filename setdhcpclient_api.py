#!flask/bin/python
from flask import Flask,jsonify,abort,request
import subprocess,os,json

app = Flask(__name__)

@app.route('/todo/dhcp', methods=['POST'])
def create_dhcpclient():
	
	if not request.json or not 'Interface' in request.json:
		abort(400)

	DHCPINT = str(request.json['Interface'])
        addintf = 'sudo vppctl set dhcp client intfc %s' % (DHCPINT)
	subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

	return ''

@app.route('/todo/dhcp', methods=['DELETE'])
def delete_dhcpclient():

        if not request.json or not 'Interface' in request.json:
                abort(400)
	if not request.json or not 'Delete' in request.json:
                abort(400)

        DHCPINT = str(request.json['Interface'])
	DELETEINT = str(request.json['Delete'])
        addintf = 'sudo vppctl set dhcp client %s intfc %s' % (DELETEINT, DHCPINT)
        subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

        return ''

if __name__== '__main__':
	app.run(debug=True)
