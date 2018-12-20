#!/usr/bin/python3

import numpy as np
import random, sys, re


class reines(object):
	"""docstring for reines"""
	def __init__(self, number):
		super(reines, self).__init__()
		self.number = number


	def constraint(self):
		p = self.number
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

	def generateNQueenProblem(self):
		n = self.number
		matrix = self.constraint()
		return matrix
		for i in range(n):
			for j in range(n):
				print("Mp[",i,',',j,"]")
				print (matrix[i,j])


#generateNQueenProblem(int(sys.argv[1]))