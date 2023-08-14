l=[35,123,11,215,14,1235,23512,3124,1521]
def maxmin():
    m=0
    for i in l:
        if m<=i:
            m=i
    mi=m
    for i in l:
        if mi>=i:
            mi=i
    print(f"Maximum:{m},Minimum:{mi}")
def secondmax():
    m=0
    for i in l:
        if m<=i:
            m=i
    sm=0
    for i in l:
        if i==m:
            continue
        if sm<=i:
            sm=i
    print(f"Second Max:{sm}")
maxmin()
secondmax()
