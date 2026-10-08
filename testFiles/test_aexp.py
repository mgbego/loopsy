import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
# import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import TripleDoesNotHold

class TestAexp(unittest.TestCase):
   def test_aexp_branch_correct(self):
      assume="x==4 && y==3 && z==2"
      body="if x-y*z>0 {r:=1} else {r:=0}"
      assert_="r==0"
      parsed= parse_function(assume, body, assert_)
      expected_result= str(check_triple_function(parsed[0], parsed[1], parsed[2]))
      #expected_result= str(Main.wp_mechanism(assume, body, assert_))
      self.assertSequenceEqual("Correct", expected_result)
   
   def test_aexp_operations_correct(self):
      assume="a==10 && c==20"
      body="result:=a+c*a-c*a*a"
      assert_="result<0"
      parsed= parse_function(assume, body, assert_)
      self.assertEqual("Correct", str(check_triple_function(parsed[0], parsed[1], parsed[2])))
   
   def test_aexp_incorrect(self):
      assume= "d==6 && e==3 && f==9"
      body= "result:=d+e-f+e-f+d+e-f+d+e-f+d+e-f+1*2"
      assert_= "result==2" 
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(TripleDoesNotHold) as tdh:
         #expected_result= 
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertIn("does not guarantee", str(tdh.exception))
      #print(expected_result)
      self.assertNotIn("Correct", str(tdh.exception))
   
   def test_aexp_precedence_correct(self):
     assume= "x==10 && y==3 && z==2"
     body= "result:= x*y+z*x-y-z*3"
     assert_= "result==41" #was 53
     parsed= parse_function(assume, body, assert_)
     expected_result= str(check_triple_function(parsed[0], parsed[1], parsed[2]))
     self.assertEqual("Correct", expected_result)

      
if __name__ == '__main__':
   unittest.main()