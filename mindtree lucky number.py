a='1230'
r,s=0,0
for i in range(len(a)):
    if 0<=i<(len(a)//2):
        r=r+int(a[i])
        #print(r)
    if (len(a)//2)<=i<len(a):
        s=s+int(a[i])
        #print(s)
if r==s:
    print('this num is lucky num')
else:
    print('this num is not lucky num')

                                #OR

b='1230'
sum,sum1=0,0
for i in range(len(b)//2):
    sum=sum+int(a[i])
for j in range((len(b)//2),len(b)):
    sum1=sum1+int(a[j])
if sum==sum1:
    print('this num is lucky num')
else:
    print('this num is not lucky num')

