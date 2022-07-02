a=input()
c=0
b=''
for i in a:
    if i not in b:
        b=b+i
for i in b:
    if i in "aeiouAEIOU":
        print(i,end=" ")
        c+=1
if c==0:
    print("-1")