class Rectangle:
  def __init__(self,w,h):
    self.w=w
    self.h=h
  def __str__(self):
    return f"Rectangle(width={self.w}, height={self.h})"
  def set_width(self, w):
    self.w=w
  def set_height(self, h):
    self.h=h
  def get_area(self):
    return self.w*self.h
  def get_perimeter(self):
    return self.w*2+self.h*2
  def get_diagonal(self):
    return (self.w**2+self.h**2)**.5
  def get_picture(self):
    if self.w>50 or self.h>50: return "Too big for picture."
    str1=''
    for i1 in range(self.h):
      str1+='*'*self.w+'\n'
    return str1
  def get_amount_inside(self, r2):
    v1=self.h//r2.h
    h1=self.w//r2.w #vertical and horizontal
    return v1*h1

class Square(Rectangle):
  def __init__(self,s):
    self.w=self.h=s
  def __str__(self):
    return f"Square(side={self.w})"
  def set_side(self,s):
    self.w=self.h=s