import os, subprocess, csv, json

read = "sudo vppctl show ip arp | column -t"
sub = subprocess.Popen(read,shell=True,stdout=subprocess.PIPE)
result = sub.communicate()[0]

textfile = open('readresults.txt', 'w')
print >>textfile, result
textfile.close()

arrange = "awk '{$1=$1}1' OFS=, /home/sti/readresults.txt"
sub2 = subprocess.Popen(arrange,shell=True,stdout=subprocess.PIPE)
output = sub2.communicate()[0]

textfile = open('readresults.csv', 'w')
print >>textfile, output
textfile.close()

with open('readresults.csv') as textfile:
        reader = csv.DictReader(textfile)
        rows = list(reader)

json.dump(rows, open("showiparp.json", "w"), indent=4)
