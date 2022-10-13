x=int(input())
temp=x
j=[]
while(temp>0):
    r=temp%2
    j.append(r)
    temp//=2
j=j[::1]
x=[]
for i in j:
    if(i==0):
        x.append(1)
    if(i==1):
        x.append(0)
k=0
sum=0
for i in x:
    sum+=i*(2**k)
    k+=1
print(sum)