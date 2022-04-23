f = open("d:\\stu_data","w")

while (True):
    roll = input("Enter Roll No.")
    s1 = input("Enter Marks for 1st Subject")
    s2 = input("Enter Marks of 2nd Subject")
    r = roll +"___"+s1+"___"+s2+"\n"
    f.write(r)
    ch = input("Do you wish to continue")
    if ch=="n" or ch=="N":
        break
f.close()
