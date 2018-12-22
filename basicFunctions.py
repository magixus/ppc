import numpy as np
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
