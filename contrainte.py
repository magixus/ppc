import numpy as np

class C(object):
	"""docstring for C"""
	"""def __init__(self,mp):
		self.mp = mp"""
	def __init__(self, *args, **kwargs):
		
		if eval(kwargs.get('random')) :
			self.contrainte_xi_xj = np.random.randint(2,size=(args[0],args[1]))

		else eval(kwargs.get('universal'):
			self.contrainte_xi_xj = np.ones((args[0],args[1]))



	def setconstraint(self,contraint):
		self.contrainte_xi_xj = contraint

	def __mul__(self,constraint):
		len_mat = len(self.contrainte_xi_xj)
		res = np.zeros((len_mat,len_mat),int)
		for i in range(len_mat) :
			for j in range(len_mat) :

				if k[i,j] > 1 : res[i,j] = 1
		return res



