from represent import *
from genetic import *
from robot import *
from world import *
from numpy import *
from matplotlib.pyplot import *

mapname = 'emptyRoom.bmp'
w = World('resources/'+mapname)
r = Robot(w, 1,1)
mutateProb = 0.1
crossoverProb = 0.9
numGens = 100
population = [Prgm(genNode(0,5)) for i in range(100)]\
            +[Prgm(genNode(0,3)) for i in range(100)]\
            +[Prgm(genNode(0,1)) for i in range(100)]
bestFit = zeros((numGens,1))

x,y = w.getRandOpen()
def metric(pgm):
    return pgm.resetExecuteScore(r,x,y)
for i in range(numGens):
    print i
    x,y = w.getRandOpen()
    population, bestFit[i,0] =\
        breed(population, metric, crossoverProb, mutateProb)

scores = [(pgm, pgm.resetExecuteScore(r,x,y)) for pgm in population]
scores.sort(lambda x,y : y[1] - x[1])
print scores

best = scores[0][0]
best.toView = True
best.startPos = (x,y)
best.mapname = mapname

with open('goodpgm.py', 'w') as F:
    F.write(str(best))

print bestFit
plot(bestFit)
show()
