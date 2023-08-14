import random
a=[]
for i in range(20):
    a.append(random.randint(1,10000))
print(a)
for i in a:
    if (i%2!=0)and(((i/10<10)and(i/10>1))or((i/1000<10)and(i/1000>1))):
        print(i,end="\t")