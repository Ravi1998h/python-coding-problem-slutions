'''
def funny(n,a,b):
    data=0
    for i in range(len(n)):
        for j in range(a,len(n)+b):
            data=data+int(n[i])**j
            #print(data)
            a=a+1
            i=i+1
    result=data/int(n)
    if result>=1:
        return int(result)
    else:
        return -1
n=input('enter the num')
a=int(input('enetr the starting squre number'))
b=a
print(funny(n,a,b))
'''


b='1230'
sum,sum1=0,0
for i in range(len(b)//2):
    sum=sum+int(a[i])
for j in range((len(b)//2),len(b)):
    sum1=sum1+int(a[i])
print(sum)
print(sum1)
