#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = None

  def add_item(self,title,price,quantity = 1):
    for _ in range(quantity):
            self.items.append(title)
    transaction_amount = price * quantity
    self.total += transaction_amount
    self.last_transaction = transaction_amount


  def apply_discount(self):
    if self.discount > 0:
        self.total -= self.total * (self.discount / 100)
        if isinstance(self.total, float):  # Check if the total is a float
            self.total = int(self.total)  # Convert total to an integer

        print(f"After the discount, the total comes to ${self.total}.")
    else:
        print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.last_transaction is not None:  # Check if last_transaction is set
            self.total -= self.last_transaction
            self.last_transaction = None
            return self.total