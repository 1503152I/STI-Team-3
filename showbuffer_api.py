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

child = subprocess.Popen('cat showbuffer/showbuffer.json', stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/todo/showbuffer', methods=['GET'])
@auth.login_required
def get_tasks():

        #Update the json file
        updatejsonfile = "python /home/sti/api-dev/showbuffer/showbuffer.py"
	subprocess.call(updatejsonfile, shell = True)

        #Update the flask item table
        newchild = subprocess.Popen('cat showbuffer/showbuffer.json', stdout=subprocess.PIPE,shell=True)
        newoutput = newchild.communicate()[0]
        tasks = newoutput

        return tasks

if __name__== '__main__':
	app.run(debug=True)


