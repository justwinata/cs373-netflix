#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    # Check for valid input range
    assert i > 0
    assert i < 1000000
    assert j > 0
    assert j < 1000000
    # Check type
    assert isinstance (i, int)
    assert isinstance (j, int)
    # Check which input is greater, create range to iterate
    if (i > j):
        r = range (j, i + 1)
    else:
        r = range (i, j + 1)
    # Start max cycle length as 1
    maxcyc = 1
    # Find largest cycle
    for n in r :
        cyc = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (3 * n) + 1
            cyc += 1
        maxcyc = max(cyc, maxcyc)
    return maxcyc

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
