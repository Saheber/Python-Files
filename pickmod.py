import pickle 
l1 = eval(input("Enter Your List"))
list(l1)
f =  open("abc.dat","wb")
pickle.dump(l1,f)
print("Data Saved")
f.close()

f = open("abc.dat","rb")
l = pickle.load(f)
print("Your Saved List is =",l)
