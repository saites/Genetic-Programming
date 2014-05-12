from world import *
from numpy import pad

class Robot:
    def __init__(self, world, x, y):
        self.world = world
        self.listeners = []
        if(not world.isOpen(x,y)):
            self.x = -1
            self.y = -1
        else:
            self.x = x
            self.y = y
        self.viewMap = pad(self.world.wmap, 1, 'constant')

    def getView(self):
        return self.viewMap[self.y:self.y+3, self.x:self.x+3]

    def setLoc(self, x, y):
        if(not self.world.isOpen(x,y)):
            return False
        else:
            self.x = x
            self.y = y
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
            l.notify()

    def addListener(self, l):
        self.listeners.append(l)
