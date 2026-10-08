
bad_input_examples = {
   "missing_curly_braces": [
      "if x>0 x:=0 else {y:=1}",   
      "if true x:=1 else {y:=0}",     
      "if x>0 {x:=1} else x:=0",
      "while x<10 inv (x>0) x:=x+1",
   ],
    
   "extra_keywords_symbols": [
      "if x>0 {x:=100} else do {x:=0}",
      "if x>0 then {x:=100} else {x:=0}",
      "while x<9 inv (x>0 then {x:=y*y})",
      "if z>=0 and y>0",
      "while y>0 or x>0 ",
      "if x>0: {y:=y-1} else {z:=z*z*z}",
      'while (y<=z) "inv" (y<=z && y<n) {z:=z*y; y:=y+2}',
   ],
   "unclosed_brace": [
      "if true {x:=1 else y:=0}",
      "if true {x:=1} else {y:=0",
      "if true {x:=1 else {y:=0}",
   ],
   "incomplete_comparison": [
      "x>= ",
      "if x<= {skip} else {skip}",
      "y==",
      ">",
      "<",
      "=",
      "!=",
   ],
   "incomplete_assignments": [
      "x:=",
      "y:=",
      "variable:=",
      "+=",
      "-=",
      "*=",
   ],
   "incomplete_statements": [
      "if",
      "while",
      "else",
      "inv",
   ],
    
   "missing_semicolon": [
      "x:=1 y:=2",
      "skip; skip x:=y",
      "while x<0 inv (x==4) {x:=1 x:=3}"
   ],
   "problem_inv": [
      "while x<5 {x:=x+1}",
      "while x>0 inv a>=b {a:=a+1}"
   ],
   "unclosed_paren":[
      "z:=0 && (x>0 || (y<0 && a<0)",
       
   ], 
}

better_messages = {
   "missing_curly_braces": "Missing curly braces",
   "extra_keywords_symbols": "Extra unsupported keyword(s) or symbol(s) in the programme",
   "unclosed_brace": "Make sure all open braces '{' have a corresponding closing one '}'",
   "incomplete_comparison": "Comparison is incomplete or unsupported operators have been used. Check the operator. Make sure it is allowed and that there are no missing values",
   "incomplete_assignments": "Assignment is incomplete or unsupported operators have been used. Make sure there are values on both sides of the operator and that the operator is allowed",
   "incomplete_statements": "Missing the rest of the statement",
   "missing_semicolon": "Missing semicolon",
   "problem_inv": "Make sure the loop invariant is supplied and wrapped in parentheses",
   "unclosed_paren": "Make sure all open parentheses '(' have a corresponding closing one ')'",
}


 