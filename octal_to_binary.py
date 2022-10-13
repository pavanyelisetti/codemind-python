def bini(x):
    temp=x
    j=""
    c=""
    while(temp>0):
        r=temp%2;
        j+=str(r)
        temp//=2
    j=j[::-1]
    k=len(j)
    while(k<3):
        c+="0"
        k+=1
    return c+j
x=input()
j=""
v=""
for i in range(1,len(x)):
    j+=bini(int(x[i]))
temp=int(x[0])
while(temp>0):
    r=temp%2;
    v+=str(r)
    temp//=2
print(v[::-1]+j)