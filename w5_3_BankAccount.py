class BankAccount:
    def __init__(self):
        self.accountNumber='5552325'
        self.name='elif'
        self.balance=5555
    def deposit(self,d):
        self.d=d
        self.balance=self.balance+d
        return self.balance
    def withdrawal(self,w):
        self.w=w
        if self.w>self.balance:
            print("Impossible operation! Insufficient balance!")
        else:
            self.balance=self.balance-w
            return self.balance
    def bankFees(self):
        self.balance=self.balance-self.balance/100*5
        return self.balance
    def display(self):
      print("accountNumber : ",self.accountNumber)
      print("name : ",self.name)
      print("balance : ",self.balance)
customer1=BankAccount()
customer1.display()
customer1.deposit(10)
customer1.display()
customer1.withdrawal(66666)
customer1.display()
customer1.bankFees()
customer1.display()
    