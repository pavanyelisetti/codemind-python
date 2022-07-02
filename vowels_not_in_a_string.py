a=input()
a=set(a)
v="aeiou"
s=""
for i in a:
    if i in v:
        s=s+i
for i in v:
    if i not in s:
        print(i,end=" ")
if len(s)==5:
    print("0")