a=input()
b=""
for i in a:
    if i in "aeiouAEIOU":
        if i not in b:
            b=b+i
for j in b:
    print(j,end=' ')
