import csv
f = open("StuData.csv","r")
cr = csv.reader(f)
for r in cr:
    print(r)
f.close()
