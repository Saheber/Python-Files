import pickle
f=open("a.dat","rb+")
records=pickle.load(f)
new_records=[]
roll_no=input("Enter Your Roll No. to Search = ")
for r in records:
    if r[0]==roll_no:
        pass
    else:
        new_records.append(r)
f.seek(0)
pickle.dump(new_records,f)
f.seek(0)
records=pickle.load(f)
for r in records:
    print(r)
f.close()
