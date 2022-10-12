for i in range(int(input())):
    x=int(input())
    temp=x
    sum=0
    t=0
    while(temp>0):
        r=temp%10
        sum+=r*(2**t)
        temp//=10
        t+=1
    print(sum)