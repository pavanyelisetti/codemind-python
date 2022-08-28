a=input()
a=a.lower()
a=a.split()
x=[]
f=0
for i in a:
    i=str(i)
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    x.append(c)
print(x.count(max(x)))