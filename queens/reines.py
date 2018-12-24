#!/usr/bin/python3

import numpy as np
import random, sys, re


class reines(object):
	"""docstring for reines"""
	def __init__(self, number):
		self.mp = self.generateNQueenProblem(number)


	def constraint(self,number):
		p = number
		Mp = np.ones((p,p,p,p),int)
		for x in range(p):
			for y in range(p):
				if x==y : 
					Mp[x,y] = np.identity(p,int)
				elif y > x:
						xixjmatrix = Mp[x,y]
						for i in range(p):
							xixjmatrix[i,i] = 0
							if (i+(y-x)) < p : xixjmatrix[i,i+(y-x)] = 0	
							if (i-(y-x)) >= 0 : xixjmatrix[i,i-(y-x)] = 0

						xixjmatrix_t = np.transpose(xixjmatrix)
						Mp[x,y] = xixjmatrix # put a random matrix on mp(x,y)
						Mp[y,x] = xixjmatrix_t	#put it transpose on mp(y,x)
				else:
					pass

		return Mp

	def generateNQueenProblem(self,number):
		matrix = self.constraint(number)
		return matrix

	def getq(self, number):
		Q = set()  # get all constraint between variables
		for i in range(number):
			for j in range(number):
				if j > i:
					if not (self.mp[i, j] == np.ones((number, number), int)).all():
						Q.add((i, j))
		return Q


