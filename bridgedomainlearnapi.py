#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

child = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
def READ():

        #Updating JSON File & Flask Item Table
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks', methods=['UPDATE'])
def UPDATElearn():

        if not request.json or not 'Learning' in request.json:
                abort(400)

        task = {'Learning': request.json['Learning'] }

        bridge = str(request.json['Learning'])
        update = 'sudo vppctl set bridge-domain learn %s' % (bridge)
        subprocess.call(update,stdout=subprocess.PIPE, shell=True)

        #Updating JSON File & Flask Item Table  
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks


if __name__ == '__main__':
        app.run(debug=True)
