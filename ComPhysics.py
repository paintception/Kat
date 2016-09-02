import numpy as np
import random
from matplotlib import pyplot as plt
from itertools import izip
import math

D = 1
L = 1001
d = 0.1
t = 0.001
m = 10000

class DiffusionAssignment():
	
	def vector_condition_1():
		
		vec_a = []

		for i in xrange(0,L):
			if i == 1:
				vec_a.append(1)
			else:
				vec_a.append(0)
		return vec_a
			
	def vector_condition_2():

		vec_b = []
		
		for i in xrange(0,L):
			if i == (L+1)/2:
				vec_b.append(1)
			else:
				vec_b.append(0)
		return vec_b

	def _matrixA():
		pass

	
	def matrixB(vector):
		
		block_matrix_b = [0.5*(1+math.e**(-2*t*D/d**2)),0.5*(1-math.e**(-2*t*D/d**2)),0.5*(1-math.e**(-2*t*D/d**2)),0.5*(1+math.e**(-2*t*D/d**2))]
		starting_point = math.e**(-2*t*D/d**2)
		
 		for v, w in zip(vector[::2], vector[1::2]):
 			
		
	if __name__ == '__main__':

		vec_a = vector_condition_1()
		vec_b = vector_condition_2()

		matrixB(vec_b)
		
