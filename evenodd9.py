num=int(input("enter the number"))
i=0
while i<1:
    if num%2!=0:
        print("wierd")
    elif num%2==0 and num>2 and num<5:
        print("notwierd")
    elif num%2==0 and num>6 and num<20:
        print("wierd")
    else:
        print("notweird")
    i=i+1

        