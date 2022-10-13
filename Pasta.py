x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in b:
    for j in a:
        if(i==j):
            c+=1
            a.remove(i)
if(c==len(b)):
    print("Yes")
else:
    print("No")