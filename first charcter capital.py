a='hello world nagaraj'
r=''
for i in range(len(a)):
    if i==0:
        if 'a'<=a[i]<='z':
            r=r+chr(ord(a[i])-32)
    elif a[i-1]==' ':
        if 'a'<=a[i]<='z':
            r=r+' '+chr(ord(a[i])-32)
    else:
        r=r+a[i]
print(r)



                       #OR


#str='ravi how are you'
#str2,str3='',''
#i=len(str)-1
#while i>=0:
#    if 'a'<=str[i]<='z':
#        str2=str[i]+str2
#   if str[i]==' ':
 #       str3,str2=str3+str2+str[i],''
 #   i=i-1
#print(str3+str2)
