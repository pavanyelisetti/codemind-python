a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=set(x)
d=set(y)
s=0
k=0
count=0
for i in c:
    if i not in d:
        s+=1
for j in d:
    if j not in c:
        k+=1
print(s+k)
    