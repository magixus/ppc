import numpy as np
import random 

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
			return self.Mp
			
		else : 
			"""
				create constraint Mp matrix 
			"""
			for x in range(n):
				for y in range(n):
					


		


class CSP(object):
	"""docstring for CSP"""
	def __init__(self, mp):
		super(CSP, self).__init__()
		self.mp = mp
	
	def REVISE_pc() :
		pass

	def PC2() :
		pass

	def look_ahead() :
		pass


test_mat = C(10,12)

test_mat.Mp