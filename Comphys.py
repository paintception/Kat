import numpy as np
import math
import itertools
import time

from matplotlib import pyplot as plt
from itertools import izip

D = 1
L = 1001
d = 0.1
t = 0.001
m = 10000

class Diffusion():

	def vector_condition_a():
			
		vec_a = []

		for i in xrange(0,L):
			if i == 1:
				vec_a.append(1)
			else:
				vec_a.append(0)	
		
		return vec_a

	def vector_condition_b():

		vec_b = []
			
		for i in xrange(0,L):
			if i == (L+1)/2:
				vec_b.append(1)
			else:
				vec_b.append(0)

		return vec_b

	def matrix_condition_a(vector_a):
				
		res_condition_a = []

		Starting_Point = math.e**-t*D*d**-2
		block_a = np.array([[0.5*(1+math.e**(-2*t*D/d**2)),0.5*(1-math.e**(-2*t*D/d**2))], 
							[0.5*(1-math.e**(-2*t*D/d**2)),0.5*(1+math.e**(-2*t*D/d**2))]])

		vec_a = izip(vector_a[::2], vector_a[1::2])

		for pairs in vec_a:
			tmp_pair = np.array([pairs[0],pairs[1]])
			res_condition_a.append(block_a.dot(tmp_pair))

		tmp_res = []

		for i in res_condition_a:
			vector_a = np.array(i).tolist()
			tmp_res.append(vector_a)

		new_vector_a = list(itertools.chain(*tmp_res)) 
		new_vector_a.append(Starting_Point*vector_a[-1])
		
		return new_vector_a


	def matrix_condition_b(vector_b):
		
		res_condition_b = []

		Starting_Point = math.e**-t*D*d**-2
		block_b = np.array([[0.5*(1+math.e**(-2*t*D/d**2)),0.5*(1-math.e**(-2*t*D/d**2))], 
							[0.5*(1-math.e**(-2*t*D/d**2)),0.5*(1+math.e**(-2*t*D/d**2))]])

		vec_b = izip(vector_b[::2], vector_b[1::2])

		for pairs in vec_b:
			tmp_pair = np.array([pairs[0],pairs[1]])
			res_condition_b.append(block_b.dot(tmp_pair))

		tmp_res = []

		for i in res_condition_b:
			vector_b = np.array(i).tolist()
			tmp_res.append(vector_b)

		new_vector_b = list(itertools.chain(*tmp_res)) 
		new_vector_b.insert(0, Starting_Point*vector_b[0])
		
		return new_vector_b


	def plots():
		pass

	if __name__ == '__main__':
		
		vec_a = vector_condition_a()
		vec_b = vector_condition_b()

		"""
		for i in xrange(1,L-1):
			n_a = matrix_condition_a(vec_a)
			vec_a = n_a
		"""

		for i in xrange(1,L-1):
			n_b = matrix_condition_b(vec_b)
			#print "Diffusion is going on: ", n_b
			#time.sleep(2)
			vec_b = n_b

	"""
	a = []
	for i in xrange(len(vec_b)):
		a.append(i)

	plt.plot(a, vec_b)
	plt.show()
	"""