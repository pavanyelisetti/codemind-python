n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
for x in range(max(len(c),len(d))):
    if x<min(len(c),len(d)):
        print(d[x],c[x],end=" ")
    else:
        if(len(c)>len(d)):
            print(c[x],end=" ")
        else:
            print(d[x],end=" ")
if n%2==1:
    print(0)
        