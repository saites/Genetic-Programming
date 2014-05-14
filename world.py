from matplotlib.image import imread

class World:
    def __init__(self, imageName):
        self.wmap = (imread(imageName)[:,:,0]).astype(int)

    def isOpen(self, x, y):
        h,w = self.wmap.shape
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        return self.wmap[y,x] != 0
