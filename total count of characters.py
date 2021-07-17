#output=l5m5j1
a='lllllmmmmmj'
count,str1=0,''
for i in a:
    if i not in str1:
        for k in a:
            if i==k:
             count=count+1
        str1=str1+i+str(count)
        count=0
print(str1)
