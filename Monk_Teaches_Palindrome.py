a=int(input())
for i in range(1,a+1):
    n=input()
    if(n==n[::-1]):
        if(len(n)%2==0):
            print("YES","EVEN")
        else:
            print("YES","ODD")
    else:
        print("NO")