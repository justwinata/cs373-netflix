#!/usr/bin/env python3

import numpy
import io
import math
import json
from pprint import pprint


path_average_movie_rating = "/u/ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
path_average_viewer_rating = "/u/ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json"

mrating = open(path_average_movie_rating,'r')
vrating = open(path_average_viewer_rating, 'r')

average_m_cache = json.loads(mrating.read())
average_v_cache = json.loads(vrating.read())

#print (str(average_v_cache["1585790"]))



def netflix_read(r):
	"""
	r is a reader
	"""
	while s:
		s= r.readLine()
	return s   



def netflix_solve(r,w):
	return 0



def netflix_eval():
	return 0			