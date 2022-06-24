totsize = 0
strisize = 0
reader = " "
myfile = open("trialfile.txt","r")
while reader:
    reader = myfile.readline()
    strisize = strisize + len(reader.strip())
    totsize = totsize + len(reader)
print("Total Size of File =", totsize)
print("Actual File Size =", strisize)
myfile.close()