#!/usr/bin/python3

import numpy as np
import random 
import sys
import re

class X(object):
	"""docstring for X"""
	def __init__(self, rang):
		super(X, self).__init__()
		self.Xi = random.randrange(rang[0],rang[1])

class D(object):
	"""docstring for D"""
	def __init__(self, rang):
		super(D, self).__init__()
		self.Di = random.randrange(rang[0],rang[1])

class C(object):
	"""docstring for C"""
	def __init__(self, n,p, with_constraint= False):
		self.Mp= np.zeros((n,n,p,p),int)
		if not with_constraint :
			"""
				create matrix of matrices 
				identity matrix on diagonal and universal ones otherwhere 
			"""
			for x in range(n):
				for y in range(n):
					if x==y : 
						self.Mp[x][y] = np.identity(p)
					else:
						self.Mp[x][y] = np.ones((p,p))
			
		else : 
			"""
				create constraint Mp matrix 
			"""
			for x in range(n):
				for y in range(n):

					if x==y : 
						for i in range(p):

							# matrix p*p that had random 0.1 in diag
							self.Mp[x][y][i][i] = random.randint(2) 

					elif y > x:
						rm = np.random.randint(2, size=(p, p))
						rm_t = np.transpose(rm)
						self.Mp[x][y] = rm # put a random matrix on mp(x,y)
						self.Mp[y][x] = rm_t	#put it transpose on mp(y,x)
					

		


class CSP(object):
	"""docstring for CSP"""
	def __init__(self,x,d,c):
		super(CSP, self).__init__()
		self.x = x
		self.d = d
		self.c = c
	
	def REVISE_pc(self,Xi,Xk,Xj):
		# this is revise_pc implementation method
		#temp = self.c.Mp[Xi][Xj 


		pass 

	def PC2() :
		pass

	def look_ahead() :
		pass

if len(sys.argv) > 2:
	xi = sys.argv[1]
	di = sys.argv[2]
	p = r"\d+"
	xi_rang = [int(x) for x in re.findall(p,xi)]
	di_rang = [int(d) for d in re.findall(p,di)]


	print(xi_rang, "    ",di_rang,"  ")

xi = X(xi_rang)
di = D(di_rang)

print(xi.Xi)
print(di.Di)
test_mat = C(xi,di)

print(test_mat.Mp)