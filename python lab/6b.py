class Bank:
    def __init__(self,a,b):
        self.acno=a
        self.bal=b
    def withdraw(self,a):
        if a>self.bal:
            raise Exception("Insufficient Funds!!")
        else:
            self.bal-=a
            print(f"Transaction Succesfull,Your Balance is:{self.bal}")
    def deposit(self,a):
        if a%100!=0:
            raise Exception("Please Deposit amount in denominition of 100")
        else:
            self.bal+=a
            print(f"Transaction Succesfull,Your Balance is:{self.bal}")
a=Bank(1234,10000)
a.withdraw(5000)
a.deposit(5000)
a.withdraw(11000)