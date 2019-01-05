#!/usr/bin/python3

import numpy as np


class reines(object):
	"""docstring for reines"""
	def __init__(self, number):
		self.mp = self.generateNQueenProblem(number)
		self.Q 	= self.getq(number)

	def generateNQueenProblem(self,number):
		matrix = self.constraint(number)
		return matrix

	def constraint(self,number):
		p = number
		Mp = np.ones((p,p,p,p),int)
		for x in range(p):
			for y in range(p):
				if x==y :
					Mp[x,y] = np.identity(p,int)
				elif y > x:
						mat = Mp[x,y]
						for i in range(p):
							mat[i,i] = 0
							if (i+(y-x)) < p : mat[i,i+(y-x)] = 0
							if (i-(y-x)) >= 0 : mat[i,i-(y-x)] = 0
						mat_t = np.transpose(mat)
						Mp[x,y] = mat # put a random matrix on mp(x,y)
						Mp[y,x] = mat_t	#put it transpose on mp(y,x)
				else:
					pass

		return Mp

	def getq(self, number):
		Q = set()  # get all constraint between variables
		for i in range(number):
			for j in range(i+1,number):
				Q.add((i, j))
		return Q


