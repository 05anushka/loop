a=int(input("enter the number"))
b=a
sum=0
while b>0:
     r= b%10
     sum=sum+r
     b=b//10
if a%sum ==0:
     print(a,"is harshad number")
else:
     print(a,"is not harshad number")

