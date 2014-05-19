from world import *
from numpy import pad, zeros, count_nonzero, logical_and
from scipy.ndimage.morphology import binary_dilation

class Robot:
    def __init__(self, world, x, y):
        self.world = world
        self.listeners = []
        self.viewMap = pad(world.wmap, 1, 'constant')
        self.nears = binary_dilation(world.wmap)
        self.reset(x,y)

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

    def getView(self):
        return self.viewMap[self.y:self.y+3, self.x:self.x+3]

    def getScore(self):
        return count_nonzero(logical_and(self.history, self.nears))

    def setLoc(self, x, y):
        self.numSteps += 1
        if(not self.world.isOpen(x,y)):
            return False
        else:
            self.x = x
            self.y = y
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
