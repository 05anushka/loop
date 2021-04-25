num=int(input("enter the num"))
i=1
while i<=num:
    b=1
    while b<=num-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    k=i-1
    while k>0:
        print(k,end="")
        k=k-1
    print()
    i+=1



    





