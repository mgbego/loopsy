import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
#import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import TripleDoesNotHold

class TestBexp(unittest.TestCase):
   def test_bexp_correct(self):
      assume= "z>0 && x<0 && y<0 && j<0-1 && i==0"
      body= "skip"
      assert_= "x>0 || (y<0 && z>0 && (j>=0 || i>=0))"
      expected_result= "Correct"
      parsed= parse_function(assume, body, assert_)
      
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
   
   #a implies b: not a or b    
   def test_implication_correct(self):
      assume= "a>5 && b<0 && c==0"
      body= "skip"
      assert_= "a<5 || b<0 && c==0" #need to add ! for implication
      parsed= parse_function(assume, body, assert_)
      expected_result= str(check_triple_function(parsed[0], parsed[1], parsed[2]))
      self.assertEqual("Correct", expected_result)
     
   def test_bexp_incorrect(self):
      assume="true"
      body="x:=x*x*x; if x>=0 {result:=1} else {result:=0-1}"
      assert_="result>0"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(TripleDoesNotHold) as tdh:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      #TripleWrong
      self.assertIn("does not guarantee the postcondition", str(tdh.exception))
      

if __name__ == '__main__':
   unittest.main()
    