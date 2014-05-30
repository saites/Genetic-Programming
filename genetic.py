    from random import *
    from copy import deepcopy
    from numpy import *

    class Functor:
        def __init__(self,maxChildren):
            self.children = None
            self.maxChildren = maxChildren
        def getDepth(self):
            return max([0]+[c.getDept() for c in self.children if c])+1
        def __str__(self):
            return ""
        def makeRand(self):
            pass

    class Terminal:
        def __init__(self):
            pass
        def getDepth(self):
            return 1
        def __str__(self):
            return ""
        def makeRand(self):
            pass

    def getNodeList(node):
        toProcess = node
        while toProcess:
            nList.append(toProcess.pop())
            toProcess.extend([n for n in node.children if n])
        return nList

    def chooseRandomNode(prgm):
        return choice(getNodeList(prgm.entry))

    class GeneticProgram:
        def __init__(self, functors, terminals, crossDepth=20, genDepth=5,
                     crossProb=.95, mutateProb=.05, metric):
            self.functors = functors
            self.terminals = terminals
            self.crossDepth = crossDepth
            self.genDepth = genDepth
            self.crossProb = crossProb
            self.mutateProb = mutateProb
            self.metric = metric

        def genNode(self, depth, maxdepth, functors, terminals):
            if depth > maxdepth:
                return None
            if depth == maxdepth:
                n = choice(terminals)()
                n.makeRand()
            else:
                n = choice(functors)()
                n.makeRand()
                n.children = [genNode(depth+1, maxdepth, functors, terminals)\
                                for i in range(n.maxChildren)]       
            return n
            
        def genPopulation(self, popSizeDict):
            '''
            popSizeDict should be a dictionary that tells how many individuals
            should be built at each size:
                {1: 50, 2: 50, 3: 30} creats 50 at each depth 1 and 2, and 
                30 more at depth 3.
            '''
            self.population = []
            for depth in popSizeDict:
                self.population +=
                    [self.genNode(0, depth, self.functors, self.terminals))\
                    for i in range(popSizeDict[depth]]

        def crossOver(pgma, pgmb):
            pgm1 = deepcopy(pgma)
            pgm2 = deepcopy(pgmb)
            p1 = chooseRandomNode(pgm1)
            p2 = chooseRandomNode(pgm2)

            if p1.children:
                c1i = randint(0,len(p1.children)-1)
                c1 = p1.children.pop(c1i)
            else:
                c1 = None

            if p2.children:
                c2i = randint(0,len(p2.children)-1)
                c2 = p2.children.pop(c2i)
            else:
                c2 = None

            if c1:
                p2.insert(c2i, c1)
            if c2:
                p1.insert(c1i, c2)

            if pgm1.getDepth() > self.crossdepth:
                pgm1 = deepcopy(pgma)
            if pgm2.getDepth() > self.crossdepth:
                pgm2 = deepcopy(pgmb)
            return [pgm1, pgm2]

        def mutate(prgm):
            prgm.entry = self.genNode(0, randint(0, randint(1,5)))
                

    def breed(self):
        if len(self.population) == 1:
            return deepcopy(self.population)
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
