# This is the code to manage the user's accounts
from account import Account

def float_check(a):
   while True:
      try:
        a=float(a)
        return a
      except ValueError:
        a = input("Please format the number correctly! Try again: ")
  

def account_manager(account):
  a = input("What would you like to do? ")
  if a == 'I':
    amount = input("How much would you like to invest? Please type just the number: ")
    while True:
      try:
        amount = float(amount)
        break
      except ValueError:
        amount = input("Please format the number correctly! Try again: ")
    while True:
      if amount < account.balance:
        break
      else:
        amount = input(f"Not enough balance! Your current balance is {account.balance} Try again: ")
    amount = round(amount, 2)
    account.invest(amount)
  elif a == "D":
    amount = input("How much would you like to deposit? Please type just the number: ")
    while True:
      try:
        amount = float(amount)
        break
      except ValueError:
        amount = input("Please format the number correctly! Try again: ")
    amount = round(amount, 2)
    account.deposit(amount)
  elif a == "W":
    amount = input("How much would you like to withdraw? Please type just the number: ")
    while True:
      amount = float_check(amount)
      if amount < account.balance:
        break
      else:
        amount = input(f"Not enough balance! Your current balance is {account.balance} Try again: ")
    amount = round(amount, 2)
    account.withdraw(amount)
  elif a == "G":
    amount = input("How much would you like to gamble? Please type just the number: ")
    while True:
      try:
        amount=float(amount)
        break
      except ValueError:
        amount = input("Please format the number correctly! Try again: ")
    while True:
      if amount < account.balance:
        break
      else:
        amount = input(f"Not enough balance! Your current balance is {account.balance} Try again: ")
    amount = round(amount, 2)
    account.gamble(amount)
  elif a == 'Q':
    return False
  else:
    input("To invest, press 'I'. To deposit, press 'D'. To withdraw, press 'W'. To gamble, press 'G'. To quit, press 'Q'.")
    
    
    
  

def main():
  print("Welcome to the Account Manager!")
  print("-----------------------------------------")
  name = input("To create your account, first type in the account name: ")
  balance = input("Now, type in your current balance as a number without dollar signs: ")
  while True:
    try:
      balance = float(balance)
      break
    except ValueError:
      balance = input("Please format the number correctly! Try again: ")
  balance = round(balance,2)
  user = Account(name, balance)
  print(f"Your account name is {name} and its current balance is ${balance}")
  print("To invest, press 'I'. To deposit, press 'D'. To withdraw, press 'W'. To gamble, press 'G'. To quit, press 'Q'. ")
  while True:
    account_manager(user)
  print("Thank you!")

main()
