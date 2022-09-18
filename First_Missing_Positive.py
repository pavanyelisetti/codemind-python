x=int(input())
a=list(map(int,input().split()))
g=0
for j in range(1,max(a)+1):
    c=0
    for i in a:
        if i!=j:
            c+=1
    if c==len(a):
        print(j)
        g=1
        break
if g==0:
    print(max(a)+1)
    