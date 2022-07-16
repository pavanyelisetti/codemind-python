n=int(input())
a=[]
x=0
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        a.append(i)
for i in a:
    for j in a:
        if i!=j and i*j==n:
            print(i,j)
            x=1
            break
    if x==1:
        break
if x==0:
    print("-1")
    