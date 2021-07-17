#input='ababcc@a!'
#output=a 3
#       b 2
 #      c 2
  #     @ 12(3*2*2)
   #    ! 4(@value/max count)(12/3)
n='ababcc@a!'
r,l,mul,count='',[],1,0
for i in n:
    if i not in r:
        if 'a'<=i<='z':
            r=r+i
            data=n.count(i)
            print(i,data)
            l=l+[data]
        else:
            count=count+1
            if count==1:
                for j in l:
                    mul=mul*j
                print(i,mul)
            else:
                if count==2:
                    print(i,mul//max(l))
