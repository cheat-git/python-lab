a=int(input("enter the num:"))
b=int(input("enter the num:"))
flag=0


for i in range(a,b+1):
    if(i==1):
        continue
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
       print(i)
    flag=0
