from AST_Lark_Transformer import * 
from Z3Representation import Z3Converter
from z3 import * 
#from z3 import Implies
from z3 import substitute 
from z3 import And as Z3And
from z3 import Or as Z3Or 
from z3 import Not as Z3Not
from z3 import Solver
from AST_structures import Skip, Assignment, IfStatement, Sequence, WhileLoop
from display_message_toggle import display_message


#changes convert_stmt to stmt_wp
class WPLogic():
   def __init__(self):
      self.converter= Z3Converter()
    
   def stmt_wp(self, currnode, q):
   
  
      if isinstance(currnode, Skip):
         return q 
       
   
      elif isinstance(currnode, Assignment):
         v= self.converter.convert_aexp(currnode.var)
         e= self.converter.convert_aexp(currnode.expr)
         return substitute(q, (v, e))
      
      elif isinstance(currnode, IfStatement):
         b=self.converter.convert_bexp(currnode.b)
         stmt1= self.stmt_wp(currnode.s1, q)
         stmt2= self.stmt_wp(currnode.s2, q)
         first_part= Z3Or(Z3Not(b), stmt1)
         second_part= Z3Or(b, stmt2)
         return Z3And(first_part, second_part)
      
      elif isinstance(currnode, Sequence):
         nested= self.stmt_wp(currnode.s1, self.stmt_wp(currnode.s2, q))
         return nested
   
      elif isinstance(currnode, WhileLoop):   
         b_= self.converter.convert_bexp(currnode.b)
         invariant= self.converter.convert_bexp(currnode.inv)
         wp_s= self.stmt_wp(currnode.s, invariant)
         
         not_wp_s_i= Z3Not(self.stmt_wp(currnode.s, invariant))
         and_i= Z3And(invariant, not_wp_s_i)
         final_incorrect= Z3And(b_, and_i)

         i_and_not_q= Z3And(invariant, Z3Not(q))
         final_too_weak= Z3And(Z3Not(b_), i_and_not_q)
      
         checkwrong1= self.error_checker(final_incorrect)
         checkwrong2= self.error_checker(final_too_weak)
         if (checkwrong1[0]==sat):
            not_an_inv= NotAnInv(invariant, checkwrong1[1], b_, wp_s, currnode.s)
            raise not_an_inv
         if (checkwrong2[0]==sat):
            inv_too_weak= InvTooWeak(invariant, checkwrong2[1], b_, q, currnode.s)
            raise inv_too_weak 
         return invariant
             
   def error_checker(self, statement):
      solver= Solver()
      solver.add(statement)
      result=solver.check()
      
      if(result == sat):
         model=solver.model()
      else:
         model=None 
         
      return result, model
   
class NotAnInv(Exception):
    def __init__(self, inv, model, loop_condition, req_wp, statement):
         self.statement=statement
         self.inv=inv
         inv= str(inv)
         self.model=model
         model=str(model)
         self.loop_condition= loop_condition
         loop_condition= str(loop_condition)
         self.req_wp= req_wp
         req_wp= str(req_wp)
         message_no_help = (f'[ERROR] The supplied invariant is not correct as it is not preserved by the loop body.\n')
         
         message_help= (f'[ERROR] The supplied invariant is not correct as it is not preserved by the loop body.\n'
                         f'Invariant: {inv}\n'
                         f'Loop Condition: {loop_condition}\n'
                         f'Required wp: {req_wp}\n'
                         f'{inv} && {loop_condition} does not imply {req_wp}\n'
                         f'An example value that breaks the correctness:\n{model}\n'
                        )
         message_no_help=str(message_no_help)
         message_help= str(message_help)
         if display_message()== True:
            super().__init__(message_help)
         else:
            super().__init__(message_no_help)
 
           
class InvTooWeak(Exception):
    def __init__(self, inv, model, loop_condition, postcondition, statement):
        self.inv = inv
        inv= str(inv)
        self.model = model
        model= str(model)
        self.loop_condition = loop_condition
        loop_condition= str(loop_condition)
        self.postcondition = postcondition
        postcondition= str(postcondition)
        self.statement = statement
        statement= str(statement)
        message_no_help= (f'[ERROR] The supplied invariant is too weak for this loop.\n')
        
        message_help = (f'[ERROR] The supplied invariant is too weak for this loop.\n'
            f'Invariant: {inv}\n'
            f'Exit condition: !({loop_condition})\n'
            f'Postcondition: {postcondition}\n'
            f'{inv} && !({loop_condition}) does not imply {postcondition}\n'
            f'An example value that breaks the correctness:\n{model}\n'
         )
        message_no_help= str(message_no_help)
        message_help=str(message_help)
        if display_message()==True:
           super().__init__(message_help)
        else:
           super().__init__(message_no_help)
   
class TripleDoesNotHold(Exception):
   def __init__(self, model):
      self.model=model
      model= str(model)
      message_no_help= (f'[ERROR] The precondition P does not guarantee the postcondition Q\n')
      message_help= (f'[ERROR] The precondition P does not guarantee the postcondition Q\n'
                       f'An example value that breaks the correctness: \n{model}\n')
      message_no_help=str(message_no_help)
      message_help= str(message_help)
      if display_message()==True:
         super().__init__(message_help)
      else:
         super().__init__(message_no_help)
   
   
