from csp import CSP
import time

file = open("randomLAPC2.csv","w",encoding='utf-8')
domains = range(20,40)


def printDom(rang):
  file.write("taille du domaine ;")
  for i in rang:
    file.write(str(i)+";")

def randomTest(rang):
  for i in rang:
    csp = CSP(10, i, 15)  # 10 variables with 15 constraints
    mp = csp.Mp.copy()

    t = time.time()
    if (csp.look_ahead(mp)):
      file.write(str(time.time() - t) + ";")

def heuristicTest(rang):
  for i in rang:
    csp = CSP(10, i,15)  # 10 variables with 15 constraints
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