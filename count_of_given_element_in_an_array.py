n=int(input())
a=list(map(int,input().split()))
x=int(input())
if x in a:
    print(a.count(x))
else:
    print("0")
    
