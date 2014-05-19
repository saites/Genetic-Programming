from matplotlib.image import imread
from numpy import nonzero
from random import randint

class World:
    def __init__(self, imageName):
        self.wmap = (imread(imageName)[:,:,0]).astype(int)
        self.openspaces = nonzero(self.wmap)
        self.nopen = len(self.openspaces[0])

    def isOpen(self, x, y):
        h,w = self.wmap.shape
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return self.wmap[y,x] != 0

    def getRandOpen(self):
        p = randint(0,self.nopen-1)
        return (self.openspaces[1][p], self.openspaces[0][p])
