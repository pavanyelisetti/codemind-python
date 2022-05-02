x=int(input())
for i in range (1,x+1):
    if(x==i*i):
        print("True")
        break
if(x!=i*i):
    print("False")