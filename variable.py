from numpy.random import randint
import random
class X(object):
	"""docstring for X"""
	def __init__(self, x):
		super(X, self).__init__()
		self.Xi = x
		#self.Xi = rang
		self.instanciation =[set() for y in range(x)]
	
	def isinstanciate(self):
		# return false if there is any var not instanciate
		return not(False in [True if(vs) else False for vs in self.instanciation])	

	def picRandomUninstanciateVar(self):
		# sefl.Xi 
		return random.choice([i for i in range(self.Xi) if not self.instanciation[i]])

	def generateConstraints(self,C_number):
		constraints = set()
		while (len(constraints) <= C_number):
			xi = randint(0,self.Xi + 1)
			try :
				xj = random.randrange(xi+1, self.Xi)
				if (xi,xj) not in constraints : constraints.add((xi,xj))
			except ValueError:
				pass

		return constraints

	def setX(self,xi):
		self.Xi = xi
	
	def setInst(self,instance):
		self.instanciation = instance

	def getX(self):
		return self.Xi

	def getInst(self):
		return self.instanciation