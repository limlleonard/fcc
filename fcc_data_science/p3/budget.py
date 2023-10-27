class Category:
  def __init__(self, name):
    self.name = name
    self.ledger=[]
  def deposit(self, amount, description=''):
    self.ledger.append({'amount':amount, 'description':description})
  def get_balance(self):
    b1=0
    for ledg in self.ledger:
      b1+=ledg['amount']
    return b1
  def get_spend(self):
    b1=0
    for ledg in self.ledger:
      if ledg['amount']<0:
        b1+=ledg['amount']
    return b1
  def check_funds(self, amount):
    if amount>self.get_balance(): return False
    else: return True
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount':-amount, 'description':description})
      return True
    else: return False
  def transfer(self, amount, cat2):
    #check if budget is enough
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {cat2.name}')
      cat2.deposit(amount, f'Transfer from {self.name}')
      return True
    else: return False
  def __str__(self):
    def f23(str1):
      if len(str1)>23: return str1[:23]
      else: return str1+' '*(23-len(str1))
    def f7(num):
      strn='{:0.2f}'.format(num)
      if len(strn)<7: return ' '*(7-len(strn))+strn
      else: return strn
    def stern(str1):
      len2=30-len(str1)
      str2='*'*(len2//2) + str1 + '*'*(len2//2)
      if len(str2)<30: str2+='*'
      str2+='\n'
      return str2
    str1=stern(self.name)
    for ledg in self.ledger:
      str1+=f23(ledg['description'])
      str1+=f7(ledg['amount'])+'\n'
    str1+=f'Total: {self.get_balance()}'
    return str1
def create_spend_chart(categories):
  str1='Percentage spent by category\n'
  len1=len(categories)
  # calculate percentage
  lst_sp=[cat1.get_spend() for cat1 in categories]
  summe=sum(lst_sp)
  lst_per=[round(num/summe*100 -5, -1) for num in lst_sp]
  # to match unittest, which round down, -5
  for i in range(100, -10, -10):
    if i==100: str1+=str(i)
    elif i==0: str1+='  '+str(i)
    else: str1+=' '+str(i)
    str1+='|'
    for per in lst_per:
      if per>=i: str1+=' o '
      else: str1+='   '
    str1+=' \n'
  str1+=' '*4+'-'*(3*len1+1)+'\n'
  lst_nm=[cat1.name for cat1 in categories]
  long_nm=max([len(i) for i in lst_nm])
  for i in range(long_nm):
    str1+=' '*4
    for nm in lst_nm:
      if i<len(nm): str1+=' '+nm[i]+' '
      else: str1+=' '*3
    str1+=' \n'
  return str1[:-1]