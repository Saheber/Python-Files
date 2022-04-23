import pickle 
l1 = [2,34,35,67,7]
f =  open("abc.dat","wb")
pickle.dump(l1,f)
print("Data Saved")
f.close()

f = open("abc.dat","rb")
l = pickle.load(f)
print(l)