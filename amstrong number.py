a=input('enter the number')
b=0
for i in a:
    b=b+int(i)**len(a)
if b==int(a):
    print('this number amstrong number')
else:
    print('this number not amstrong number')
