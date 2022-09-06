import pickle
from re import L 
f = open("a.dat","wb+")
records=[]
while True:
    roll_no=input("Enter Your Roll No. = ")
    s1 = int(input("Enter Marks of Subject 1 = "))
    s2 = int(input("Enter Marks of Subject 2 = "))
    r=[roll_no,s1,s2]
    records.append(r)
    ch=input("Do You Wish To Continue? = ")
    if ch=="n" or ch=="N":
        break
pickle.dump(records,f)
f.seek(0)
records=pickle.load(f)
for r in records:
    print(r)
