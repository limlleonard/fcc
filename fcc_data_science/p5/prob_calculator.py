import copy
import random
# Consider using the modules imported above.
def d2l(dct1): #{'a':1, 'b':2} -> [a,b,b]
  lst1=[]
  for k1 in dct1:
    for _ in range(dct1[k1]):
      lst1.append(k1)
  return lst1
def l2d(lst1):
  dct1={}
  for i in lst1:
    if i in dct1:
      dct1[i]+=1
    else: dct1[i]=1
  return dct1
class Hat:
  def __init__(self, **kwargs):
    self.contents=d2l(kwargs)
  def draw(self, num):
    if num>len(self.contents): return self.contents
    drawn=random.sample(self.contents, num)
    for rm in drawn: self.contents.remove(rm)
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  hit=0
  for _ in range(num_experiments):
    hatcp=copy.deepcopy(hat)
    lst_drawn=hatcp.draw(num_balls_drawn) #list, have to compare to a dict
    dct_drawn=l2d(lst_drawn)
    flag=1
    for k1 in expected_balls:
      if k1 in dct_drawn:
        if expected_balls[k1]<=dct_drawn[k1]:
          continue
      flag=0
      break
    hit+=flag
  return round(hit/num_experiments, 3)