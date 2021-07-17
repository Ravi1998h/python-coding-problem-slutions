#substacting the given numbers in list and find the max nu in list


b,c=[],[]
n=int(input('eneter the lengt of list'))
for i in range(n):
    n1=int(input('eneter the number'))
    b=b+[n1]
print(b)
for j in range(n-1):
    c=c+([b[j]-b[j+1]])
print(c)
max=c[0]
for i in c:
    if max<i:
        max=i
print('maximum number in list:',max)
