a=int(input("enter any number"))
b=int(input("enter any number"))
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
        lcm=a*b/gcd
    i+=1
print("The least common multiplier of",a,"and",b,"is",lcm)