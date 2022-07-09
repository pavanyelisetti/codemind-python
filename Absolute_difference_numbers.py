a,b=map(int,input().split())
a=str(a)
x=a[:b]
z=a[::-1]
y=z[:b]
y=y[::-1]
print(abs(int(x)-int(y)))