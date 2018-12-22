import random

class X(object):
	"""docstring for X"""
	def __init__(self, rang):
		super(X, self).__init__()
		self.Xi = random.randrange(rang[0],rang[1])
		#self.Xi = rang
		self.instanciation =[set() for y in range(self.Xi)]
	
	def isinstanciate(self):
		# return false if there is any var not instanciate
		return not(False in [True if(vs) else False for vs in self.instanciation])	

	def picRandomUninstanciateVar(self):
		# sefl.Xi 
		return random.choice([i for i in range(self.Xi) if not self.instanciation[i]])

	def setX(self,xi):
		self.Xi = xi
	
	def setInst(self,instance):
		self.instanciation = instance

	def getX(self):
		return self.Xi

	def getInst(self):
		return self.instanciation