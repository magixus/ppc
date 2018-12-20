#!/usr/bin/python3

import numpy as np
import random 
import sys
import re
from sty import fg, bg, ef, rs, Rule
from queens import reines as queen 

def intersection_m(m1, m2):
	return  m1*m2

def product_m(m1,m2):
	k = np.dot(m1,m2)
	for i in range(len(k[0])) :
		for j in range(len(k[0])) :
			if k[i,j] >1 : k[i,j] =1
	return k 

def printcolor(ob):
	print(bg(np.random.randint(255)) + str(ob) + bg.rs)


def printmatrix(m):
	printcolor(m)




class X(object):
	"""docstring for X"""
	def __init__(self, rang):
		super(X, self).__init__()
		#self.Xi = random.randrange(rang[0],rang[1])
		self.Xi = rang
		self.instantiation =[set() for y in range(self.Xi)]
	
	def isinstanciate(self):
		# return false if there is any var not instanciate
		return not(False in [True if(vs) else False for vs in self.instantiation])	

	def picRandomUninstanciateVar(self):
		# sefl.Xi 
		return random.choice([i for i in range(self.Xi) if not self.instantiation[i]])

class D(object):
	"""docstring for D"""
	def __init__(self, rang):
		super(D, self).__init__()
		#self.Di = random.randrange(rang[0],rang[1])
		self.Di = rang


class C(object):
	"""docstring for C"""
	def __init__(self,mp):
		self.mp = mp
		
	def getq(self,mat,var,dom):
		Q = set() # get all constraint between variables
		for i in range(var):
			for j in range(var):
				if j > i:
					if not (mat[i,j] == np.ones((dom,dom), int)).all():
						Q.add((i,j))
		return Q

class CSP(object):
	"""docstring for CSP"""
	def __init__(self,x,d,cMp):
		super(CSP, self).__init__()
		self.x = x # number of variables
		self.d = d # range of domain definition
		self.Mp = cMp
		self.domainXi = [set([p for p in range(self.d.Di) ]) for y in range(self.x.Xi)]
		#self.domainXi = [{} * self.x]
		print(self.domainXi)

	"""def REVISE_pc(self,i,k,j):
		# this is revise_pc implementation method
		# temp=Mp[i,j] ^ Mp[i,k]° Mp[k,k] °Mp[k,j]
		temp = intersection_m(self.Mp[i,j],product_m(self.Mp[i,k],product_m(self.Mp[k,k],self.Mp[k,j])))

		if (temp!=self.Mp[i,j]).all() :
			self.Mp[i,j] = temp
			return True
		else : 
			return False"""

	def updateconstraint(self, mat,xi,vi):
		var_pos = mat[xi]
		for xj in range(xi+1,len(var_pos)-1) :
			vec = list(mat[xi,xj][vi])
			unchaged = np.array(vec)

			# transposer le vecteur
			mat_t = np.reshape(unchaged,(len(var_pos),1))

			mat[xi,xj] = unchaged
			mat[xj,xi] = mat_t	#put transpose on mp(xj,xi)

	def updatedomain(self,m,position):
		for y in range(position+1,self.x.Xi-1):
			mat = m[position,y]
			print(mat)
			for i in range(len(mat)):
				if mat[i] == 0 :
					self.domainXi[y].remove(i)

	def PC2(self,mat,Q):
		while Q: #while Q still has elements on it 
			pair = Q.pop()
			i = pair[0] ; j = pair[1]
			for k in range(self.x.Xi) :
				if (not (k==i) and not (k==j)) :
					#green
					temp = intersection_m(mat[i,k],product_m(mat[i,j],product_m(mat[j,j],mat[j,k])))
					if not (temp ==mat[i,k]).all() :
						mat[i,k] = temp ; mat[k,i] = np.transpose(temp) 
						if i < k: Q.add((i,k)) 	
						else: Q.add((k,i))
					#blue
					temp = intersection_m(mat[k,j],product_m(mat[k,i],product_m(mat[i,i],mat[i,j])))
					if (temp!=mat[k,j]).all() :
						mat[k,j] = temp ; mat[j,k] = np.transpose(temp) 
						if k < j: Q.add((k,j))   
						else: Q.add((j,k))
		return mat


	##except Exception as e:
	##	return "faill"


	def consistance(self,mat):
		for i in range(len(mat[0])) :
			for j in range(len(mat[0])) :
				# if any matrix is empty then false
				if (np.zeros((self.d.Di,self.d.Di),int)==mat[i,j]).all() : 
					return False
		return True

	def look_ahead_v1(self, m,Q) : # perform random var's initiation  
		# (x,d) = (variables, domains)
		self.PC2(m,Q)
		if not self.consistance(m) : print("inconsistant"); return False
		if self.x.isinstanciate() : 
			print("tout est instantié")
			return True
		else :
			# pic random var to istanciate 
			print(["vide" if not (e) else e for e in self.x.instantiation])
			xi = self.x.picRandomUninstanciateVar()

			for vi in self.domainXi[xi]:
				self.updatedomain(m,xi)
				m2 = m 
				self.x.instantiation[xi] = set([vi])
				
				#changement de domaine
				self.updateconstraint(m2,xi,vi)
				if self.look_ahead_v1(m2,Q) : return True 

			return False

	def look_ahead_v2(self, m):
		# (x,d) = (variables, domains)
		m= self.PC2(m)
		if not self.consistance() : print("inconsistant"); return False
		if self.x.isinstanciate() : 
			print("tout est instantié")
			return True
		else :
			# pic random var to istanciate
			pass








if len(sys.argv) > 3:
	xi = sys.argv[1]
	di = sys.argv[2]
	const = sys.argv[3]
	p = r"\d+"
	xi_rang = [int(x) for x in re.findall(p,xi)]
	di_rang = [int(d) for d in re.findall(p,di)]


	print(xi_rang, "    ",di_rang,"  ")

	xi = X(xi_rang[0])
	di = D(di_rang[0])

	print("random variables  = ",xi.Xi)
	print("random domains    = ",di.Di)

	"""if const.startswith("True") :
		const_mat = C(xi.Xi,di.Di, True)
	else:
		const_mat = C(xi.Xi,di.Di)
	#print(const_mat.Mp)
	"""
	#print(fg.red + str(const_mat.Mp)+ fg.rs)

	q = queen.reines(xi.Xi)
	Qmp = q.constraint()
	csp = CSP(xi,di,q.generateNQueenProblem())

	c= C(Qmp)

	Q = c.getq(Qmp,xi.Xi,di.Di)
	print(csp.look_ahead_v1(Qmp,Q))


	print(csp.x.instantiation)
	#printmatrix(csp.Mp)
	#printcolor(const_mat.Mp)
	#while not csp.look_ahead_v1(const_mat.Mp):
	#	print( "pas de solustion")
	#printcolor(const_mat.Mp)
	#printmatrix(const_mat.Mp)
