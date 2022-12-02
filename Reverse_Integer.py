n=int(input())
temp=n
while(1):
    if n%10!=0:
        break
    else:
        n//=10
c=0
if n<0:
    n=n*-1
    c+=1
x=str(n)
x=x[::-1]
if c>0:
    print("-"+x)
else:
    print(x)