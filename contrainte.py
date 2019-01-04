import numpy as np

class C(object):
	"""docstring for C"""
	"""def __init__(self,mp):
		self.mp = mp"""
	def __init__(self, *args, **kwargs):
		if (kwargs.get('random')) :
			self.constraint_xi_xj = np.random.randint(2,size=(args[0],args[1]))

		elif kwargs.get('universal'):
			self.constraint_xi_xj = np.ones((args[0],args[1]))
		else :
			self.constraint_xi_xj = args[0]

		def setconstraint(self,contraint):
			self.constraint_xi_xj = contraint

	def is_empty(self):
		if np.sum(self.constraint_xi_xj) == 0 : return True
		else : return  False

	def transpose(self):
		p = len(self.constraint_xi_xj)
		if p == 1:
			self.constraint_xi_xj.reshape(p,1)
		else :
			return np.transpose(self.constraint_xi_xj)

	def __and__(self, other):
		return self.constraint_xi_xj &  other.constraint_xi_xj

	"""def __rand__(self, other):
		return other & self.constraint_xi_xj"""

	def __eq__(self, other):
		n = self.constraint_xi_xj.shape
		for i in range(n[0]):
			for j in range(n[1]):
				if self.constraint_xi_xj[i,j] != other.constraint_xi_xj[i,j]:
					return False
		return True

	def __mul__(self, other):
		res = np.dot(self.constraint_xi_xj, other.constraint_xi_xj)
		for i in range(res.shape[0]) :
			for j in range(res.shape[1]) :
				if res[i,j] > 1 : res[i,j] = 1
		return C(res)
