# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:14:06 2022

@author: sande
"""

#setting up the custom object

class Purchase(object):
  def __init__(self, amount):
    self.amount = amount

  def  calculateTax(self, taxPercent):
      return self.amount * taxPercent/100.0

  def calculateTip(self, tipPercent):
     return self.amount * tipPercent/100.0

  def calculateTotal(self, taxPercent, tipPercent):
    return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

#create purchase object given an amount

purchase = Purchase(100.0)

#set tax and tip %

taxPercent = 7.5
tipPercent = 20.0

#use object to calculat tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#display info

print('Tax:', tax)
print('Tip:', tip)
print('Total:', purchase.calculateTotal(taxPercent, tipPercent))