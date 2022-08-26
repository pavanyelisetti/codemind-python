x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
y=[]
for i in a:
    if i not in x:
        x.append(i)
for i in b:
    if i not in y:
        y.append(i)
for i in x:
    if i in y:
        print(i,end=" ")


