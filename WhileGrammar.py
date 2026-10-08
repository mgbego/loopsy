
while_grammar = """
   
   statement: variable ":=" aexp -> assign
         | "skip" -> skip
         | statement ";" statement -> sequence
         | "if" bexp "{" statement "}" "else" "{" statement "}" -> if_statement
         | "while" bexp "inv" "(" bexp ")" "{" statement "}" -> while_loop
   
   ?aexp: aexp "-" term -> sub
         | aexp "+" term -> add
         | term
         
   ?term: term "*" factor -> multi
         | factor
   
   ?factor: INT -> n
         | variable 
         | "("aexp")"
   
   bexp: "false" -> false_b
         | "true" -> true_b
         
         
         | bexp "||" bexp -> or_b
         | bexp "&&" bexp -> and_b
         | "!" bexp -> not_b
         
         
         | aexp "==" aexp -> eq 
         | aexp "<" aexp -> lt
         | aexp ">" aexp -> gt
         | aexp "<=" aexp -> leq
         | aexp ">=" aexp -> geq
         
         | "("bexp")" -> bracket_b
         
   !variable: /_?[a-z][a-zA-Z0-9_]*/
   %import common.INT 
   %import common.WS
   %ignore WS   
"""
