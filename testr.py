from represent import *
from genetic import *
from robot import *
from world import *

mapname = 'star.bmp'
w = World('resources/'+mapname)
r = Robot(w, 1,1)
x,y = w.getRandOpen()
def metric(pgm):
    return pgm.resetExecuteScore(r,x,y)
mutateProb = 0.08
crossoverProb = 0.9

population = [Prgm(genNode(0,5)) for i in range(100)]
for i in range(1000):
    print i
    population = breed(population, metric, crossoverProb, mutateProb)

scores = [(pgm, pgm.resetExecuteScore(r,x,y)) for pgm in population]
scores.sort(lambda x,y : y[1] - x[1])
print scores
best = scores[0][0]
best.toView = True
best.startPos = (x,y)
best.mapname = mapname

with open('goodpgm.py', 'w') as F:
    F.write(str(best))
