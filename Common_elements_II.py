e,f=map(int,input().split())
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
    if i not in y:
        print(i,end=" ")
for i in y:
    if i not in x:
        print(i,end=" ")