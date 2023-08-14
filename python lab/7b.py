import numpy as np
m=int(input("enter the number of rows:"))
n=int(input("enter the number of columns:"))
a=np.zeros((m,n),dtype=int)
for i in range (m):
    for j in range(n):
        a[i][j]=int(input("enter:"))
print(a)
print("reverse Order\n")
b=np.flip(a)
print(b)
print("\nPrincipal Diagonal")
print(np.diag(a))
print("\nAscending according to column 1")
# print(a[np.argsort(a[:, 0])])
print((np.sort(a,axis=None)).reshape(m,n))
print("\nDescending according to column 1")
# print(a[a[:,0].argsort()[::-1]])
print((np.sort(a,axis=None))[::-1].reshape(m,n))