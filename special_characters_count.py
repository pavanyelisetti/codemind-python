a=input()
count=0
count1=0
count2=0
count3=0
for i in a:
    if(ord(i)>=33 and ord(i)<=47):
        count+=1
    if(ord(i)>=58 and ord(i)<=64):
        count1+=1
    if(ord(i)>=91 and ord(i)<=96):
        count2+=1
    if(ord(i)>=123 and ord(i)<=126):
        count+=1
print(count+count1+count2+count3)