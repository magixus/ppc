
  # !/usr/bin/python3


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

  def __init__(self, x, d,c):
    self.x = X(x)  # number of variables
    self.d = D(d, x)  # range of domain definition
    self.domainXi = [set([p for p in range(d)]) for y in range(x)]
    if type(c) is 'int':
      self.Mp = self.generateRandomConstraint(self.getQ(c))
    else :
      self.Mp = c


  def generateRandomConstraint(self, constraint):
    n = self.x.Xi
    p = len(self.d.Di)
    mp = np.ones((n,n,p,p),int)
    for i in range(n):
      mp[i, i] = np.identity(p)
      for j in range(i+1,n):
        if (i,j) in constraint :
          c_xi_xj = C(p,p,random="True")
          c_xi_xj_transpoe = c_xi_xj.transpose()
          mp[i,j] = c_xi_xj.constraint_xi_xj
          mp[j,i] = c_xi_xj_transpoe
    return mp

  def getQ(self, n):
    return self.x.generateConstraints(n)

  def updateconstraint(self, mat, xi, vi):
    var_pos = mat[xi]
    for xj in range(xi + 1, len(var_pos) - 1):
      vec = list(mat[xi, xj][vi])
      unchaged = np.array(vec)

      # transposer le vecteur
      mat_t = np.reshape(unchaged, (len(var_pos), 1))

      mat[xi, xj] = unchaged
      mat[xj, xi] = mat_t  # put transpose on mp(xj,xi)

  def updatedomain(self,mat,domaine):
    for i in range(self.x.Xi) :
      c = mat[i,i]
      for l in range(len(c)):
        if c[l,l] == 0 :
          domaine.exists[i][l] = 0
          self.domainXi[i].remove(l)


  def is_consistant(self,mat):
    for i in range(self.x.Xi):
      for j in range(self.x.Xi):
        # if any matrix is empty then false
        if np.sum(mat[i, j]) == 0: return False
    return True

  def PC2(self,domaine, mat,Q):

    while Q:  # while Q still has elements on it
      pair = Q.pop()
      print(pair)
      i,j = pair[0],pair[1]
      for k in range(self.x.Xi):
        if (not (k == i) and not (k == j)):
          # green
          temp = C(mat[i, k]) & (C(mat[i, j]) * (C(mat[j, j]) * C(mat[j, k])))
          if not (C(temp) == C(mat[i, k])):
            mat[i, k] = temp
            mat[k, i] = C(temp).transpose()
            if i < k:
              Q.add((i, k))
            else:
              Q.add((k, i))
          # blue
          temp = C(mat[k, j]) & (C(mat[k, i]) * (C(mat[i, i]) * C(mat[i, j])))
          if not (C(temp) == C(mat[k, j])):
            mat[k, j] = temp
            mat[j, k] = C(temp).transpose()
            if k < j:
              Q.add((k, j))
            else:
              Q.add((j, k))
    #BF.printt(mat)
    self.updatedomain(mat,domaine)

  ##except Exception as e:
  ##	return "faill"

  def look_ahead(self, Domaine, m, Q):  # perform random var's initiation
    QQ = Q
    self.PC2(Domaine,m,QQ)
    print("passage ici--------")
    if not self.is_consistant(m): print("inconsistant"); return False
    if self.x.is_instanciate():
      print("tout est instantié")
      return True
    else:
      # pic random var to istanciate
      xi = self.x.picRandomUninstanciateVar()
      print(["vide" if not (e) else e for e in self.x.instanciation])

      print(self.domainXi[xi])

      for vi in Domaine.Di[xi]:
        self.domainXi[xi]={vi}
        dom = Domaine
        dom.Di[xi] = {vi}
        self.x.instanciation[xi] = {vi}
        m2 = m
        BF.printt(m)
        self.updateConstrait(dom,m2)
        if self.look_ahead(dom, m2, Q): return True
      return False

  def updateConstrait(self, dom, mat):
    for i in range(self.x.Xi):
      for j in range(i+1,self.x.Xi):
        domC = dom.getConstraintFromDomain(i,j)
        """
        print("----")
        print(domC)
        """
        mat[i,j] = mat[i,j] & domC
        domC = np.transpose(domC)
        mat[j,i] = mat[j,i] & domC