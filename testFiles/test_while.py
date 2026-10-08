import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
#import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import InvTooWeak, TripleDoesNotHold, NotAnInv


class TestWhile(unittest.TestCase):
   def test_fibonacci_correct(self):
      assume= "n>=0"
      body= "a:=0; b:=1; next_term:=0; while i<n inv(a>=0 && b>0){next_term:=a+b; a:=b;b:=next_term; i:=i+1}"
      assert_= "!(i<n)"
      parsed= parse_function(assume, body, assert_)
      expected_result="Correct"
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
   
   #"conflict?" between how the inner loop and the outer loop change the values
   def test_nested_while_notinv(self):
      assume= "y < 10 && x == y"
      body= "while y < 10 inv(x==y && y<=10) {y:= y+1; while x<y inv (x<=y && y <10) {x:=x+1}}"
      assert_="x==10"
      parsed= parse_function(assume, body, assert_)
      #NotAnInv
      with self.assertRaises(NotAnInv) as ni:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertIn("not correct as it is not preserved", str(ni.exception))
   
   #FAIL because too weak
   #what we get from the terminatiom condition and the invariant does not say anything about
   #the postcondition 
   def test_factorial_tooweak(self):
         assume="n>0"
         #added i:=1 and changed factorial >=1 to i 
         body="factorial:=1; while i>=1 && i<=n inv(factorial>=1) {factorial:=factorial*i;i:=i+1}"
         assert_="factorial>n"
         #InvTooWeak
         parsed= parse_function(assume, body, assert_)
         with self.assertRaises(InvTooWeak) as itw:
            check_triple_function(parsed[0], parsed[1], parsed[2])
         self.assertIn("too weak", str(itw.exception))
   
   #the logic of the triple itself is wrong
   def test_gcd_wrong_triple(self):
      assume="x<10"
      # inv x should be equal to i==0, but precond allows -3, 6, -100 etc, so postcond cannot be guaranteed
      body="i:=0; while i<10 inv(x==i && i<=10) {x:=x+1; i:=i+1}"
      assert_="x<=10"
      parsed= parse_function(assume, body, assert_)
      #TripleWrong
      with self.assertRaises(TripleDoesNotHold) as tdh:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      #print(expcected_result)
      self.assertIn("does not guarantee the postcondition", str(tdh.exception))
       
if __name__ == '__main__':
   unittest.main()
    
