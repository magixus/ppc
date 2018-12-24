import numpy as np

class D(object):
	""""docstring for D"""
	def __init__(self,p,V):
		super(D, self).__init__()
		self.Di = [set([d for d in range(p)]) for y in range(V)]
		self.exists = [[1 for a in range(p) if a in self.Di[y]]for y in range(V) ]
		#self.Di = rang

	def addDom(self,dom,xi):
		self.Di[xi] = dom

	def getDom(self, xi):
		return self.Di[xi]

	def picHeuristicVar(self, x):
		# list des variable non encore instanciées
		varNotInst = [i for i in range(x.Xi) if not x.instanciation[i]]
		picMin = min([(len(self.Di[s]),s) for s in varNotInst])
		return picMin[1]

	def clearDom(self,xi,val):
		#for l in range(len(self.Di)):
		pass

	def getConstraintFromDomain(self,xi,xj):
		res = np.zeros((len(self.Di),len(self.Di)),int)
		for i in self.Di[xi]:
			for j in self.Di[xj]:
				res[i,j] = self.exists[xi][i] * self.exists[xj][j]
		return res
