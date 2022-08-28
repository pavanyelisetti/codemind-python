a=input()
a=a.lower()
a=a.split()
for i in a:
    i=str(i)
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    print(c,end=" ")