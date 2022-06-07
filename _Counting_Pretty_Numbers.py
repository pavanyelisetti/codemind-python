n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    count=0
    count1=0
    for i in range(a,b+1):
        if i>=10:
            r=i%10
            if(r==2 or r==3 or r==9):
                count+=1
        else:
            if(i==2 or i==3 or i==9):
                count1+=1
    print(count+count1)