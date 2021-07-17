#output=[(1,3),(2,1),(5,3),(1,1),(2,1)

a='111255512'
count,n=0,0
l=[]
for k in range(len(a)):
    for i in range(n,len(a)):
        for j in range(n,len(a)):
            if a[i]==a[j]:
                count=count+1
                if j+1==len(a):
                    l = l + [(a[i], count)]
            else:
                l=l+[(a[i],count)]
                n=n+count
                count=0
                break
        break
    if i+1==len(a):
        break
print(l)
