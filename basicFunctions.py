import numpy as np
from sty import fg, bg, ef, rs, Rule


def printcolor(ob):
	print(bg(np.random.randint(255)) + str(ob) + bg.rs)



def printt(m):
	for i in range(len(m)):
		for j in range(len(m)):
			print("Mp[",i,',',j,"]")
			print (m[i,j])