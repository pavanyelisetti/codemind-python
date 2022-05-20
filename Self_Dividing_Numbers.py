a=int(input())
b=int(input())
for i in range (a,b+1):
    count=0
    count2=0
    temp=i
    while(temp>0):
        r=temp%10
        count2+=1
        if(r>0):
            if(i%r==0):
                count+=1
        temp=temp//10
    if(count==count2):
        print(i,end=' ')