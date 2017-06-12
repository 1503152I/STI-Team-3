import os, subprocess, csv, json

#Running the vpp command
cmd = "sudo vppctl show buffers | column -t"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
output = ps.communicate()[0]

#Outputting the result to a text file for easier translation
f = open('showbuffer.txt', 'w')
print >>f, output
f.close()

#Readying the text file for json format translation (replacing spaces with commas)
trueoutput = os.popen("awk '{$1=$1}1' OFS=, /home/sti/api-dev/showbuffer/showbuffer.txt").read()

#Saving the readied output for json translation
f = open('showbuffer.csv', 'w')
print >>f, trueoutput
f.close()

#Performing the csv to json translation, saving the json output to a file.
with open('showbuffer.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

json.dump(rows, open("showbuffer.json", "w"), indent=4)
