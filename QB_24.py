start=int(input("enter fifrst number"))
end=int(input("enter last number"))
e_sum=0
o_sum=0
while start<end:
    if start%2==0:
        e_sum+=1
    else:
        o_sum+=1
    start+=1
print("sum of even number=",e_sum)
print("sum of odd number=",o_sum)