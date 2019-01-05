from csp import CSP
import time
from queens.reines import reines as queen

file = open("queensLAPC2.csv","w",encoding='utf-8')
domains = range(10,21)


def printDom(rang):
  file.write("taille du domaine ;")
  for i in rang:
    file.write(str(i)+";")

def randomTest(rang):
  for i in rang:
    Queen = queen(i)
    csp = CSP(i, i, Queen.mp, Queen.Q)
    mp = csp.Mp.copy()

    t = time.time()
    if (csp.look_ahead(mp)):
      file.write(str(time.time() - t) + ";")

def heuristicTest(rang):
  for i in rang:
    Queen = queen(i)
    csp = CSP(i, i, Queen.mp, Queen.Q)
    mp = csp.Mp.copy()

    t = time.time()
    if (csp.look_ahead_heuristic(mp)):
      file.write(str(time.time() - t)+";")

if __name__ == "__main__" :
  printDom(domains)
  file.write("\ntime with random selection!")
  heuristicTest(domains)

  printDom(domains)
  file.write("\ntime with heuristic selection!")
  randomTest()

  file.close()