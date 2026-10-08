import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 
#import Main
from runFiles.run import check_triple_function
from runFiles.run import parse_function
from WPLogic import InvTooWeak, TripleDoesNotHold


class TestBranching(unittest.TestCase):
   def test_abs_val_correct(self):
      assume= "true"
      body= "if x<0 {y:=0-x} else {y:=x}"
      assert_= "y>=0"
      parsed= parse_function(assume, body, assert_)
      expected_result="Correct"
      self.assertEqual(str(check_triple_function(parsed[0], parsed[1], parsed[2])), expected_result)
   
   #cannot include any value comparisons in inv because they are being swapped all the time 
   #so inv would need to keep track of all of them 
   def test_bubble_sort_wrong(self):
      assume="n1==9 && n2==20 && n3==1 && n4==3"
      body="i:=0; while i<3 inv (true) {if n1>n2 {t:=n1; n1:=n2; n2:=t} else {skip}; if n2>n3 {t:=n2; n2:=n3; n3:=t} else {skip}; if n3>n4 {t:=n3; n3:=n4; n4:=t} else {skip}}"
      assert_="n1==1 && n2==3 && n3==9 && n4==20"
      parsed= parse_function(assume, body, assert_)
      with self.assertRaises(InvTooWeak) as itw:
         check_triple_function(parsed[0], parsed[1], parsed[2])
      self.assertNotIn("Correct", str(itw.exception))
      self.assertIn("too weak", str(itw.exception))
      
   def test_bubble_sort_correct(self):
      assume = "n1==9 && n2==20 && n3==1 && n4==3"
      body = ("if n1>n2 {t:=n1; n1:=n2; n2:=t} else {skip}; if n2>n3 {t:=n2; n2:=n3; n3:=t} else {skip}; if n3>n4 {t:=n3; n3:=n4; n4:=t} else {skip}; if n1>n2 {t:=n1; n1:=n2; n2:=t} else {skip}; if n2>n3 {t:=n2; n2:=n3; n3:=t} else {skip}; if n3>n4 {t:=n3; n3:=n4; n4:=t} else {skip}")
      assert_ = "n1==1 && n2==3 && n3==9 && n4==20"
      parsed= parse_function(assume, body, assert_)
      expected_result=str(check_triple_function(parsed[0], parsed[1], parsed[2]))
      self.assertEqual(expected_result, "Correct")
   
   def test_score_wrong(self):
      assume="score==70"
      body="if score<49 {result:=fail} else {if score>=49 && score <65 {result:=pass} else {if score>=65 && score <70 {result:=merit} else {if score>70 && score<=100 {result:=distinction} else {result:=unknown}}}}"
      assert1="result==distinction"
      parsed1= parse_function(assume, body, assert1)
      assert2="result==unknown"
      parsed2= parse_function(assume, body, assert2)
      
      with self.assertRaises(TripleDoesNotHold) as tdh:
        str(check_triple_function(parsed1[0], parsed1[1], parsed1[2]))
        
      self.assertNotIn("Correct", str(tdh.exception))
      expected_result2= str(check_triple_function(parsed2[0], parsed2[1], parsed2[2]))
      self.assertEqual("Correct", expected_result2)
            
if __name__ == '__main__':
   unittest.main()
    
