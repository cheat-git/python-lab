n=int(input("Enter the number of strings:"))
a=[]
b=[]
for i in range(n):
    c=input("Enter:")
    a.append((c,len(c)))
    b.append(len(c))
b.sort()
c=[]
for i in b:
    for j in a:
        if j[1]==i:
            c.append(j)
            a.remove(j)
            break 
print(c)