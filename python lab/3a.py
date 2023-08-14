d={}
def add(k,m):
    d[k]=m
def remove1(k):
    if k in d.keys():
        del d[k]
    else:
        print("Key Not in Dict")
def findm(k):
    if k in d.keys():
        print(d[k])
    else:
        print("Key not in Dict")
def findw(m):
    f=0
    for i in d.keys():
        if m==d[i]:
            print(i)
            
            f=1
    if f==0:
        print("Meaning Not in Dict")
def display():
     a=dict(sorted(d.items()))
     print(a)
while(True):
    a=int(input("1.Add\n2.Remove\n3.Find Meaning\n4.Find Word\n5.Display"))
    if a==1:
        k=input("Enter the word:")
        m=input("Enter the meaning:")
        add(k,m)
    elif a==2:
        k=input("Enter the word:")
        remove1(k)
    elif a==3:
        k=input("Enter the word:")
        findm(k)
    elif a==4:
        m=input("Enter the meaning:")
        findw(m)
    else:
        display()
    o=int(input("Continue press 1 else 0:"))
    if o==0:
        break        
