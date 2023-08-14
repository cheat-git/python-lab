def binarys(a,h,l,k):
    if (l<=h):
        m=(h+l)//2
        if (k==a[m]):
            print(f"Found at {m}")
            return 1
        elif (k>a[m]):
            return binarys(a,h,m+1,k)
        else:
             return binarys(a,m-1,l,k)
    return 0
n=int(input("Enter the number of elements:"))
print("enter the elements in ascending order")
l=[]
for i in range(n):
    l.append(int(input("Enter:")))
k=int(input("Enter the key:"))
b=binarys(l,len(l)-1,0,k)
if b==0:
    print("Not found")