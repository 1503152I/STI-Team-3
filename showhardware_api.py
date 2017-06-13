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

child = subprocess.Popen('cat showhardware.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/vpp/tasks', methods=['GET'])
@app.login_required
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