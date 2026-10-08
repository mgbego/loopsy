import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest 


from test_branching import *
from test_while import *
from test_bexp import *
from test_sequences import *
from test_assignment import *
from test_aexp import *



if __name__ == '__main__':
   unittest.main()

