from represent import *
from random import *
from copy import deepcopy
from numpy import *

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

def crossOver(pgma, pgmb):
    pgm1 = deepcopy(pgma)
    pgm2 = deepcopy(pgmb)
    p1 = chooseRandomNode(pgm1)
    p2 = chooseRandomNode(pgm2)
    if isinstance(p1, IfStatement):
        if random.random() >= .5:
            child = p1.iftrue
            ctype = 0
        else:
            child = p1.iffalse
            ctype = 1
    else:
        child = p1.nextStep
        ctype = 2
    if isinstance(p2, IfStatement):
        if random.random() >= .5:
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
    if pgm1.getDepth() > 20:
        pgm1 = deepcopy(pgma)
    if pgm2.getDepth() > 20:
        pgm2 = deepcopy(pgmb)
    return [pgm1, pgm2]

ifPer = .45
mvPer = 1.-ifPer
def genNode(depth, maxdepth):
    if depth > maxdepth:
        return None 
    roll = random.random()
    if roll < ifPer:
        direction = randint(0,8)
        if direction == IfStatement.C:
            direction += 1
        node = IfStatement(direction)
        if depth == maxdepth:
            if random.random() > .5:
                node.iftrue = MoveStatement(randint(0,3))
            if random.random() > .5:
                node.iffalse = MoveStatement(randint(0,3))
        else:
            node.iftrue = genNode(depth+1, maxdepth)
            node.iffalse = genNode(depth+1, maxdepth) 
    else: 
        node = MoveStatement(randint(0,3))
        node.nextStep = genNode(depth, maxdepth)
    return node

def mutate(prgm):
    '''
    n = chooseRandomNode(prgm)
    child = genNode(0, randint(0,4))
    if isinstance(n, IfStatement):
        if random.random() >= .5:
            n.iftrue = child
        else:
            n.iffalse = child
    else:
        n.nextStep = child
    '''
    prgm.entry = genNode(0, randint(0, randint(1,5)))

def breed(population, metric, crossProb, mutateProb):
    if len(population) == 1:
        return deepcopy(population)
    fitness = [(pgm, metric(pgm)) for pgm in population]
    fitness.sort(lambda x,y : x[1] - y[1])

    if fitness[-1][1] != 0:
        fsum = float(sum(f[1] for f in fitness))
    else:
        fsum = 1.
    percent = array([f[1] / fsum for f in fitness])
    for i in range(len(percent)-1):
        percent[i+1] += percent[i]

    newpop = deepcopy([fitness[-1][0]])
    print [f[1] for f in fitness]
    while len(newpop) < len(population):
        n1 = deepcopy(fitness[where(percent >= random.random())[0][0]][0])
        if random.random() < crossProb:
            n2 = n1
            while n1 == n2:
                n2 = fitness[where(percent >= random.random())[0][0]][0]
            n1, n2 = crossOver(n1,n2)
            newpop.append(n2)
        if random.random() < mutateProb:
            mutate(n1)
        newpop.append(n1)

    if len(newpop) > len(population):
        newpop = newpop[:-1]        
    return newpop, fitness[-1][1]
