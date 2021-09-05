n=int(input("eneter any number"))
i=n
sum=0
while i>0:
    digit=i%10
    j=digit
    factorial=1
    while j>=1:
        factorial=j*factorial
        j-=1
    sum=sum+factorial
        
    i=i//10
if n==sum:
    print("it is a strong number")
else:
    print("it is not a strong number")