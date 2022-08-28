a=input()
a=a.split()
x=0
y=0
for i in a:
    x+=ord(min(i))
    y+=ord(max(i))
print(abs(x-y))