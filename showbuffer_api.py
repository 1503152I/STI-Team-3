#!flask/bin/python
from flask import Flask,jsonify,abort,request
import subprocess,os,json

app = Flask(__name__)

child = subprocess.Popen('cat showbuffer/showbuffer.json', stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]

tasks = output

@app.route('/todo/showbuffer', methods=['GET'])
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


