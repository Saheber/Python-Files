stk=[]
ch='y'
while ch=='y' or ch=='Y':
    print("1 : Push")
    print("2 : Pop")
    print("3 : Display")
    c = int(input("Enter Your Choice = "))
    if c==1:
        a=int(input("Enter A Value = "))
        stk.append(a)
    elif c == 2:
        if stk == []:
            print("Stack Empty .. Underflow")
        else:
            print("Deleted element is",stk.pop())
    elif c == 3:
        for i in range(len(stk)-1,-1,-1):
            print(stk[i], end="->")
    
    else:
        print("invalid input")
    ch=input("DO YOU KNOW WISH TO CONTINUE")
    9