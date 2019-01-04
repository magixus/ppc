import sys
import re
import random
import numpy as np
from csp import CSP

from queens.reines import reines as queen
from contrainte import C 
from domaine import D
from variable import X 
import basicFunctions as BF


if len(sys.argv) > 3:

	p = r"\d+"
	xi = list([int(x) for x in re.findall(p,sys.argv[1])])
	di = list([int(d) for d in re.findall(p,sys.argv[2])])
	ci = list([int(c) for c in re.findall(p,sys.argv[3])])

	X_rang = random.randrange(xi[0],xi[1])
	D_rang = random.randrange(di[0],di[1])
	C_rang = random.randrange(ci[0],ci[1])

	print("random variables  = ",X_rang)
	print("random domains    =  [ 0 .. ",D_rang,"]")

	csp = CSP(X_rang,D_rang,C_rang)
	Q = csp.getQ(C_rang)
	print(Q)
	Mp = csp.Mp
	print(Mp)
	#BF.printcolor(Mp)
	dom = csp.d.Di
	print(csp.look_ahead(Mp))
	print(csp.x.instanciation)



elif len(sys.argv) == 2:
	queenNubmer = int(sys.argv[1])
	Queen = queen(queenNubmer)
	#BF.printt(Queen.mp)
	Q = Queen.getq(queenNubmer)
	csp = CSP(queenNubmer,queenNubmer,Queen.mp,Q)
	mp = csp.Mp
	#BF.printt(mp)

	print(sorted(Q))

	print(csp.look_ahead(mp))
	#print(csp.x.instanciation)

else :
	print("\n\tusage \t: python solver.py [Var range] [dom range] [con range]\n")
	print("\n\tOR  \t: python solver.py numberQueen\n\n")