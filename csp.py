#!/usr/bin/python3

import numpy as np
import random 
import sys
import re
from sty import fg, bg, ef, rs, Rule


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
		self.Xi = random.randrange(rang[0],rang[1])
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
						self.Mp[x,y] = np.identity(p)
					else:
						self.Mp[x,y] = np.ones((p,p))
			
		else : 
			"""
				create constraint Mp matrix 
			"""
			for x in range(n):
				for y in range(n):

					if x==y : 
						for i in range(p):

							# matrix p*p that had random 0.1 in diag
							self.Mp[x,y][i,i] = np.random.randint(2) 

					elif y > x:
						rm = np.random.randint(2, size=(p, p))
						rm_t = np.transpose(rm)
						self.Mp[x,y] = rm # put a random matrix on mp(x,y)
						self.Mp[y,x] = rm_t	#put it transpose on mp(y,x)
					


class CSP(object):
	"""docstring for CSP"""
	def __init__(self,x,d,cMp):
		super(CSP, self).__init__()
		self.x = x # number of variables
		self.d = d # range of domain definition
		self.Mp = cMp
		self.domainXi = [set([p for p in range(self.d.Di) ]) for y in range(self.x.Xi)]
		#self.domainXi = [{} * self.x]
		

	"""def REVISE_pc(self,i,k,j):
		# this is revise_pc implementation methodd
		# temp=Mp[i,j] ^ Mp[i,k]° Mp[k,k] °Mp[k,j]
		temp = intersection_m(self.Mp[i,j],product_m(self.Mp[i,k],product_m(self.Mp[k,k],self.Mp[k,j])))

		if (temp!=self.Mp[i,j]).all() :
			self.Mp[i,j] = temp
			return True
		else : 
			return False"""
	def changedomain(self, xi,vi):
		var_pos = self.Mp[xi]
		for i in range(len(var_pos)) :
			self.Mp[xi,i] = self.Mp[xi,i][vi]

	def PC2(self):
		Q = set() # get all constraint between variables
		for i in range(self.x.Xi):
			for j in range(self.x.Xi):
				if j > i:
					if not (self.Mp[i,j] == np.ones((self.d.Di,self.d.Di), int)).all():
						Q.add((i,j))

		#printcolor(Q)
	##try:
		while Q: #while Q still has elements on it 
			pair = Q.pop()
			i = pair[0] ; j = pair[1]
			for k in range(self.x.Xi) :
				if not (k==i==j) :
					#green
					temp = intersection_m(self.Mp[i,k],product_m(self.Mp[i,j],product_m(self.Mp[j,j],self.Mp[j,k])))
					if not (temp ==self.Mp[i,k]).all() :
						self.Mp[i,k] = temp ; self.Mp[k,i] = np.transpose(temp) 
						if i <= k: 
							Q.add((i,k))
						else:
							Q.add((k,i))
					#blue
					temp = intersection_m(self.Mp[k,j],product_m(self.Mp[k,i],product_m(self.Mp[i,i],self.Mp[i,j])))
					if (temp!=self.Mp[k,j]).all() :
						self.Mp[k,j] = temp ; self.Mp[j,k] = np.transpose(temp) 
						if k <= j: 
							Q.add((k,j))
						else:
							Q.add((j,k))
		return "success"
	##except Exception as e:
	##	return "faill"


	def consistance(self):
		for i in range(self.x.Xi) :
			for j in range(self.x.Xi) :
				# if any matrix is empty then false
				if (np.zeros((self.d.Di,self.d.Di),int)==self.Mp[i,j]).all() :
					return False
		return True

	def look_ahead_v1(self) : # perform random var's initiation  
		# (x,d) = (variables, domains)
		self.PC2()
		if not self.consistance() : print("bonsoir"); return False
		if self.x.isinstanciate() : 
			print("bonjour")
			return True
		else :
			# pic random var to istanciate 
			xi = self.x.picRandomUninstanciateVar()


			for vi in range(self.d.Di):
				print(xi,"--",vi)
				self.x.instantiation[xi].add(vi)
				
				#changement de domaine
				self.Mp[xi] 
				if self.look_ahead_v1() : return True
			return False










if len(sys.argv) > 3:
	xi = sys.argv[1]
	di = sys.argv[2]
	const = sys.argv[3]
	p = r"\d+"
	xi_rang = [int(x) for x in re.findall(p,xi)]
	di_rang = [int(d) for d in re.findall(p,di)]


	print(xi_rang, "    ",di_rang,"  ")

	xi = X(xi_rang)
	di = D(di_rang)

	print("random variables  = ",xi.Xi)
	print("random domains    = ",di.Di)

	if const.startswith("True") :
		const_mat = C(xi.Xi,di.Di, True)
	else:
		const_mat = C(xi.Xi,di.Di)
	#print(const_mat.Mp)

	print(fg.red + str(const_mat.Mp)+ fg.rs)

	csp = CSP(xi,di,const_mat.Mp)
	print(csp.look_ahead_v1())
	print(csp.x.instantiation)
	#printmatrix(const_mat.Mp)
