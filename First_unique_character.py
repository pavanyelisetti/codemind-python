a=input()
b=list(a)
s=0
for i in a:
    if(a.count(i)==1):
        print(i)
        s=1
        break
if(s==0):
    print('-1')