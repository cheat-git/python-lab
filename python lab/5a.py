b=[]
for i in range(3):
    b.append(input("Enter the Input:"))
print(tuple(b))
a=tuple(b)
print(len(a))
f=1
for i in a:
    if i=='2':
        print("yes")
        f=0
        break
if f==1:
    print("no")
print(a[2])