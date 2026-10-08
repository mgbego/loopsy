
#aexp 
class Num:
   def __init__ (self, n):
      self.n=n 
   def __repr__ (self):
      return f"Numeral({self.n})"
   

class Variable:
   def __init__ (self, var):
      self.var=var
   def __repr__(self):
      return f"Variable({self.var})"
      
class Add: 
   def __init__(self, a1, a2):
      self.a1=a1
      self.a2=a2
      
   def __repr__(self):
      return f"Adding({self.a1}, {self.a2})"

class Multi:
   def __init__ (self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Multiplying({self.a1}, {self.a2})"


class Sub:
   def __init__ (self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Subtracting({self.a1}, {self.a2})"
   
#bexp
class TT:
   pass
   def __repr__(self):
      return "True"

class FF:
   pass
   def __repr__(self):
      return "False"
   
   
class Equal:
   def __init__(self, a1, a2):
      self.a1=a1
      self.a2=a2
      
   def __repr__(self):
      return f"Equal({self.a1}, {self.a2})"

class Leq:
   def __init__(self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Less than or equal to({self.a1}, {self.a2})"


class And:
   def __init__(self, b1, b2):
      self.b1=b1
      self.b2=b2
   def __repr__(self):
      return f"And({self.b1}, {self.b2})"

class Or:
   def __init__(self, b1, b2):
      self.b1=b1
      self.b2=b2
   def __repr__(self):
      return f"Or({self.b1}, {self.b2})"

class Not:
   def __init__(self, b):
      self.b=b
   def __repr__(self):
      return f"Not({self.b})"

class Lt:
   def __init__ (self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Less than({self.a1}, {self.a2})"

class Gt:
   def __init__(self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Greater than({self.a1}, {self.a2})"

class Geq:
   def __init__(self, a1, a2):
      self.a1=a1
      self.a2=a2
   def __repr__(self):
      return f"Greater than or equal to({self.a1}, {self.a2})"

#S   
class Skip:
   pass
   def __repr__(self):
      return f"Skip"
   
class Assignment: 
   def __init__ (self, var, expr):
      self.var= var
      self.expr= expr 
   def __repr__(self):
      return f"Assignment({self.var}, {self.expr})"

class Sequence:
   def __init__(self, s1, s2):
      self.s1= s1
      self.s2= s2 
   def __repr__(self):
      return f"Sequence({self.s1}, {self.s2})"

class IfStatement:
   def __init__ (self, b, s1, s2):
      self.b=b
      self.s1=s1
      self.s2=s2
   def __repr__(self):
      return f"If({self.b}, {self.s1}, {self.s2})"
      

class WhileLoop:
   def __init__ (self, b, inv, s):
      self.b= b
      self.inv= inv
      self.s= s 
   
   def __repr__ (self):
      return f"While({self.b}, {self.inv}, {self.s})"
   
