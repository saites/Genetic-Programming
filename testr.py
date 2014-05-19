from represent import *
from random import random, randint
from robot import *
from world import *

w = World('resources/star.bmp')
r = Robot(w, 1,1)
x,y = w.getRandOpen()
population = [Prgm(genNode(0)) for i in range(10)]
scores = [(pgm, pgm.resetExecuteScore(r,x,y)) for pgm in population]
scores.sort(lambda x,y : y[1] - x[1])
x.pass
print scores
