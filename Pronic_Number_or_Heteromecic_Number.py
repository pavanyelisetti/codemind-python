n=int(input())
x=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            if i*j==n:
                if abs(i-j)==1:
                    print("YES")
                    x=1
                    break
    if x==1:
        break
if(x==0):
    print("NO")