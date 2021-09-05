i=1
count=0
a=int(input("how many prime numbers you want from begining?"))
while count<a:
    factor=0
    j=1
    while j<=i:
        if i%j==0:
            factor+=1
        j+=1
    if factor==2:
        k=i
        count+=1
    i+=1
print(k)