a=input()
a=list(a)
for i in a:
    if i==" ":
        a.remove(i)
b=set(a)
print(min(b),end=" ")
print(a.count(min(b)),end=" ")
print(max(b),end=" ")
print(a.count(max(b)),end=" ")

