import numpy as np

# test matrix creation 
def matrix1 (n,p):
	Mp = np.zeros((n,n,p,p),int)
	for x in range(n):
		for y in range(n):
			if x==y : 
				Mp[x][y] = np.identity(p)
			else:
				Mp[x][y] = np.ones((p,p))
	return Mp

csp = matrix1(5,10)
print(csp[1])
print(csp[1][1])
print(csp[2][3])


