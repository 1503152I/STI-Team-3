import os, subprocess, csv, json

read = "sudo vppctl show api clients | column -t | sed 1d"
sub = subprocess.Popen(read,shell=True,stdout=subprocess.PIPE)
result = sub.communicate()[0]

textfile = open('readresults2.txt', 'w')
print >>textfile, result
textfile.close()

arrange = "awk '{$1=$1}1' OFS=, /home/sti/readresults2.txt"
sub2 = subprocess.Popen(arrange,shell=True,stdout=subprocess.PIPE)
output = sub2.communicate()[0]

textfile = open('readresults2.csv', 'w')
print >>textfile, output
textfile.close()

with open('readresults2.csv') as textfile:
	reader = csv.DictReader(textfile)
	rows = list(reader)

json.dump(rows, open("showapiclients.json", "w"), indent=4)
