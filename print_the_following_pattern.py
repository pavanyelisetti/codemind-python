n=int(input())
for i in range(n):
    for j in range(n):
        if i!=n-1:
            if (i==j) or (j==0):
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print("*",end="")
    print()