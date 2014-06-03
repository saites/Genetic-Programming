from represent import *
from genetic import *
from robot import *
from world import *
from numpy import *
from matplotlib.pyplot import *

mapname = 'emptyRoom.bmp'
w = World('resources/'+mapname)
r = Robot(w, 1,1)
numGens = 100

x,y = w.getRandOpen()
def metric(pgm):
    return pgm.resetExecuteScore(r,x,y)

functors = [IfStatement, MoveStatement]
terminals = [PassStatement]
GP = GeneticProgram(functors, terminals, metric)
GP.genPopulation({i:50 for i in range(1,6)})

bestFit = zeros((numGens,1))
for i in range(numGens):
    print i
    x,y = w.getRandOpen()
    GP.breed()
    print [f[1] for f in GP.fitness]
    bestFit[i,0] = GP.fitness[0][1]


print [f[1] for f in GP.fitness]
best = GP.fitness[-1][0]
prgm = stringMe(best, mapname, x, y)

with open('goodpgm.py', 'w') as F:
    F.write(prgm)

print prgm
plot(bestFit)
show()
