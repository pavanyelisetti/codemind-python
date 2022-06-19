n=int(input())
a=list(map(int,input().split()))
count1=0
n=0
s=0
for i in a:          
    b=a.count(i)    
    if(i==b):
        count1+=i 
        n+=1
        s=1
        if(b>1):        
            a.remove(i)
if(s==0):
    print('-1')
else:
    c=count1/n
    print("%.2f"%c)