import random

class D(object):
	"""docstring for D"""
	def __init__(self, rang, V):
		super(D, self).__init__()
		self.p = random.randrange(rang[0],rang[1])
		self.Di = [set([d for d in range(self.p)]) for y in range(V)]
		#self.Di = rang

	def addDom(self,dom,xi):
		self.Di[xi] = dom

	def getDom(self, xi):
		return self.Di[xi]