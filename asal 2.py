
for i in range(1,100):
    flag=0
    for x in range(2,i):
        if i%x==0:
         break
    else:
        print(i)
