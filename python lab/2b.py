a=["Maths","MCIOT","DAA","DCN","FAFL"]
for i in a:
    print(i)
print(a[1],a[4])
print(a[:4])
print(a[-1:-3:-1])
if "Python lab" in a:
    print("yes")
else:
    print("no")
a.append("Python Lab")
print(a)
a.insert(1,"DAA Lab")
print(a)
a.remove("DAA")
print(a)
print(a.pop())