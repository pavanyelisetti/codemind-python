n=int(input())
for i in range (1,n+1):
    a=input()
    count=0
    for i in a:
        if i in '0123456789':
            count+=1
    if(count==len(a)):
        print('True')
    else:
        print('False')