a=input()
b=''
c="aeiou"
s=0
for i in  a:
    if i in "aeiouAEIOU":
        b=b+i
for i in c:
    if i not in b:
        print(i,end=' ')
        s=1
if(s==0):
    print("0")


