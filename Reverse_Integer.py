n=int(input())
temp=n
rev=0
if(n>0):
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    print(rev)
if(n<0):
    n=n*-1
    temp=n
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    c='-'+str(rev)
    print(c)
    