totsize = 0
strisize = 0
myfile = open("trialfile.txt","r")
reader = myfile.readlines(72)
linecount = len(reader)
print(reader)
print(linecount)

myfile.close()