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

#@app.route('/todo/updatebridge', methods=['PUT'])
#@auth.login_required
#def update_bridge_forward():
#
#        if not request.json or not 'State' in request.json:
#                abort(400)
#        if not request.json or not 'ID' in request.json:
#                abort(400)
#
#        BRIDGEID = int(request.json['ID'])
#        UPDATEBRIDGE = str(request.json['State'])
#
#	if UPDATEBRIDGE == "enable":
#		UPDATEBRIDGE == ""
#
#	addintf = 'sudo vppctl set bridge-domain forward %i %s' % (BRIDGEID, UPDATEBRIDGE)
#	subprocess.call(addintf,stdout=subprocess.PIPE, shell = True)
#
#	#Output the result of the update i.e. show bridge
#	childsp = subprocess.Popen('sudo vppctl show bridge', stdout=subprocess.PIPE, shell = True)
#	childoutput = childsp.communicate()[0]
#	showbridgedomain = childoutput
#
#	return showbridgedomain

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

        DHCPINT = str(request.json['Interface'])
        addintf = 'sudo vppctl set dhcp client del intfc %s' % (DHCPINT)
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

@app.route('/todo/updateinterface', methods=['PUT'])
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

#@app.route('/vpp/tasks/bridgedomain', methods=['PUT'])
#@auth.login_required
#def UPDATElearn():
#
#        if not request.json or not 'Learning' in request.json:
#                abort(400)
#
#        task = {'Learning': request.json['Learning']}
#
#        learn = str(request.json['Learning'])
#        update = 'sudo vppctl set bridge-domain learn %s' % (learn)
#        subprocess.call(update,stdout=subprocess.PIPE, shell=True)
#
#        #Updating JSON File & Flask Item Table  
#        updatejson = "python showbridgedomain.py"
#        subprocess.call(updatejson, shell=True)
#        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
#        updatedoutput = updatedchild.communicate()[0]
#        tasks = updatedoutput
#
#        return tasks

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

#@app.route('/vpp/tasks/bridgedomainf', methods=['PUT'])
#@auth.login_required
#def UPDATEflood():
#
#        if not request.json or not 'Flooding' in request.json:
#                abort(400)
#
#        task = {'Flooding': request.json['Flooding'] }
#
#        flood = str(request.json['Flooding'])
#        update = 'sudo vppctl set bridge-domain flood %s' % (flood)
#        subprocess.call(update,stdout=subprocess.PIPE, shell=True)
#
#        #Updating JSON File & Flask Item Table  
#        updatejson = "python showbridgedomain.py"
#        subprocess.call(updatejson, shell=True)
#        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
#        updatedoutput = updatedchild.communicate()[0]
#        tasks = updatedoutput
#
#        return tasks

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

####################################################################################

#YU XIANG'S CRUD

sub = subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
results = sub.communicate()[0]

job = results

sub2 = subprocess.Popen('cat showapiclients.json',stdout=subprocess.PIPE,shell=True)
results2 = sub2.communicate()[0]

job2 = results2

@app.route('/todo/iparp', methods=['GET'])
@auth.login_required
def get_iparp():
	#Update the json file when a new item is added
	update = "python showiparp.py"
	subprocess.call(update,shell=True)
	
	#Update the displayed flask table
	sub = subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
	newresults = sub.communicate()[0]
	newjob = newresults

	return newjob	

@app.route('/todo/apiclients', methods=['GET'])
@auth.login_required
def get_apiclients():
	#Update the json file when a new item is added
	update = "python showapiclients.py"
	subprocess.call(update,shell=True)

	#Update the displayed flask table
	sub = subprocess.Popen('cat showapiclients.json',stdout=subprocess.PIPE,shell=True)
	newresults = sub.communicate()[0]
	newjob = newresults

	return newjob

@app.route('/todo/iparp', methods=['POST'])
@auth.login_required
def create_iparp():
	#abort if there are no inputs
	if not request.json or not 'Flags' in request.json:
		abort(400)
	if not request.json or not 'IP4' in request.json:
		abort(400)
	if not request.json or not 'Interface' in request.json:
		abort(400)
	if not request.json or not 'Ethernet' in request.json:
		abort(400)

	job = {
		'Flags': request.json['Flags'],
		'IP4': request.json['IP4'],
		'Interface': request.json['Interface'],
		'Ethernet': request.json['Ethernet']
	}
	#Requesting the types of input
	flag= str(request.json['Flags'])
	ipaddr= str(request.json['IP4'])
	interface= str(request.json['Interface'])
	eth= str(request.json['Ethernet'])

	#Inserting new input through vpp command
	insert= "sudo vppctl set ip arp %s %s %s %s" % (flag, interface, ipaddr, eth)
	sub= subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
	output= sub.communicate()[0]
	
	#Updating and calling the new json file
	update= "python showiparp.py"
	subprocess.call(update,shell=True)

	sub2= subprocess.Popen('cat showiparp.json',stdout=subprocess.PIPE,shell=True)
	newresults= sub2.communicate()[0]
	newjob = newresults

	return newjob

@app.route('/todo/iparp', methods=['DELETE'])
@auth.login_required
def delete_iparp():
	#abort if there are no inputs
	if not request.json or not 'Flags' in request.json:
		abort(400)
	if not request.json or not 'IP4' in request.json:
		abort(400)
	if not request.json or not 'Interface' in request.json:
		abort(400)
	if not request.json or not 'Ethernet' in request.json:
		abort(400)

        job = {
                'Flags': request.json['Flags'],
                'IP4': request.json['IP4'],
                'Interface': request.json['Interface'],
                'Ethernet': request.json['Ethernet']
        }
	#Requesting the types of input
	flag= str(request.json['Flags'])
	ipaddr= str(request.json['IP4'])
	interface= str(request.json['Interface'])
	eth= str(request.json['Ethernet'])

	#Deleting input through vpp command
	delete= "sudo vppctl set ip arp %s delete %s %s %s" % (flag, interface, ipaddr, eth)
	sub = subprocess.Popen(delete,shell=True,stdout=subprocess.PIPE)
	output= sub.communicate()[0]

	#Updating and calling the new json file
        update= "python showiparp.py"
        subprocess.call(update,shell=True)

        sub2= subprocess.Popen('cat readresults.json',stdout=subprocess.PIPE,shell=True)
        newresults= sub2.communicate()[0]
	newjob = newresults

	return newjob

@app.route('/todo/gretunnel', methods=['POST'])
@auth.login_required
def create_gretunnel():
	#abort if there are no inputs
	if not request.json or not 'src' in request.json:
		abort(400)
	if not request.json or not 'dst' in request.json:
		abort(400)

	#Requesting the types of input
	source= str(request.json['src'])
	destination= str(request.json['dst'])
	
	#Inserting new input through vpp command
	insert = "sudo vppctl create gre tunnel src %s dst %s" % (source, destination)
	sub = subprocess.Popen(insert,shell=True,stdout=subprocess.PIPE)
	output = sub.communicate()[0]

	#Display new input through vpp command
	update = "sudo vppctl show gre tunnel"
	sub2 = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
	newresults = sub2.communicate()[0]
	newjob = newresults

	return newjob

@app.route('/todo/gretunnel', methods=['DELETE'])
@auth.login_required
def delete_gretunnel():
	#abort if there are no inputs
	if not request.json or not 'src' in request.json:
		abort(400)
	if not request.json or not 'dst' in request.json:
		abort(400)

	#Requesting the types of input
	source= str(request.json['src'])
	destination= str(request.json['dst'])

	#Delete input through vpp command
	delete= "sudo vppctl create gre tunnel src %s dst %s del" % (source, destination)
	sub = subprocess.Popen(delete,shell=True,stdout=subprocess.PIPE)
	output = sub.communicate()[0]

	#Display new input through vpp command
	update= "sudo vppctl show gre tunnel"
	sub2 = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
	newresults = sub2.communicate()[0]
	newjob = newresults

	return newjob

#@app.route('/todo/bridgedomain/uu', methods=['PUT'])
#@auth.login_required
#def update_uu_flood():
#	#abort if there are no inputs
#	if not request.json or not 'ID' in request.json:
#		abort(400)
#	if not request.json or not 'disable' in request.json:
#		abort(400)
#
#	#Requesting the types of input
#	ID = int(request.json['ID'])
#	disable = str(request.json['disable'])
#
#	#Updating input through vpp command
#	update= "sudo vppctl set bridge-domain uu-flood %i %s" % (ID, disable)
#	sub = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
#	output= sub.communicate()[0]
#
#	#Display new input through vpp command
#	update2 = "sudo vppctl show bridge"
#	sub2 = subprocess.Popen(nupdate,shell=True,stdout=subprocess.PIPE)
#	newresults = sub2.communicate()[0]
#       newjob = newresults
#
#        return newjob

#@app.route('/todo/bridgedomain/arpterm', methods=['PUT'])
#@auth.login_required
#def update_arpterm():
#	#abort if there are no inputs
#	if not request.json or not 'ID' in request.json:
#		abort(400)
#	if not request.json or not 'disable' in request.json:
#		abort(400)
#	
#	#Requesting the types of input
#	ID = int(request.json['ID'])
#	disable = str(request.json['disable'])
#
#	#Updating input through vpp command
#	update= "sudo vppctl set bridge-domain arp term %i %s" % (ID, disable)
#	sub = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
#	output= sub.communicate()[0]
#
#	#Display new input through vpp command
#	update2 = "sudo vppctl show bridge"
#	sub2 = subprocess.Popen(nupdate,shell=True,stdout=subprocess.PIPE)
#	newresults = sub2.communicate()[0]
#	newjob = newresults
#
#	return newjob
 

########################################################################################

#Since the group uses bridge domain as the updates, these is the compiled version for all bridge domain updates

@app.route('todo/bridgedomain', methods=['PUT'])
@auth.login_required
def update_bridge():
	#abort if there are no inputs
	if not request.json or not 'ID' in request.json:
		abort(400)
	if not request.json or not 'State' in request.json:
		abort(400)
	if not request.json or not 'Type' in request.json:
		abort(400)

	#Requesting the types of input
	bridgeid = int(request.json['ID'])
	state = str(request.json['State'])
	bridgetype = str(request.json['Type'])

	states = "enable"
	if state.lower() == states:
		state == ""
	
	#Updating input through vpp command
	update = "sudo vppctl set bridge-domain %s %i %s" % (bridgetype, bridgeid, state)
	sub = subprocess.Popen(update,shell=True,stdout=subprocess.PIPE)
	output = sub.communicate()[0]

	#Updating and calling the new json file 
	update2 = "python showbridgedomain.py"
	subprocess.call(update2,shell=True)

	sub2 = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
	newresults = sub2.communicate()[0]
	newtask = newresults
	
	return newtask

if __name__== '__main__':
	app.run(debug=True)
