import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
#import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import TripleDoesNotHold

#only correct and wrong triple
class TestAssignment(unittest.TestCase):
   def test_assignment_composite_correct(self):
      assume="x==5 && y==3"
      body="x:=x*x*y; y:=x+1; z:=y*10"
      assert_="z==760"
      parsed= parse_function(assume, body, assert_)
      expected_result="Correct"
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
   #swapping vars
   def test_assignment_swap_correct(self):
      assume="m==7 && n==1 && k==10 && l==4"
      body="t1:=0; t2:=0; t1:=m; m:=l; t2:=n; n:=t1; t1:=k; k:=t2; l:=t1"
      assert_="m==4 && n==7 && k==1 && l==10"
      parsed= parse_function(assume, body, assert_)
      expected_result="Correct"
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
      
   def testing_assignment_swap_wrong(self):
      assume= "x==5"
      body= "x:=0; y:=x"
      assert_= "y==5 && x==0"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(TripleDoesNotHold) as tdh:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      #WrongTriple
      self.assertNotIn("Correct", str(tdh.exception))
      self.assertIn("does not guarantee the postcondition", str(tdh.exception))
      

if __name__ == '__main__':
   unittest.main()