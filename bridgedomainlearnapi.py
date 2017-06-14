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

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

child = subprocess.Popen('cat showbridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
@auth.login_required
def READ():

        #Updating JSON File & Flask Item Table
        updatejson = "python showbridgedomain.py"
        subprocess.call(updatejson, shell=True)
        updatedchild = subprocess.Popen('cat showbridge.json', stdout=subprocess.PIPE,shell=True)
        updatedoutput = updatedchild.communicate()[0]
        tasks = updatedoutput

        return tasks

@app.route('/vpp/tasks', methods=['PUT'])
@auth.login_required
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