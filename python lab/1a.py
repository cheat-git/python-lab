a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("1.Sum\n2.Difference\n3.Multiply\n4.Divide"))
if c==1:
    print(f"The Sum is:{a+b}")
elif c==2:
    print(f"The Difference is:{a-b}")
elif c==3:
    print(f"The Product is:{a*b}")
else:
    print(f"The Quotient is:{a/b}")