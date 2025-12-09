from pydantic import EmailStr

class Account:
    def __init__(self, acc_holder_name, balance, address, email):
        self.acc_holder_name : str = acc_holder_name
        self.balance: float = balance
        self.address: str = address
        self.email: EmailStr = email

    def get_balance(self):
        return f"{self.acc_holder_name}'s account balance: {self.balance:.2f}"

    def deposite(self, amt):
        self.balance = self.balance + amt
        print(f'\nDeposite Processing of amount ₹{amt:.2f} ...')
        return self.get_balance()

    def withdrawl(self, amt):
        if self.balance < amt or self.balance == 0.0:
            print("\nInsufficient Funds!!!!")
        else:
            self.balance = self.balance - amt  
            print(f"\nProcessing Withdrawl of amount {amt:.2f} ...")
        return self.get_balance() 
    
    def transfer(self, other, amt):
        print(f"\nInitiating transfer of ₹{amt} from {self.acc_holder_name} to {other.acc_holder_name} ...")
        if self.balance < amt or self.balance == 0.0:
            print("\nERROR!!! Insufficient Funds...")
        else:
            self.balance -=amt
            other.balance += amt
        return f"{self.get_balance()},\n{other.get_balance()}"
    
class InterestRewardAcc(Account):
    """Account that gives 5% interest on each deposite"""
    def deposite(self, amt):
        self.balance += amt * 1.05
        print("Deposite Complted")
        return self.get_balance()

class SavingAccount(InterestRewardAcc):
    """Saving account that will give rewaard on deposite of 5% and take charges of 10"""
    def withdrawl(self, amt):
        charges = 10
        deduction = amt + charges
        self.balance -=deduction
        return self.get_balance()


    
    
