factor=0
n=int(input("enter any number"))
while factor<=n:
    factor+=1
    if n%factor==0:
        print(factor)
print("above number's are the factor of",n)