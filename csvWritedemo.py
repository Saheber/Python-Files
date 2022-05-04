import csv
f = open("StuData.csv","w",newline='')
wr = csv.writer(f)
wr.writerow(['Roll No.','Name','Marks'])
rows = (['1','Sunny',90],['2','Baban',85])
wr.writerows(rows)
f.close()
print("Data Saved")
