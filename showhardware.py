import os, subprocess, csv, json

command = "sudo vppctl show hardware-interfaces | column -t"
ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
out = ps.communicate()[0]

g = open('showhardware.txt', 'w')
print >>g, out
g.close()

rdy = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/showhardware.txt").read()

g = open('showhardware.csv', 'w')
print >>g, rdy
g.close()

with open('showhardware.csv') as g:
        reader = csv.DictReader(g)
        rows = list(reader)

json.dump(rows, open("showhardware.json", "w"), indent=4)