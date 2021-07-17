#amazon search

a='mango'
d=['man','mangodb','male','mangio']
l,s=[],''
for i in range(2,len(a)+1):
    for k in range(len(d)):
        if a[0:i]==d[k][0:i]:
            l=l+[d[k]]
    if len(a)!=i:
        s=s+a[0:i]+'='+str(l)+','
        l=[]
    else:
        s = s + a[0:i] + '=' + str(l)
print(s)
