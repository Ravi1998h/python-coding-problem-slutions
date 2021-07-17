#total number of uppercase and lowercase
n=input('eneter the string')
count=0
count1=0
for i in n:
    if 'A'<=i<='Z':
        count=count+1
    else:
        count1=count1+1
print('total uppercase in  given str:',count)
print('total lowercase in  given str:',count1)        
