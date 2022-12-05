from itertools import permutations
a,c=list(map(int,input().split()))
l=list(permutations(range(1,a+1)))
b=[]
for i in l:
    k=''
    for j in i:
        k+=str(j)
    b.append(k)
print(int(b[c-1]))
        
    