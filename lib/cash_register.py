#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items_detailed = []
    self.items = []

  def add_item(self, item_name, unit_price, quantity=1):
    self.items_detailed.append((item_name, unit_price, quantity))

    for i in range(quantity):

      self.items.append(item_name)
    self.total += (unit_price * quantity)

  def apply_discount(self):
    if not self.discount:
      print("There is no discount to apply.")
    else:
      discounted_total = (1 - (self.discount / 100)) * self.total
      self.total = discounted_total
      print(f"After the discount, the total comes to ${int(self.total)}.")
    
  def void_last_transaction(self):
    last_item_total = self.items_detailed[-1][1] * self.items_detailed[-1][2]
    self.total -= last_item_total

   


