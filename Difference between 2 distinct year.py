#difference between two distinct year



s='un was establish on 24-10-1947. and 12-09-1985 india got freedom on 15-08-1985, indian 15-09-1947'
list,count=[],0
for i in range(len(s)):
    if s[i]=='-':
        if s[i+3]=='-':
            list=list+[int(s[i+3+1:i+3+5])]
print(list)
for j in list:
        for k in list:
            if j!=k:
                count=count+1
        break
print(count)
