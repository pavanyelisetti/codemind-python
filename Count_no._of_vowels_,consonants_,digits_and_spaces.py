a=input()
v=0
c=0
d=0
w=0
for i in a:
    if i in 'aeiou':
        v+=1
    elif i in '0123456789':
        d+=1
    elif i==' ':
        w+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)