#total count pythogoran a**2 + b**2 = c**2

count=0
for i in range(5,21):
    for j in range(5,21):
        d=i**2+j**2
        for k in range(5,21):
            if d==k**2:
                count=count+1
print(count//2)
