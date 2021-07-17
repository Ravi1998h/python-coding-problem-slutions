n1=int(input('eneter the 1st num'))
n2=int(input('eneter the 2nd num'))
if n1<n2:
    r=n1
else:
    r1=n2
n=0
for i in range(1,r+1):
    if n1%i==0 and n2%i==0:
            print('hcf',i)
