a=input()
b=input()
a=a.lower()
b=b.lower()
a=set(a)
b=set(b)
s=""
c=0
for i in a:
    if i!=' ':
        if i not in b:
                s=s+i
for i in b:
    if i!=' ':
        if i not in a:
                s=s+i
s=sorted(s)
for i in s:
    if i!=" ":
        print(i,end="")