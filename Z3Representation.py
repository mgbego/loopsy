from z3 import * 
from z3 import And as Z3And
from z3 import Or as Z3Or 
from z3 import Not as Z3Not
from z3 import BoolVal
from z3 import IntVal 
from z3 import Int
from AST_Lark_Transformer import * 


class Z3Converter():
   def __init__(self):
      pass
            
   def convert_aexp(self, currnode):
   
      if isinstance(currnode, Num):
         converted_num= IntVal(int(currnode.n)) 
         return converted_num 
      
      elif isinstance(currnode, Variable):
         converted_variable= Int(str(currnode.var))
         return converted_variable
      
         
      elif isinstance(currnode, Sub): 
         left= self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2) 
         converted_sub= left-right
         return converted_sub
      
      elif isinstance(currnode, Add):
         left=self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_add= left+right
         return converted_add 
   
      elif isinstance(currnode, Multi):
         left=self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_multi= left*right
         return converted_multi

   def convert_bexp(self, currnode):
      if isinstance(currnode, TT):
         converted_true= BoolVal(True)
         return converted_true
      elif isinstance(currnode, FF):
         converted_false=BoolVal(False) 
         return converted_false
    
      elif isinstance(currnode, Or):
         left= self.convert_bexp(currnode.b1)
         right=self.convert_bexp(currnode.b2)
         converted_orb= Z3Or(left, right)
         return converted_orb
   
      elif isinstance(currnode, And):
         left= self.convert_bexp(currnode.b1)
         right= self.convert_bexp(currnode.b2)
         converted_andb= Z3And(left, right)
         return converted_andb
      
      elif isinstance(currnode, Not):
         converted_notb= Z3Not( self.convert_bexp(currnode.b))
         return converted_notb
      
      elif isinstance(currnode, Equal):
         left= self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_equal= left == right
         return converted_equal
      
      elif isinstance(currnode, Leq):
         left= self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_leq= left <= right 
         return converted_leq
      
      elif isinstance(currnode, Lt):
         left = self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_lt= left<right
         return converted_lt
      
      elif isinstance(currnode, Gt):
         left= self.convert_aexp(currnode.a1)
         right=self.convert_aexp(currnode.a2)
         converted_gt= left>right
         return converted_gt
      
      elif isinstance(currnode, Geq):
         left= self.convert_aexp(currnode.a1)
         right= self.convert_aexp(currnode.a2)
         converted_geq= left>=right
         return converted_geq
   
