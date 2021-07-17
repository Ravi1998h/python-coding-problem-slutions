a,b='5020','5564'
sum,sum1=0,0
for i in range(1,int(a)):
    if int(a)%i==0:
        sum=sum+i
for j in range(1,int(b)):
    if int(b)%j==0:
        sum1=sum1+j
if sum==int(b) and sum1==int(a):
    print('this numbers are amicable numbers')
