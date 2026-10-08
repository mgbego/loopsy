import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, request, jsonify, send_file
from lark import Lark
from lark.exceptions import UnexpectedInput, UnexpectedEOF
from z3 import *
from z3 import And as Z3And
from z3 import Not as Z3Not
from z3 import Solver
from WhileGrammar import while_grammar
from Bad_Input_Guide import bad_input_examples, better_messages
from AST_Lark_Transformer import ConstructAST
from Z3Representation import Z3Converter
from WPLogic import WPLogic, NotAnInv, InvTooWeak, TripleDoesNotHold
#from display_message_toggle import display_message


backend = Flask(__name__, static_folder='.', static_url_path='')
parser = Lark(while_grammar, start=['bexp', 'statement'], parser='earley')

#debug_mode = False  #True
#error handling
def try_parse(text, start_rule, examples, messages, section_name):
   def parse_with_start(text):
      return parser.parse(text, start=start_rule)
   try:
        tree = parser.parse(text, start=start_rule)
        return tree, None
   except UnexpectedEOF as e:
        lines = text.splitlines() or [""]
        #last idx
        last_line = lines[-1] 
        return None, (
            f"[ERROR] ({section_name}): input ended unexpectedly.\n"
            f"The statement is incomplete.\n{last_line}\n"  
         )
   except UnexpectedInput as e:
        if examples and messages:
            label = e.match_examples(parse_with_start, examples)
            if label and label in messages:
               return None, f"[ERROR] ({section_name}) at line {e.line}, column {e.column}: {messages[label]}\n"
              
        return None, f"[ERROR] ({section_name}): syntax error at line {e.line}, column {e.column}\n"
 

@backend.route('/')
def index():
   #return open('index.html').read()
   return open(os.path.join(os.path.dirname(__file__), 'index.html')).read()

@backend.route('/style.css')
def styles():
   return send_file('style.css')

@backend.route('/script.js')
def script():
   return send_file('script.js')

@backend.route('/run', methods=['POST'])
def run():
   code = request.json['code']
   assume = request.json['assume']
   assert_ = request.json['assert_']
   err = []
   #debug_output = []

   assumeTree, assume_err = try_parse(assume, 'bexp', None, None, "Assume")
   if assume_err:
        err.append(assume_err)
        
   # elif debug_mode and assumeTree:
   #      debug_output.append(f"Assume parse tree\n{assumeTree.pretty()}")

   codeTree, code_err = try_parse(code, 'statement', bad_input_examples, better_messages, "Programme")
   #logic only for body, assume assert just check grammar. 
   if code_err:
        err.append(code_err)
   # elif debug_mode and codeTree:
   #      debug_output.append(f"Programme parse tree\n{codeTree.pretty()}")

   assertTree, assert_err = try_parse(assert_, 'bexp', None, None, "Assert")
   if assert_err:
        err.append(assert_err)
   # elif debug_mode and assertTree:
   #      debug_output.append(f"Assert parse tree\n{assertTree.pretty()}")

   output_parts = []
   if err:
        output_parts.append('\n'.join(err))
   else:
         #output_parts.append('No syntax errors detected\n')
      try:
         
         parsed= parse_function(assume, code, assert_)
         output_parts.append(check_triple_function(parsed[0], parsed[1], parsed[2]))
            # result= wp_mechanism(assume, code, assert_)
            # output_parts.append(str(result))
      except (InvTooWeak, NotAnInv, TripleDoesNotHold) as error:
            #msg = str(error)
            #print(msg)
            #, 'error': msg
            output_parts.append(str(error))
   return jsonify({'output': '\n'.join(output_parts)})
           
   # if debug_mode and debug_output:
   #      output_parts.append('\n'.join(debug_output))

   #return jsonify({'output': '\n\n'.join(str(part) for part in output_parts)})

#helpers (essentially prev main broken up)
def parse_function(assume_code, body_code, assert_code):
   parser_s= Lark(while_grammar, start='statement', parser='earley')
   parser_b= Lark(while_grammar, start='bexp', parser='earley')
   ast_assume= ConstructAST().transform(parser_b.parse(assume_code))
   ast_assert= ConstructAST().transform(parser_b.parse(assert_code))
   ast_body= ConstructAST().transform(parser_s.parse(body_code))
   return ast_assume, ast_body, ast_assert 

def check_triple_function(ast_assume, ast_body, ast_assert):
   z3_converter= Z3Converter()
   wp_logic= WPLogic()
   formula_assume = z3_converter.convert_bexp(ast_assume)
   formula_assert = z3_converter.convert_bexp(ast_assert)
   formula_body= wp_logic.stmt_wp(ast_body, formula_assert)
   solver= Solver()
   solver.add(Z3And(formula_assume, Z3Not(formula_body)))
   if solver.check() == sat:
      raise TripleDoesNotHold(solver.model())
   return "Correct"
  
if __name__ == '__main__':
   backend.run(debug=True)
   
