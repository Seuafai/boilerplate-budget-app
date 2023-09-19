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
    else:
      return False
# *get_balance - returns current balance based on above methods
  def get_balance(self):
    return self.balance

# *Transfer - accepts amount and another budget catefory as args. refer notes
  def transfer(self, amount, category):
    can_withdraw = self.check_funds(amount)
    
    if can_withdraw:
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
    else:
      return False
         
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
  
# * create_spend_chart - function outside of class. 
#  takes list of categories returns string that is a barchart

def create_spend_chart(categories):
  c = f"Percentage spent by category\n"
  
  totalspend = 0
  cats = {}
  for category in categories:
    catspend = 0
    for item in category.ledger:
      amount = float(item["amount"])
      if amount < 0:      
        catspend += abs(amount)
        totalspend += abs(amount)

    cats[category.name] = catspend
  #print(cats)

  for key, val in cats.items():
    persent = val/totalspend * 100
    persent = round(persent, -1)
    cats[key] = persent
         
  for n in range(100, -1, -10):
    c += f"{str(n) + '|':>4}"
    for val in cats.values():
      if val >= n:
        c += " o "
    c += "\n"

  x = len(cats.values())
  c += f"    {((x*3)+1)* '-':}\n"

  max_name_length = max(len(category.name) for category in categories)

    # Print category names vertically
  for i in range(max_name_length):
      c += "     "
      for category in categories:
          if i < len(category.name):
              c += category.name[i] + "  "
          else:
              c += "   "
      c += "\n"
     
  return c

  
 