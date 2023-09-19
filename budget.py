# * create_spend_chart - function outside of class. 
#  takes list of categories returns string that is a barchart 

class Category:
#ledger list
  def __init__(self, name):
    self.name = name
    self.balance = 0.00
    self.ledger = []
     
# *deposit - appends to ledger list in form of {"amount": amount, "description": description}
  def deposit(self, amount, description = 1):
    self.balance += amount
    amount = "{:.2f}".format(float(amount))
    if description != 1:
      self.ledger.append({"amount": amount, "description": description})
    else:
      description = ""
      self.ledger.append({"amount": amount, "description": description})
# *withdraw - similar to deposit but neg. num.
#  if not enough funds no ledger entry. Return True if withdrawal occurs. else False
  def withdraw(self, amount, description = 1):
    can_withdraw = self.check_funds(amount)
    amount = "{:.2f}".format(-float(amount))
    #print(amount)
    if can_withdraw:
      self.balance += float(amount)
      if description == 1:
        description = ""
        self.ledger.append({"amount": (amount), "description": description})
      else:
        self.ledger.append({"amount": (amount), "description": description})
     
 # *get_balance - returns current balance based on above methods
  def get_balance(self):
    return self.balance

# *Transfer - accepts amount and another budget catefory as args. refer notes
  def transfer(self, amount, category):
    can_withdraw = self.check_funds(amount)
    
    if can_withdraw:
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
         
# *check_funds
  def check_funds(self, amount):
    if self.balance < float(amount):
      return False
    return True
    
#printversion of ledger
  def __repr__(self):
    p = f"{self.name:*^30}\n"
    
    for category in self.ledger:
      if len(category['description']) > 23:
        category['description'] = category['description'][0:23]
        p += f"{category['description']}{category['amount']:>{30 - len(category['description'])}}\n"
      else:
        p += f"{category['description']}{category['amount']:>{30 - len(category['description'])}}\n"
    p += f"Total: {self.balance}"
    
                
    return p
      
    
    

  

def create_spend_chart(categories):
  pass