num=int(input("enter any number"))
sum=1
while num>0:
    digit=num%10
    sum=sum*digit
    num=num//10
print(sum)