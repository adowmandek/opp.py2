

class Account:
    def __init__(self,phoneNumber, id,name):
         self.phoneNumber=phoneNumber
         self.id=id
         self.name=name
         self.balance=0 
         self.loanLimit=loanLimit
         

    def name(self):
         return f"hello this  is {self.phoneNumber}, {self.id} {self.name}"



    def send(self):
        withdraw=234568
        Send=4567890
        return f"hello this  is {self.withdraw}and{self.send}"


    def show_balance(self):
        return self.balance



    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance +=amount
            return f" dear {self.amount} you have deposited KES {amount} your new balance is{self.balance}"



    def withdraw(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        elif(amount<self.balance):
            return f"the amount must be less than the balance"
        else:
            self.balance+=amount
            return f"amount reduces the balance"

    def borrow(self,amount):
        if amount<=self.loanLimit:
            return f"you can borrow"
        elif(self.balance<amount):
            return f"you have already an existing loan"
        else:
            self.loan+=1
            self.balance+=amount
            return "you have successfully borrowed"
            




