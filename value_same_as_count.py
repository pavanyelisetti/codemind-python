n=int(input())
a=list(map(int,input().split()))
count1=0
s=0
for i in a:          
    b=a.count(i)    
    if(i==b):
        count1+=1   
        if(b>1):        
            a.remove(i)
print(count1)