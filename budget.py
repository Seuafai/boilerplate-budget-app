class Category:
#ledger list
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.ledger = []
     
# *deposit - appends to ledger list in form of {"amount": amount, "description": description}
  def deposit(self, amount, description = ""):
    
    self.balance += amount
    
    self.ledger.append({"amount": amount, "description": description})
   
# *withdraw - similar to deposit but neg. num.
#  if not enough funds no ledger entry. Return True if withdrawal occurs. else False
  def withdraw(self, amount, description=""):
    can_withdraw = self.check_funds(amount)
   
    if can_withdraw:
        self.balance -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True
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
        #print(self.ledger)
        return True
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
      amount = category['amount']
      #print(amount)
      description = category['description']
      formatted_amount = "{:.2f}".format(amount)
      if len(description) > 23:
        description = description[:23]
      p += f"{description}{formatted_amount:>{30 - len(description)}}\n"
    formatted_balance = "{:.2f}".format(self.balance)  # Format the balance with two decimal places
    p += f"Total: {formatted_balance}"
    return p
  
# * create_spend_chart - function outside of class. 
#  takes list of categories returns string that is a barchart

def create_spend_chart(categories):
  
  c = f"Percentage spent by category\n"
  
  totalspend = 0
  cats = {}
  for category in categories:
    catspend = int(0)
    for entry in category.ledger:
      
      amount = entry["amount"]
      amount = float(amount)
      
      if amount < 0:      
        catspend += amount
        totalspend += amount
      

    cats[category.name] = catspend
    

  # Check if totalspend is zero to avoid division by zero
  
    #print(totalspend)
  for key, val in cats.items():
    
    #print(val) 
    percent = round((val/totalspend)*100)
    
    cats[key] = percent
        
  for n in range(100, -1, -10):
    c += f"{str(n) + '|':>4}"
    for val in cats.values():
      if val >= n:
        c += " o "
      else:
        c += "   "
    c += " \n"

  x = len(cats.values())
  c += f"    {((x*3)+1)* '-':}\n"

  max_name_length = max(len(category.name) for category in categories)

    # Print category names vertically
  for i in range(max_name_length):
    c += "    "
    for category in categories:
        if i < len(category.name):
            c += f" {category.name[i]} "
        else:
            c += "   "
    if i != max_name_length -1:
      c += " \n"
    else:
      c += " "

  return c

