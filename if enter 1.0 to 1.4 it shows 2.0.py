#if enter 1.0 to 1.4 it shows 2.0
#if enter 1.5 to 2.0 it shows 1.0



a='1.5'
b=int(a[0])
if b<=float(a)<=(b+0.4):
    print(b+1)
if b+0.4<float(a)<=(b+0.9):
    print(1)
    '''
