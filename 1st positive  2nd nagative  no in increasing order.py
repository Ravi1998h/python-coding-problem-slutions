#input=[45,-25,84,2,6,8,-24,-1,4,-6] 1st positive  2nd nagative in increasing order
#output=[2, -25, 4, -24, 6, -6, 8, -1, 45, 84]



a=[45,-25,84,2,6,8,-24,-1,4,-6]
b,c,d=[],[],[]
for i in a:
    if i >=0:
        b=b+[i]
    else:
        c=c+[i]
e=sorted(b)
f=sorted(c)
for l in range(len(b)):
    d=d+[e[l]]
    if l in range(len(f)):
        d=d+[f[l]]
print(d)
