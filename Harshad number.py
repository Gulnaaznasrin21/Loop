num=int(input("give number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
if num%sum==0:
    print("it is a Harshad number")
else:
    print("it is not a Harshad number")
