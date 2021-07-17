#input=1,2,3,4,5      output=['1','2','3','4','5']
#                             ('1','2','3','4','5')

a=1,2,3,4,5
l,t='',''
for i in a:
    l=l+str(i)
    t=t+str(i)
print(list((l)))
print(tuple(t))
