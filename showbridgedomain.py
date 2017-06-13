import os, subprocess, csv, json

command = "sudo vppctl show bridge-domain | column -t"
ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
out = ps.communicate()[0]

g = open('showbridge.txt', 'w')
print >>g, out
g.close()

rdy = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/showbridge.txt").read()

g = open('showbridge.csv', 'w')
print >>g, rdy
g.close()

with open('showbridge.csv') as g:
        reader = csv.DictReader(g)
        rows = list(reader)

json.dump(rows, open("showbridge.json", "w"), indent=4)