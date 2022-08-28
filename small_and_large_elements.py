a=input()
a=a.split()
for i in a:
    print(min(i),end=" ")
    break
a=a[::-1]
for i in a:
    print(max(i),end=" ")
    break
