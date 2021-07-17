l=[1,2,3,4,[25,12,12,45,7],2,2,5,[7,8,5,5]]
n=[]
for i in l:
    if type(i)==list:
        for j in i:
            n=n+[j]
    else:
        n=n+[i]
print(n)
            
        
