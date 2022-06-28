a=input()
a=a.split()
max=0
for i in a:
    i=str(i)
    if (max<len(i)):
        max=len(i)
print(max)
    