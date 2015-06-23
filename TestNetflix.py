#!/usr/bin/env python3

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Netflix import *
import math
import json
from urllib.request import urlopen

urlamr = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")
urlavr = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
urlpps = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")

average_m_cache = json.loads(urlamr.read().decode(urlamr.info().get_param('charset') or 'utf-8'))
average_v_cache = json.loads(urlavr.read().decode(urlavr.info().get_param('charset') or 'utf-8'))

totalavg = 3.674130451108032
# -----------
# TestCollatz
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----
    
    def test_read_1 (self) :
        r = StringIO("1:\nhybhydsbu\n990\n")
        result=netflix_read(r)
        self.assertEqual("1:",result) 
    def test_read_2 (self) :
        r = StringIO("54:        \n88481\n541\n")
        result=netflix_read(r)
        self.assertEqual("54:",result) 
    def test_read_3 (self) :
        r = StringIO("10:\t\t\n6854\n815\n")
        result=netflix_read(r)
        self.assertEqual("10:",result) 
    def test_read_4 (self) :
        r = StringIO("2450\n849\nbob\n")
        result=netflix_read(r)
        self.assertEqual("2450",result) 
    def test_read_5 (self) :
        r = StringIO("0")
        result=netflix_read(r)
        self.assertEqual("0",result) 

 
    # -----
    # predict
    # -----
    
    def test_predict_1 (self):
        w = StringIO()
        netflix_predict("1", "2529547", w, totalavg)
        self.assertEqual(w.getvalue(), "4.0\n")
    

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print("1:", w)
        self.assertEqual(w.getvalue(), "1:\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print("54816", w)
        self.assertEqual(w.getvalue(), "54816\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print("1", w)
        self.assertEqual(w.getvalue(), "1\n")

    def test_print_4 (self) :
        w = StringIO()
        netflix_print("17770:", w)
        self.assertEqual(w.getvalue(), "17770:\n")

    def test_print_5 (self) :
        w = StringIO()
        netflix_print("2649429", w)
        self.assertEqual(w.getvalue(), "2649429\n")
    # -----
    # solve
    # -----
    def test_solve (self):
        r = StringIO("10088:\n2594473\n2181764\n1982763\n1875632\n2302111\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10088:\n3.8\n3.8\n3.3\n4.3\n3.4\nRMSE: 1.13")
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
Ran 12 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Netflix          18      0      6      0   100%
TestNetflix      33      1      2      1    97%   106
---------------------------------------------------------
TOTAL            106     1      10     1    98%
"""
