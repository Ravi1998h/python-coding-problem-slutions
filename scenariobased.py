'''
a='PrasaD$#%R7=<akesh()AmiT)[]n'
b=' '
for i in a:
    if 'A'<=i<='Z':
        b=b+chr(ord(i)+32)
    elif 'a'<=i<='z':
        b=b+i
    else:
        b=b+' '
s=b.split()
d={}
for i in s:
    d[i]=len(i)
print(d)
'''



a='45756833'
r=0
s=0
for i in range(len(a)):
    if 0<=i<(len(a)//2):
        r=r+int(a[i])
        print(r)
    if (len(a)//2)<=i<=(len(a)):
        s=s+int(a[i])
        print(s)
if r==s:
    print('this num is lucky num')
else:
    print('this num is not lucky num')
