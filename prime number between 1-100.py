i=1
while i<=100:
    factor=0
    x=1
    while x<=i:
        if i%x==0:
            factor+=1
        x+=1
    if factor==2:
        print(i,"is a prime number")
    else:
        print(i,"is not a prime number")
    i+=1