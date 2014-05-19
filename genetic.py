from represent import *
from random import random, choice, randint
from copy import deepcopy

def buildNodeList(node, nList):
    if not node:
        return nList
    elif isinstance(node, IfStatement):
        nList.append(node)
        buildNodeList(node.iftrue, nList)
        buildNodeList(node.iffalse, nList)
        return nList
    elif isinstance(node, MoveStatement):
        nList.append(node)
        buildNodeList(node.nextStep, nList)
        return nList

def chooseRandomNode(prgm):
    return choice(buildNodeList(prgm.entry, []))

def crossOver(pgm1, pgm2):
    pgm1 = deepcopy(pgm1)
    pgm2 = deepcopy(pgm2)
    p1 = chooseRandomNode(pgm1)
    p2 = chooseRandomNode(pgm2)
    if isinstance(p1, IfStatement):
        if random() >= .5:
            child = p1.iftrue
            ctype = 0
        else:
            child = p1.iffalse
            ctype = 1
    else:
        child = p1.nextStep
        ctype = 2
    if isinstance(p2, IfStatement):
        if random() >= .5:
            temp = p2.iftrue
            p2.iftrue = child
        else:
            temp = p2.iffalse
            p2.iffalse = child
    else:
        temp = p2.nextStep
        p2.nextStep = child
    if ctype == 0:
        p1.iftrue = temp
    elif ctype == 1:
        p1.iffalse = temp
    else:
        p1.nextStep = temp
    return [pgm1, pgm2]

ifPer = .45
mvPer = 1.-ifPer
def genNode(depth, maxdepth):
    if depth > maxdepth:
        return None 
    roll = random()
    if roll < ifPer:
        direction = randint(0,8)
        if direction == IfStatement.C:
            direction += 1
        node = IfStatement(direction)
        if depth == maxdepth:
            if random() > .5:
                node.iftrue = MoveStatement(randint(0,3))
            if random() > .5:
                node.iffalse = MoveStatement(randint(0,3))
        else:
            node.iftrue = genNode(depth+1, maxdepth)
            node.iffalse = genNode(depth+1, maxdepth) 
    else: 
        node = MoveStatement(randint(0,3))
        node.nextStep = genNode(depth, maxdepth)
    return node
