from world import *
from numpy import pad, zeros, count_nonzero, logical_and, logical_not
from scipy.ndimage.morphology import binary_dilation

class Robot:
    def __init__(self, world, x, y):
        self.world = world
        self.listeners = []
        self.viewMap = pad(world.wmap, 1, 'constant')
        self.nears = binary_dilation((world.wmap-255).astype(bool))
        self.reset(x,y)
        self.notNears = logical_not(self.nears)

    def reset(self, x, y):
        self.history = zeros(self.world.wmap.shape)
        if(not self.world.isOpen(x,y)):
            self.x = -1
            self.y = -1
        else:
            self.x = x
            self.y = y
            self.history[y,x] = 1
        self.numSteps = 0
        self.lastx = -1
        self.lasty = -1
        self.score = 0

    def getView(self):
        return self.viewMap[self.y:self.y+3, self.x:self.x+3]

    def getScore(self):
        return self.score
        #return count_nonzero(logical_and(self.history, self.nears))

    def changeScore(self):
        if self.nears[self.lasty, self.lastx] and\
            self.nears[self.y, self.x] and\
            not self.history[self.y, self.x]:
            self.score += 1

    def setLoc(self, x, y):
        self.numSteps += 1
        self.lastx = self.x
        self.lasty = self.y
        if(not self.world.isOpen(x,y)):
            return False
        else:
            self.x = x
            self.y = y
            self.changeScore()
            self.history[y,x] = 1
            self.notifyAll()
            return True

    def moveLeft(self):
        return self.setLoc(self.x-1, self.y)

    def moveRight(self):
        return self.setLoc(self.x+1, self.y)

    def moveUp(self):
        return self.setLoc(self.x, self.y+1)

    def moveDown(self):
        return self.setLoc(self.x, self.y-1)

    def notifyAll(self):
        for l in self.listeners:
            l.notify(self)

    def addListener(self, l):
        self.listeners.append(l)
