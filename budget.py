# * create_spend_chart - function outside of class. 
#  takes list of categories returns string that is a barchart 

class Category:
#ledger list
  def __init__(self, name):
    self.name = name
    self.balance = 0.00
    self.ledger = []
    #print(self.name, self.ledger)
     
# *deposit - appends to ledger list in form of {"amount": amount, "description": description}
  def deposit(self, amount, description):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})
    #print(self.ledger)
      
# *withdraw - similar to deposit but neg. num.
#  if not enough funds no ledger entry. Return True if withdrawal occurs. else False
  def withdraw(self, amount, description = 1):
    if self.balance < amount:
      return False
      pass
    else:
      return True
      self.balance -= amount
    if description == 1:
      description = ""
      self.ledger.append({"amount": amount, "description": description})
      print(self.ledger)
    else:
      self.ledger.append({"amount": amount, "description": description})
      print(self.ledger)
 # *get_balance - returns current balance based on above methods
  def get_balance(self):
    return self.balance

# *Transfer - accepts amount and another budget catefory as args. refer notes
  def transfer(self, amount, category):
    pass
# *check_funds - refer notes
  #def check_funds(self):
    




#def create_spend_chart(categories):