def write1():
    f=open('a.txt','w')
    while(1):
        a=input("enter:")
        if a=='*':
            break
        f.write(a)
        f.write("\n")
    f.close()
def func():
    f=open('a.txt','r')
    a=f.read().split()
    b=[]
    for i in a:
        b.append(len(i))
    for i in a:
        if len(i)==max(b):
            print(f"Maximum:{i} length {max(b)}")
        if len(i)==min(b):
            print(f"Minimum:{i} length {min(b)}")
    f.close()
write1()
func()