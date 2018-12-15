#!/usr/bin/python3

import numpy as np
import random 
import sys
import re

def intersection_m(m1, m2):
	return  m1*m2

def product_m(m1,m2)
	k = np.dot(m1,m2)
	for i in range(len(k[0])) :
		for j in range(len(k[0])) :
			if k[i,j] >1 : k[i,j] =1
	return k 


class X(object):
	"""docstring for X"""
	def __init__(self, rang):
		super(X, self).__init__()
		self.Xi = random.randrange(rang[0],rang[1])
		self.instantiation =[{} for y in range(len(self.Xi))]
	
	def isinstanciate():
		# return false if there is any var not instanciate
		return not(False in [vs for vs in self.instantiation])	

	def picRandomUninstanciateVar():
		# sefl.Xi 
		return random.choice([i for i in range(self.Xi) if self.instanciation[i]])

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
							self.Mp[x,y][i,i] = random.randint(2) 

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
		self.MP = cMp
		self.domainXi = [set([p for p in range(self.d) ]) * self.x.Xi]
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

	def PC2() :
		Q = set() # get all constraint between variables
		for x in range(n):
			for y in range(n):
				if y > x:
					if (self.Mp[x,y] != np.ones((self.d,self.d), int)):
						Q.add((x,y))
		
		try:
			while Q: #while Q still has elements on it 
				pair = Q.pop()
				i = pair[0] ; j = pair[1]
				for k in range(self.x) if not (k==i==j):
					#green
					temp = intersection_m(self.Mp[i,k],product_m(self.Mp[i,j],product_m(self.Mp[j,j],self.Mp[j,k])))
					if (temp!=self.Mp[i,k]).all() :
						self.Mp[i,k] = temp ; self.Mp[k,i] = np.transpose(temp) 
						if i <= k: 
							Q.add((i,k))
						else:
							Q.add(k,i)
					#blue
					temp = intersection_m(self.Mp[k,j],product_m(self.Mp[k,i],product_m(self.Mp[i,i],self.Mp[i,j])))
					if (temp!=self.Mp[k,j]).all() :
						self.Mp[k,j] = temp ; self.Mp[j,k] = np.transpose(temp) 
						if k <= j: 
							Q.add((k,j))
						else:
							Q.add(j,k)
			return "success"
			pass
		except Exception as e:
			return "faill"

	def consistance():
		for i in range(self.x) :
			for j in range(self.x) :
				# if any matrix is empty then false
				if (np.zeros((self.d,self.d),int)==self.Mp[x,y]).all() :
					return False
		return True

	def look_ahead_v1(A={}) : # perform random var's initiation  
		# (x,d) = (variables, domains)
		PC2()
		if not consistance() : return False
		if isinstanciate() : 
			return True
		else :
			# pic random var to istanciate 
			xi = picRandomUninstanciateVar()

			for vi in range(self.d):
				self.x.instantiation[xi].add(vi)
				self.domainXi[xi] = self.x.instantiation[xi]
				A.add((xi,vi))
				if look_ahead_v1(A) : return True

			return False








"""

if len(sys.argv) > 2:
	xi = sys.argv[1]
	di = sys.argv[2]
	p = r"\d+"
	xi_rang = [int(x) for x in re.findall(p,xi)]
	di_rang = [int(d) for d in re.findall(p,di)]


	print(xi_rang, "    ",di_rang,"  ")

	xi = X(xi_rang)
	di = D(di_rang)

	print("random variables  = ",xi.Xi)
	print("random domains    = ",di.Di)
	const_mat = C(xi.Xi,di.Di)

	print(test_mat.Mp)

	scp = CSP(xi,di,const_mat.Mp)
	print(scp.PC2())"""