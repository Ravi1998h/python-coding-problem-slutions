n=input('enter the number')
f=1
d=0
for i in n:
    for j in range(1,int(i)+1):
        f=f*j
    d=d+f
    f=1
if d==int(n):
    print('this number is strong number')
else:
    print('this number not strong number')
    

