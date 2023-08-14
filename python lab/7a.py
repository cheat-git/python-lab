class stack:
    def __init__(self,l):
        self.l=l
        self.top=-1
    def push(self,a):
        if self.top>len(self.l):
            print("stack overflow")
        else:
            self.top+=1
            self.l[self.top]=a
    def pop1(self):
        if self.top==-1:
            print("stack underflow")
        else:
            print(self.l[self.top])
            self.top-=1
    def display(self):
        a=self.top
        for i in range(a+1):
            print(self.l[i])
class queue:
    def __init__(self,l):
        self.l=l
        self.front=-1
        self.rear=-1
    def add(self,a):
        if self.front>len(self.l):
            print("stack overflow")
        else:
            self.rear+=1
            self.l[self.rear]=a
    def delete(self):
        if self.front==self.rear:
            print("stack underflow")
        else:
            self.front+=1
            print(self.l[self.front])
            # self.front+=1
    def display(self):
        a=self.front
        for i in range(a,self.rear+1):
            print(self.l[i])
l=[0,0,0,0]
# print(len(l))
a=stack(l)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.pop1()
print("\n")
a.display()
print("\n")
l=[0,0,0,0]
a=queue(l)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.delete()
print("\n")
a.display()