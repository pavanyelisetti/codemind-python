n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n-1):
    max=0
    for j in range(i+1,n):
        if max<=a[j]:
            max=a[j]
    b.append(max)
b.append(-1)
print(*b)