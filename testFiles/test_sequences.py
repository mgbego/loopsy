import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
#import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import TripleDoesNotHold, NotAnInv, InvTooWeak
 
class TestSequnces(unittest.TestCase):
   def test_sequence_correct(self):
      assume= "i==0 && s==0 && n==5"
      body= "while i<n inv (s==i && i>=0 && i<=n) {i:=i+1; s:=s+1}"
      assert_= "s==n"
      parsed= parse_function(assume, body, assert_)
      expected_result="Correct"
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
  
   def test_swap_swap_wrong(self):
      assume="i==6 && j==5"
      #missing j=t so incorrect swap
      #t=6 i=5 t=11 j=6 i=6 
      #t:=i; i:=j; j:=t; t:=i+j; j:=t-j; i:=t-i
      #t=6 i=5 j=6 t=11 j=5 i=6
      body= "t:=i; i:=j; t:=i+j; j:=t-j; i:=t-i"
      assert_= "i==6 && j==5"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(TripleDoesNotHold) as tdh:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertIn("does not guarantee the postcondition", str(tdh.exception))
      
   def test_seq_too_weak(self):
      assume= "x==0 && y==0"
      body= "while y<28 inv(x==y) {y:=y+2; while x<y inv(x<=y) {x:=x+1}}"
      assert_= "x==28"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(InvTooWeak) as itw:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertIn("too weak", str(itw.exception))
   
   def test_seq_not_inv(self):
      assume="i==1 && j==0"
      body="while i<20 inv (i>j) {i:=i+1; j:=j+2}"
      assert_="i>j"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(NotAnInv) as ni:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertIn("not correct as it is not preserved", str(ni.exception))
      
if __name__ == '__main__':
   unittest.main()
    