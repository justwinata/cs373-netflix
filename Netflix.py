#!/usr/bin/env python3

import io
from math import sqrt
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
global ourpredictions
ourpredictions = []

global actualpredictions
actualpredictions = []

"""
print (float(prob_sol_cache["1"]["30878"]))
actualpredictions.append(float(prob_sol_cache["4446"]["1657689"]))
print (*actualpredictions)
"""
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

def netflix_predict(m_id, customer_id,w,totalavg):
	predict = 0
	predict = (average_m_cache[m_id] + average_v_cache[customer_id]) - totalavg
	ourpredictions.append(float(predict))
	actualpredictions.append(float(prob_sol_cache[m_id][customer_id]))
	#print(*ourpredictions)
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
			w.write("RSME: " + str(round(rmse,2)))
		elif s[-1] == ':':
			movie_id = s[:-1]
			netflix_print(s,w)
		else:
			netflix_predict(movie_id,s,w,totalavg)
	
	netflix_end()	