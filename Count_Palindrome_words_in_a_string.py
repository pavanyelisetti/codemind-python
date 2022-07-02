n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    i=str(i)
    if i==i[::-1]:
        c+=1
print(c)