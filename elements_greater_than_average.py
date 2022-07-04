n=int(input())
a=list(map(int,input().split()))
c=0
x=0
for i in a:
    x+=i
y=x//n
for i in a:
    if i>=y:
        c+=1
print(c)