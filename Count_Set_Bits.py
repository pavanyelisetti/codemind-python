for i in range(int(input())):
    x=int(input())
    temp=x
    j=[]
    while(temp>0):
        r=temp%2
        j.append(r)
        temp//=2
    print(j.count(1))