n=input()
n=n.lower()
n=set(n)
s=""
for i in n:
    if i!=" ":
        s=s+i
s=sorted(s)
for i in s:
    print(i,end="")