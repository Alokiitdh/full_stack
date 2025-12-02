from Bank_account import Account, InterestRewardAcc, SavingAccount

# we have two accounts instances
Alok = Account(acc_holder_name='Alok',balance=3000, address= 'Chirawa, Jhunjhunu', email='aloklashok@gmail.com' )
Ashok = Account(acc_holder_name='Ashok',balance=6000, address= 'Chirawa, Jhunjhunu', email='ashok@gmail.com' )

print(Alok)
print(Ashok)

print(Alok.get_balance())
print(Ashok.get_balance())


print(Alok.deposite(amt=200))
print(Ashok.deposite(amt=400))

print(Alok.withdrawl(amt=500))
print(Ashok.withdrawl(amt=800))

print(Alok.transfer(other=Ashok,amt=500))

Pankaj = InterestRewardAcc(acc_holder_name='Pankaj',balance=1000, address= 'Chirawa, Jhunjhunu', email='pankaj@gmail.com')
print(Pankaj.get_balance())
print(Pankaj.deposite(100))
print(Pankaj.withdrawl(200))
print(Pankaj.transfer(Alok,200))

Manu = SavingAccount(acc_holder_name='Manu',balance= 1500, address= 'Chirawa, Jhunjhunu', email='manu@gmail.com')
print(Manu.get_balance())
print(Manu.deposite(100))
print(Manu.withdrawl(100))
print(Manu.transfer(Alok,100))



