#input=['h','e','l','l','o',' ',' ',' ','h','a','i']
#output=['hello   hai']


a=['h','e','l','l','o',' ',' ',' ','h','a','i']
b=''
for i in range(len(a)):
    if a[i]!=' ':
        b=b+a[i]
    if a[i]==' ':
       if 'a'<=a[i+1]<='z':
            b=b+a[i]
print([(b)])
