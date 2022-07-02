a=input()
a=a.lower()
s=""
for i in a:
    if a.count(i)==1:
        s=s+i
s=sorted(s)
for i in s:
    if i!=" ":
        print(i,end="")