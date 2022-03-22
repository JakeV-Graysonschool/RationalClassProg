import math

class Rational():
  def __init__(self,numer,denom):
    self.numer = int(numer)
    self.denom = int(denom)
    self.reduce()
    
  def reduce(self):
    reduction_factor = math.gcd(self.numer, self.denom)
    self.numer = self.numer//reduction_factor
    self.denom = self.denom//reduction_factor
    if self.denom < 0:
      self.denom = abs(self.denom)
      self.numer *= -1

  def __repr__(self):
    return "{}/{}".format(self.numer,self.denom)

  def invert(self):
    return Rational(self.denom, self.numer)

  def __neg__(self):
    return Rational(-self.numer,self.denom)
  
  def __add__(self,other):
    if type(self) == int:
      self = Rational(self,1)
    if type(other) == int:
      other = Rational(other,1)
    return Rational(self.numer*other.denom+other.numer*self.denom, self.denom*other.denom)

  def __sub__(self,other):
    return self+ -other

  def __mul__(self,other):
    if type(other) == int:
      other = Rational(other,1)
    return Rational(self.numer*other.numer, self.denom*other.denom)

  def __truediv__(self,other):
    if type(other) == int:
      other = Rational(other,1)
    return self*other.invert()

  def __radd__(self, other):
    return self+other

  def __rsub__(self, other):
    return -self+other
  
  def __rmul__(self, other):
    return self*other

  def __rtruediv__(self, other):
    return self.invert() * other

  def __float__(self):
    return self.numer/self.denom

  def __int__(self):
    return self.numer//self.denom
    
  def __str__(self):
    return str(self.numer) + "\n" + ("-"*len(str(self.denom))) + "\n" + str(self.denom)

def g_rat(n):
  start_guess = Rational(1,1)
  for m in range(0,n):
    next_guess = 1 + 1/start_guess
    start_guess = next_guess
  return next_guess
  
def main():
  two_thirds = Rational(-2,-3)
  expart_a = Rational(4,2)
  expart_b = Rational(2,1)
  smart_alec_answer = " 1+√(5)\n--------\n   2"
  print(expart_a / expart_b * two_thirds)
  print(g_rat(150))
if __name__ == "__main__":
  main()