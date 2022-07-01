n=input()
n=n.lower()
n=set(n)
c=0
for i in n:
    if i!=" ":
        c+=1
print(c)