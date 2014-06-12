from represent import *
from genetic import *
from robot import *
from world import *
from numpy import *
from matplotlib.pyplot import *

mapname = 'wideRoom.bmp'
programsLoc = 'programs'
w = World('resources/'+mapname)
r = Robot(w, 1,1)
mutateProb = 0.10
crossoverProb = .99
numGens = 100
population = [Prgm(genNode(0,5)) for i in range(500)]\
            +[Prgm(genNode(0,1)) for i in range(500)]
bestFit = zeros((numGens,1))
avgFit = zeros((numGens,1))

x,y = w.getRandOpen()
def metric(pgm):
    return pgm.resetExecuteScore(r,x,y)
for i in range(numGens):
    print i
    x,y = w.getRandOpen()
#    try:
    population, best, avgFit[i,0] =\
        breed(population, metric, crossoverProb, mutateProb)
    bestFit[i, 0] = best[1]
    with open('%s/pgm%d.py' % (programsLoc, i), 'w') as F:
        best[0].toView = True
        best[0].startPos = (x,y)
        best[0].mapname = mapname
        F.write(str(best[0]))
#    except RuntimeError as e:
#        print e
#        print "maximum recursion depth reached"
#        break

plot(bestFit)
show()
plot(avgFit)
show()
