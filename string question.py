sentence="my name is Naazneen and my Friends name is Barsha and my mom is my best friend"
sub="is"
c=sentence.split()
d=0
i=1
while  i<len(c):
    if c[i]==sub:
        d+=1
    i+=1
print(d,"times",sub,"present in sentence")
