from represent import *
from random import random, randint

ifPer = .5
mvPer = 1.-ifPer

MAXDEPTH = 10
def genNode(depth):
    if depth > MAXDEPTH:
        return
    roll = random()
    if roll < ifPer:
        direction = randint(0,8)
        if direction == IfStatement.C:
            direction += 1
        node = IfStatement(direction)
        node.iftrue = genNode(depth+1)
        node.iffalse = genNode(depth+1) 
    else: 
        node = MoveStatement(randint(0,3))
        node.nextStep = genNode(depth+1)
    return node

prgm = Prgm(genNode(0))

print prgm
