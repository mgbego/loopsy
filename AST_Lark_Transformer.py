from AST_structures import * 
from AST_structures import Sequence
from lark import Transformer 


class ConstructAST(Transformer):
   def n(self, args):
      return Num(args[0])
   
   def variable(self, args):
      return Variable(args[0])
   
   def add(self, args):
      return Add(args[0], args[1])
   
   def multi(self, args):
      return Multi(args[0], args[1])
    
   def sub(self, args):
      return Sub(args[0], args[1])
   
   def bracket_exp(self, args):
      return (args[0])
   
   #bool exp
   def true_b(self, args):
      return TT() 
   
   def false_b(self, args):
      return FF()
   
   def eq(self, args):
      return Equal(args[0], args[1])
   
   def leq(self, args):
      return Leq(args[0], args[1])
   
   def and_b(self, args):
      return And(args[0], args[1])
   
   def or_b(self,args):
      return Or(args[0], args[1])
   
   def not_b(self, args):
      return Not(args[0])
   
   def lt(self, args):
      return Lt(args[0], args[1])
   
   def gt(self, args):
      return Gt(args[0], args[1])
   
   def geq(self, args):
      return Geq(args[0], args[1])
   
   def bracket_b(self, args):
      return (args[0])
   
   def skip (self, args):
      return Skip()
   
   def assign(self, args):
      return Assignment(args[0], args[1])
   
   def sequence(self, args):
      return Sequence(args[0], args[1])
    
   def if_statement(self, args):
      return IfStatement(args[0], args[1], args[2])
   
   def while_loop(self, args):
      return WhileLoop(args[0], args[1], args[2])
   

