f = open("Writer.txt","w")
List1 = []
for i in range (5):
    name = input("Enter Your Name = ")
    List1.append(name+'\n')
f.writelines(List1)
f.close()
print(type(f))