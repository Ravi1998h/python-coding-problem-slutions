a=[7,7,3,3,4,4,1,5,10,22,9,33,21,50,41,60,22,68,90]
c=[]
for i in range(len(a)):
    if a[i] not in c:
        if a[0]<=a[i]:
            if a[0]!=a[i]:
                c=c+[a[i]]
                a[0]=a[i]
            else:
                c=c+[a[i]]
        if (c[-1])<a[i]:
            c=c+[a[i]]
print(len(c))
print(c)
