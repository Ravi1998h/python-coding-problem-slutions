#input='1122344444'
#output= counting the numbers  [(1,2),(2,2),(3,1),(4,5)]

a='1122344444'
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
