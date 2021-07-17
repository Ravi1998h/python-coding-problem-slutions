a='hi amit hello'
b,c='',[]
for i in a:
    if i==' ':
        c=[b]+c
        print(c)
        b=' '
    else:
        b=b+i
        print(b)
for i in c:
    b=b+' '+i
print(b)




                            #OR



#str='ravi how are you'
#str2,str3='',''
#i=len(str)-1
#while i>=0:
#    if 'a'<=str[i]<='z':
#        str2=str[i]+str2
#    if str[i]==' ':
#        str3,str2=str3+str2+str[i],''
 #   i=i-1
#print(str3+str2)
