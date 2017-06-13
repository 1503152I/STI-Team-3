#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

child = subprocess.Popen('cat showhardware.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
def READ2():

        #Updating JSON File & Flask Item Table
        updatejson = "python showhardware.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showhardware.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

if __name__ == '__main__':
        app.run(debug=True)
