def bin(x):
    x=int(x)
    temp=x
    sum=0
    t=0
    while(temp>0):
        r=temp%10
        sum+=r*(2**t)
        temp//=10
        t+=1
    return sum
for i in range(int(input())):
    a=input()
    a=list(a)
    a=a[::-1]
    x=""
    d=[]
    y=""
    for i in a:
        x+=i
    for i in range(0,len(x),3):
        f=x[i:i+3]
        d.append(f)
    for i in d:
        i=i[::-1]
        x=str(bin(i))
        y+=x
    print(y[::-1])

        
        