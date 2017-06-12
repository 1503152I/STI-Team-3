import os, subprocess, csv, json

command = "sudo vppctl show threads | column -t"
ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
out = ps.communicate()[0]

g = open('showthreads.txt', 'w')
print >>g, out
g.close()

rdy = os.popen("awk '{$1=$1}1' OFS=, /home/sti/vpp/showthreads.txt").read()

g = open('showthreads.csv', 'w')
print >>g, rdy
g.close()

with open('showthreads.csv') as g:
        reader = csv.DictReader(g)
        rows = list(reader)

json.dump(rows, open("showthreads.json", "w"), indent=4)