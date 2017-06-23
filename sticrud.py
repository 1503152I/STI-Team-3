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

#########################################################################################

#YIU WAI LEONG's crud

child1 = subprocess.Popen('cat showbuffer/showbuffer.json', stdout=subprocess.PIPE,shell=True)
output1 = child1.communicate()[0]

tasks1 = output1

@app.route('/todo/showbuffer', methods=['GET'])
@auth.login_required
def get_showbuffer():

        #Update the json file
        updatejsonfile = "python /home/sti/api-dev/showbuffer/showbuffer.py"
	subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showbuffer/showbuffer.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks1 = newoutput

        return tasks1

@app.route('/todo/updatebridge', methods=['UPDATE'])
@auth.login_required
def update_bridge_forward():

        if not request.json or not 'State' in request.json:
                abort(400)
        if not request.json or not 'ID' in request.json:
                abort(400)

        BRIDGEID = int(request.json['ID'])
        UPDATEBRIDGE = str(request.json['State'])

	if UPDATEBRIDGE == "enable":
		UPDATEBRIDGE == ""

        addintf = 'sudo vppctl set bridge-domain forward %i %s' % (BRIDGEID, UPDATEBRIDGE)
        subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

	#Output the result of the update i.e. show bridge
	childsp = subprocess.Popen('sudo vppctl show bridge', stdout=subprocess.PIPE, shell = True)
	childoutput = childsp.communicate()[0]
	showbridgedomain = childoutput

        return showbridgedomain

@app.route('/todo/createdhcp', methods=['POST'])
@auth.login_required
def create_dhcpclient():

        if not request.json or not 'Interface' in request.json:
                abort(400)

        DHCPINT = str(request.json['Interface'])
        addintf = 'sudo vppctl set dhcp client intfc %s' % (DHCPINT)
        subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

	childsp = subprocess.Popen('sudo vppctl show dhcp client', stdout=subprocess.PIPE, shell = True)
	childoutput = childsp.communicate()[0]
	showdhcpclient = childoutput

        return showdhcpclient

@app.route('/todo/deletedhcp', methods=['DELETE'])
@auth.login_required
def delete_dhcpclient():

        if not request.json or not 'Interface' in request.json:
                abort(400)
        if not request.json or not 'Delete' in request.json:
                abort(400)

        DHCPINT = str(request.json['Interface'])
        DELETEINT = str(request.json['Delete'])
        addintf = 'sudo vppctl set dhcp client %s intfc %s' % (DELETEINT, DHCPINT)
        subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)

        childsp = subprocess.Popen('sudo vppctl show dhcp client', stdout=subprocess.PIPE, shell = True)
        childoutput = childsp.communicate()[0]
        showdhcpclient = childoutput

        return showdhcpclient

child2 = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
output2 = child2.communicate()[0]

tasks2 = output2

@app.route('/todo/showinterface', methods=['GET'])
@auth.login_required
def get_showinterface():

        #Update the json file
        updatejsonfile = "python showinterface.py"
        subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showint.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks2 = newoutput

        return tasks2

@app.route('/todo/createhost', methods=['POST'])
@auth.login_required
def create_host():

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
        tasks2 = newoutput

        return tasks2

@app.route('/todo/deletehost', methods=['DELETE'])
@auth.login_required
def delete_host():

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
        tasks2 = newoutput

        return tasks2

@app.route('/todo/updateinterface', methods=['UPDATE'])
@auth.login_required
def update_interface_state():

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
        tasks2 = newoutput

        return tasks2

###################################################################################

#LOH YU YANG's CRUD

child = subprocess.Popen('cat showhardware.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks/showhardware', methods=['GET'])
@auth.login_required
def READ2():

        #Updating JSON File & Flask Item Table
        updatejson = "python showhardware.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showhardware.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks/bridgedomain', methods=['GET'])
@auth.login_required
def READ():

        #Updating JSON File & Flask Item Table
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks/bridgedomain', methods=['PUT'])
@auth.login_required
def UPDATElearn():

        if not request.json or not 'Learning' in request.json:
                abort(400)

        task = {'Learning': request.json['Learning']}

        learn = str(request.json['Learning'])
        update = 'sudo vppctl set bridge-domain learn %s' % (learn)
        subprocess.call(update,stdout=subprocess.PIPE, shell=True)

        #Updating JSON File & Flask Item Table  
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks/loopbackint', methods=['POST'])
@auth.login_required
def CREATE():

        addintf = 'sudo vppctl create loopback interface'
        subprocess.call(addintf,shell=True)

        output = subprocess.Popen('sudo vppctl show interface', stdout=subprocess.PIPE,shell=True)
        newoutput = output.communicate()[0]
        tasks = newoutput
        return tasks

@app.route('/vpp/tasks/loopbackint', methods=['DELETE'])
@auth.login_required
def DELETE():

        if not request.json or not 'Name' in request.json:
                abort(400)

        task = { 'Name': request.json['Name'] }

        LBintf = str(request.json['Name'])
        deleteintf = 'sudo vppctl delete loopback interface intfc %s' % (LBintf)
        subprocess.call(deleteintf, shell=True)

        output = subprocess.Popen('sudo vppctl show interface', stdout=subprocess.PIPE,shell=True)
        newoutput = output.communicate()[0]
        tasks = newoutput
        return tasks

@app.route('/vpp/tasks/bridgedomainf', methods=['PUT'])
@auth.login_required
def UPDATEflood():

        if not request.json or not 'Flooding' in request.json:
                abort(400)

        task = {'Flooding': request.json['Flooding'] }

        flood = str(request.json['Flooding'])
        update = 'sudo vppctl set bridge-domain flood %s' % (flood)
        subprocess.call(update,stdout=subprocess.PIPE, shell=True)

        #Updating JSON File & Flask Item Table  
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks/vxlan', methods=['POST'])
@auth.login_required
def CREATE2():

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

        output = subprocess.Popen('sudo vppctl show vxlan tunnel', stdout=subprocess.PIPE,shell=True)
        newoutput = output.communicate()[0]
        tasks = newoutput
        return tasks

@app.route('/vpp/tasks/vxlan', methods=['DELETE'])
@auth.login_required
def DELETE2():

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

        output = subprocess.Popen('sudo vppctl show vxlan tunnel', stdout=subprocess.PIPE,shell=True)
        newoutput = output.communicate()[0]
        tasks = newoutput
        return tasks


if __name__== '__main__':
	app.run(debug=True)


