a=input()
a=a.lower()
a=a.split()
c=0
for i in a:
    i=str(i)
    if i[0] in "aeiou" and i[-1] not in "aeiou":
        c+=1
print(c)
        
    