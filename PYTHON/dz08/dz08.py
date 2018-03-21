from BankAccount import *

print("-----------------------------------------------Zadatak-----------------------------------------------")
ba = BankAccount()
ba2 = BankAccount(200)

ba.deposit(300)
ba2.withdraw(100)

print("Trenutno stanje prvog racuna je: {} ".format(ba.get_amount()))
print("Trenutno stanje drugog racuna je: {} ".format(ba2.get_amount()))

