a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=set(x)
d=set(y)
count=0
for i in c:
    for j in d:
        if i==j:
            count+=1
print(count)