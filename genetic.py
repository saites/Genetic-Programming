from represent import *
from random import *
from copy import deepcopy
from numpy import *

def buildNodeList(node, nList):
    if not node:
        return nList
    elif isinstance(node, IfStatement):
        nList.append(node)
        buildNodeList(node.children[0], nList)
        buildNodeList(node.children[1], nList)
        return nList
    elif isinstance(node, MoveStatement):
        nList.append(node)
        buildNodeList(node.children[0], nList)
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
            child = p1.children[0]
            ctype = 0
        else:
            child = p1.children[1]
            ctype = 1
    else:
        child = p1.children[0]
        ctype = 2
    if isinstance(p2, IfStatement):
        if random.random() >= .5:
            temp = p2.children[0]
            p2.children[0] = child
        else:
            temp = p2.children[1]
            p2.children[1] = child
    else:
        temp = p2.children[0]
        p2.children[0] = child
    if ctype == 0:
        p1.children[0] = temp
    elif ctype == 1:
        p1.children[1] = temp
    else:
        p1.children[0] = temp
    if pgm1.getDepth() > 30:
        pgm1 = deepcopy(pgma)
    if pgm2.getDepth() > 30:
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
                node.children[0] = MoveStatement(randint(0,3))
            if random.random() > .5:
                node.children[1] = MoveStatement(randint(0,3))
        else:
            node.children[0] = genNode(depth+1, maxdepth)
            node.children[1] = genNode(depth+1, maxdepth)
    else: 
        node = MoveStatement(randint(0,3))
        node.children[0] = genNode(depth, maxdepth)
    return node

def mutate(prgm):
    '''
    n = chooseRandomNode(prgm)
    child = genNode(0, randint(1,5))
    if isinstance(n, IfStatement):
        if random.random() >= .5:
            n.children[0] = child
        else:
            n.children[1] = child
    else:
        n.children[0] = child
    '''
    return Prgm(genNode(0,randint(1,5)))

def breed(population, metric, crossProb, mutateProb):
    if len(population) == 1:
        return deepcopy(population)
    fitness = [(pgm, metric(pgm)) for pgm in population]
    fitness.sort(lambda x,y : x[1] - y[1])

    fitnesses = array([f[1] for f in fitness])
    meanfit = mean(fitnesses)
    bestfit = fitness[-1]
    print fitnesses

    fsum = 0.0
    for i in range(len(fitness)):
        fitness[i] = (fitness[i][0], fitness[i][1]+fitness[0][1])
        fsum += fitness[i][1]
    if fsum == 0:
        fsum = 1.
    percent = array([f[1] / fsum for f in fitness])
    for i in range(len(percent)-1):
        percent[i+1] += percent[i]

    newpop = deepcopy([fitness[-1][0]])
    while len(newpop) < len(population):
        if random.random() < crossProb:
            n1 = fitness[where(percent >= random.random())[0][0]][0]
            n2 = n1
            while n1 == n2:
                n2 = fitness[where(percent >= random.random())[0][0]][0]
            n1, n2 = crossOver(n1,n2)
            newpop.append(n2)
        else:
            n1 = deepcopy(fitness[where(percent >= random.random())[0][0]][0])
        if random.random() < mutateProb:
            n1 = mutate(n1)
        newpop.append(n1)

    if len(newpop) > len(population):
        newpop = newpop[:-1]        
    print [p.getDepth() for p in newpop]
    return newpop, bestfit, meanfit 
