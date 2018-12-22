import sys,re
import random
import numpy as np
from csp import CSP

from queens import reines as queen 
from contrainte import C 
from domaine import D
from variable import X 
import basicFunctions as BF


if len(sys.argv) > 4:
	xi = sys.argv[1]
	di = sys.argv[2]
	nombre_contraint = sys.argv[3]
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

	Q = const_mat.getq(const_mat.Mp,xi.Xi,di.Di)

	csp = CSP(xi,di,const_mat.Mp)

	print(csp.look_ahead_v2(const_mat.Mp,Q))


	print(csp.x.instanciation)
	BF.printmatrix(csp.Mp)
