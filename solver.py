import sys
import re
import random
from csp import CSP
import time

from queens.reines import reines as queen


if len(sys.argv) > 3:

	p = r"\d+"
	xi = list([int(x) for x in re.findall(p,sys.argv[1])])
	di = list([int(d) for d in re.findall(p,sys.argv[2])])
	ci = list([int(c) for c in re.findall(p,sys.argv[3])])

	X_rang = random.randrange(xi[0],xi[1])
	D_rang = random.randrange(di[0],di[1])
	C_rang = random.randrange(ci[0],ci[1])

	print("random variables  	=	",X_rang)
	print("random domains    	=	[ 0 .. ",D_rang,"]")
	print("random constraint	=	",C_rang )

	csp = CSP(X_rang,D_rang,C_rang)
	print("constraints are	=	",csp.Q)
	Mp = csp.Mp.copy()

	t= time.time()
	if csp.look_ahead(Mp):
		print("Solution found in :", time.time()-t, " s")
		print(csp.x.instanciation)
	else:
		print("No solution found !")



elif len(sys.argv) == 2:
	queenNubmer = int(sys.argv[1])
	Queen = queen(queenNubmer)
	#BF.printt(Queen.mp)
	csp = CSP(queenNubmer,queenNubmer,Queen.mp, Queen.Q)
	mp = csp.Mp.copy()

	print("Queens number		=	", queenNubmer)
	print("Queens domains		=	[ 0 .. ", queenNubmer, "]")

	t = time.time()
	if (csp.look_ahead(mp)):
		print("Solution found in  :", time.time()-t," s")
		print(csp.x.instanciation)
	else :
		print("no solution found")

else :
	print("\n\tusage \t: python solver.py [Var range] [dom range] [con range]\n")
	print("\n\tOR  \t: python solver.py numberQueen\n\n")