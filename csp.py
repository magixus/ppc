#!/usr/bin/python3

import numpy as np
import random 
import sys
import re
from sty import fg, bg, ef, rs, Rule
from queens import reines as queen 
from contrainte import C 
from domaine import D
from variable import X 
import basicFunctions as BF

class CSP(object):
	"""docstring for CSP"""
	def __init__(self,x,d,cMp):
		super(CSP, self).__init__()
		self.x = x # number of variables
		self.d = d # range of domain definition
		self.Mp = cMp
		self.domainXi = [set([p for p in range(self.d.Di) ]) for y in range(self.x.Xi)]
		#self.domainXi = [{} * self.x]

	def picHeuristicVar(self):
		# list des variable non encore instanciées
		varNotInst = [i for i in range(self.x.Xi) if not self.x.instanciation[i]]

		picMin = min([(len(self.domainXi[s]),s) for s in varNotInst])

		return picMin[1]



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


	def consistance(self,mat):
		taille = len(mat)
		for i in range(taille) :
			for j in range(i+1,taille-1) :
				# if any matrix is empty then false
				if np.sum(mat[i,j]) == 0 : return False
		return True

	def PC2(self,mat,Q):

		while Q: #while Q still has elements on it 
			pair = Q.pop()
			i = pair[0] ; j = pair[1]
			for k in range(self.x.Xi) :
				if (not (k==i) and not (k==j)) :
					#green
					temp = BF.intersection_m(mat[i,k],BF.product_m(mat[i,j],BF.product_m(mat[j,j],mat[j,k])))
					if not (temp ==mat[i,k]).all() :
						mat[i,k] = temp ; mat[k,i] = np.transpose(temp) 
						if i < k: Q.add((i,k)) 	
						else: Q.add((k,i))
					#blue
					temp = BF.intersection_m(mat[k,j],BF.product_m(mat[k,i],BF.product_m(mat[i,i],mat[i,j])))
					if (temp!=mat[k,j]).all() :
						mat[k,j] = temp ; mat[j,k] = np.transpose(temp) 
						if k < j: Q.add((k,j))   
						else: Q.add((j,k))
		return mat


	##except Exception as e:
	##	return "faill"



	def look_ahead_v1(self, m,Q) : # perform random var's initiation  
		# (x,d) = (variables, domains)
		self.PC2(m,Q)
		if not self.consistance(m) : print("inconsistant"); return False
		if self.x.isinstanciate() : 
			print("tout est instantié")
			return True
		else :
			# pic random var to istanciate 
			print(["vide" if not (e) else e for e in self.x.instanciation])
			xi = self.x.picRandomUninstanciateVar()

			for vi in self.domainXi[xi]:
				self.updatedomain(m,xi)
				m2 = m 
				self.x.instanciation[xi] = set([vi])
				
				#changement de domaine
				self.updateconstraint(m2,xi,vi)
				if self.look_ahead_v1(m2,Q) : return True 

			return False

	def look_ahead_v2(self, m,Q):
		# (x,d) = (variables, domains)
		m= self.PC2(m, Q)
		if not self.consistance(m) : print("inconsistant"); return False
		if self.x.isinstanciate() : 
			print("tout est instantié")
			return True
		else :
			# pic heuristic variable
			xi = self.picHeuristicVar()
			for vi in self.domainXi[xi]:
				self.updatedomain(m,xi)
				m2 = m 
				self.x.instanciation[xi] = set([vi])
				
				#changement de domaine
				self.updateconstraint(m2,xi,vi)
				if self.look_ahead_v1(m2,Q) : return True 

			return False

