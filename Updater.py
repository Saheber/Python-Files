import pickle
f=open("a.dat","rb+")
records=pickle.load(f)
new_records=[]
roll_no=input("Enter Your Roll No. to Updated = ")
for r in records:
    if r[0]==roll_no:
        r[1]=int(input("Enter New Value For Sub1"))
        r[2]=int(input("Enter New Value For Sub2"))
        
    new_records.append(r)
f.seek(0)
pickle.dump(new_records,f)
f.seek(0)
records=pickle.load(f)
for r in records:
    print(r)
f.close()
