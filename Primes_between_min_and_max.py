def isprime(x):
    d=0
    for i in range(1,x+1):
        if x%i==0:
            d+=1
    if(d==2):
        return 1
n=int(input())
a=list(map(int,input().split()))
maxx=0
maxi=0
mini=0
minn=a[0]
temp1=0
c=0
for i in range(0,len(a)):
    if(a[i]>=maxx):
        maxx=a[i]
        maxi=i
    if(a[i]<=minn):
        minn=a[i]
        mini=i
if mini>maxi:
    temp1=mini
    mini=maxi
    maxi=temp1
for i in range(mini,maxi+1):
    if isprime(a[i]):
        c+=1
print(c)

        