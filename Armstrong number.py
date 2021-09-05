i=int(input("enter number"))
d=str(i)
sum=0
while i>0:
    digit=i%10
    i=i//10
    sum=sum+(digit**len(d))
    s=str(sum)
if s==d:
    print(d,"is a Armstrong number")
else:
    print(d,"is not a Armstronng number")