#!/usr/bin/env python3

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Netflix import *
import math

# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----
    '''
    def test_read_1 (self) :
        r = StringIO("1:\nhybhydsbu\n990\n")
        result=netflix_read(r)
        self.assertEqual("1:",result) 

    '''  
    # ----
    # solve
    # ----

    
    def test_solve (self):
        r = StringIO("1:\n23\n78\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:")
            
# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestNetflix      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
