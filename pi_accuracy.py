import commands

nmap = 100
results = []

nrange = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]


for nreduce in nrange:
    cmd = "bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar pi %s %s" % (nmap, nreduce)
    a, b = commands.getstatusoutput(cmd)
    temp = b[-22:]
    results.append((nmap, nreduce, temp))


# write to file
filename = "pi-nums.txt"
with open(filename, 'w') as f:
    for item in results:
        f.write("%s %s %s\n" % (item[0], item[1], item[2]))
print("Done")


