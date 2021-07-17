#find the series of factorial number from 10 to 20
f=1
for i in range(1,11):
    f=f*i
print(i,'=',f)
for j in range(11,21):
    f=f*j    
    print(j,'=',f)


#using while loop
print()
f=1
i=1
while i<=10:
    f=f*i
    i+=1
print(i,'=',f)
j=11
while j<=20:
    f=f*j
    print(j,'=',f)
    j+=1
    
