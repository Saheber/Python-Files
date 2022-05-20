stu = []
mks = []

for a in range (4):
    n, m = eval(input("Enter Roll No., Enter Marks"))
    stu.append(n)
    mks.append(m)
dict1 = {stu[0]:mks[0],stu[1]:mks[1],stu[2]:mks[2],stu[3]:mks[3]}
print("Created Dictionary =")
print(dict1)

if stu[1]>75:
    print("Student No.", stu[1],"(>75)")
else:
    print("Student No.", stu[1],"(<75)")
