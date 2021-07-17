n='hEllO WoRLD hOw Are YoU'
r=''
for i in n:
    if 'a'<=i<='z':
        r=r+chr(ord(i)-32)  
    if 'A'<=i<='Z':
        r=r+chr(ord(i)+32)
    if i==' ':
        r=r+i
print(r)
