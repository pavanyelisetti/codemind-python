def bin(x):
    temp=x;
    j=""
    while(temp):
        r=temp%2;
        j+=str(r)
        temp//=2
    while(len(j)<b):
        j+="0"
    j=j[::-1]
    return j
n=int(input())
b=n
n=pow(2,n)
for i in range(n):
    print(bin(i))