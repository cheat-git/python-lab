def write1():
    f=open('a.txt','w')
    while(1):
        a=input("enter:")
        if a=='*':
            break
        f.write(a)
    f.close()
def func():
    f=open('a.txt','r')
    a=f.read()
    c=0
    d=0
    e=0
    for i in a:
        if i.islower():
            c+=1
        elif i.isupper():
            d+=1
        elif i.isdigit():
            e+=1
    print(f"LowerCase:{c},UpperCase:{d},Digits:{e}")
    f.close()
write1()
func()