#!/usr/bin/env python3

import numpy
import io
import math
import json
from pprint import pprint


path_average_movie_rating = "/u/ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
path_average_viewer_rating = "/u/ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json"
path_probe_solutions = "/u/ebanner/netflix-tests/pam2599-probe_solutions.json"

mrating = open(path_average_movie_rating,'r')
vrating = open(path_average_viewer_rating, 'r')
probe_solutions = open(path_probe_solutions, 'r')

average_m_cache = json.loads(mrating.read())
average_v_cache = json.loads(vrating.read())
prob_sol_cache = json.loads(probe_solutions.read())

#print (str(average_v_cache["1585790"]))

def netflix_end():
	mrating.close()
	vrating.close()
	probe_solutions.close()

def netflix_read(r):
	"""
	r is a reader
	.strip() removes all whitespace at the start and end, 
	including spaces, tabs, newlines and carriage returns.
	"""
	s = r.readline().strip()
	return s

def netflix_predict():
	return 0		


def netflix_print(s,w):
	w.write(s + "\n")




def netflix_solve(r,w):
	"""
    r a reader
    w a writer
    """
	movie_id = "-1"
	processing = True 

	while(processing):
		s = netflix_read(r)
		if s =='':
			processing = False
			netflix_print("RSME " + "blah",w)
		elif s[-1] == ':':
			movie_id = s[:-1]
				
		else:
			print (s)
			