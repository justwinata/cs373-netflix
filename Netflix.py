#!/usr/bin/env python3

import io
from math import sqrt
import json
from pprint import pprint
from urllib.request import urlopen

urlamr = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")
urlavr = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
urlpps = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")

average_m_cache = json.loads(urlamr.read().decode(urlamr.info().get_param('charset') or 'utf-8'))
average_v_cache = json.loads(urlavr.read().decode(urlavr.info().get_param('charset') or 'utf-8'))
prob_sol_cache = json.loads(urlpps.read().decode(urlpps.info().get_param('charset') or 'utf-8'))

global ourpredictions
ourpredictions = []

global actualpredictions
actualpredictions = []

def netflix_read(r):
	"""
	r is a reader
	.strip() removes all whitespace at the start and end, 
	including spaces, tabs, newlines and carriage returns.
	"""
	s = r.readline().strip()
	return s

def netflix_predict(m_id, customer_id,w,totalavg):
	predict = 0
	predict = (average_m_cache[m_id] + average_v_cache[customer_id]) - totalavg
	ourpredictions.append(float(predict))
	actualpredictions.append(float(prob_sol_cache[m_id][customer_id]))
	netflix_print(str(round(predict,1)),w)
			
def netflix_print(s,w):
	w.write(""+s + "\n")

def netflix_solve(r,w):
	"""
    r a reader
    w a writer
    """
	movie_id = "-1"
	processing = True 
	rmse =0
	avg = 0

	"""
	totalavg calculated with:

	for v in average_v_cache:
		avg += average_v_cache[v]

	totalavg = avg/len(average_v_cache)	
	print (totalavg)
	"""
	totalavg = 3.674130451108032

	while(processing):
		s = netflix_read(r)
		if s =='':
			processing = False
			z = zip(ourpredictions,actualpredictions)
			v = sum((x-y) ** 2 for x, y in z)
			rmse = sqrt(v/len(ourpredictions))	
			w.write("RMSE: " + str(round(rmse,2)))
		elif s[-1] == ':':
			movie_id = s[:-1]
			netflix_print(s,w)
		else:
			netflix_predict(movie_id,s,w,totalavg)