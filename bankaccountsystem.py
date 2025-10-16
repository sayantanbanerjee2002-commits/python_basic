class bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
# deposite method
    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"Deposided amount: {amount}.Updated balanace = {self.balance}")
# withdrawl method
    def withdrawl(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"withdrawl amount: {amount}. remaining balance ={self.balance}")
        else:
            print("Insufficient balance")

# creating an object
acc1 = bankaccount("Sayantan", 60000)
acc1.deposite(10000)
acc1.withdrawl(20000)
acc1.withdrawl(30000)
acc1.deposite(10000)
acc1.withdrawl(50000)
            