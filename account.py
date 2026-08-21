import random


class Account:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def invest(self, amount):
    investment = input("where do you want to invest your money? Select 'S' for S&P 500, 'N' for NASDAQ 'D' for DOW ").strip().upper()
    if investment == "S" or investment == "N" or investment == "D":
      old_balance = self.balance
      self.balance -= amount
      print("investing now")
      if investment == "S":
        self.balance += amount * (1+random.uniform(-0.1, 0.2))
      elif investment == "N":
        self.balance += amount * (1+random.uniform(-0.2, 0.3))
      else:
        self.balance += amount * (1+random.uniform(-0.15, 0.23))
      self.balance = round(self.balance, 2)
      if self.balance <= old_balance:
        print("you suck at investing")
      else:
        print("you're investment succeeded!")
      print(f"your new balance is {self.balance}.")
    else:
      print("please enter a valid investment")

  def deposit(self, amount):
    self.balance += round(amount, 2)
    print(f"your new balance is {self.balance}.")

  def withdraw(self, amount):
    self.balance -= round(amount, 2)
    print(f"your new balance is {self.balance}.")

  def gamble(self, amount):
    old_balance = self.balance
    print("gambling now")
    self.balance -= amount
    gl = random.uniform(-3, 1)
    if gl >= 0:
      self.balance += amount * random.uniform(0, 3)
    else:
      self.balance -= amount * random.uniform(0, 3)
    self.balance = round(self.balance, 2)
    if self.balance <= old_balance:
      print("You have terrible luck")
    else:
      print("Gambling paid off!")
    print(f"your new balance is {self.balance}.")
