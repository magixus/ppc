
class D(object):
	""""docstring for D"""
	def __init__(self,p,V):
		super(D, self).__init__()
		self.Di = [set([d for d in range(p)]) for y in range(V)]
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
