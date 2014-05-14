import pygame
from pygame.locals import *
from numpy import rot90, zeros

class Viewer:
    def __init__(self, world, w=280, h=180):
        self.world = world
        self.robots = []

        pygame.init()
        self.screen = pygame.display.set_mode((w,h))
        self.fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Robot Viewer')

        self.W = w
        self.H = h

        h,w = world.wmap.shape
        self.surface = pygame.Surface((w,h))
        pygame.surfarray.use_arraytype('numpy')
        self.locs = {}
        self.fps = 30

        self.showTrails = True

    def setShowTrails(self, value):
        self.showTrails = value

    def addRobot(self, robot):
        self.robots.append(robot)
        robot.addListener(self)
        self.locs[robot] = zeros((self.world.wmap.shape))
        self.fps = 20*len(self.robots)

    def notify(self, robot): 
        rloc = self.locs[robot]
        rloc[robot.y, robot.x] = 1.
        rloc *= .9
        self.draw()

    def draw(self):
        im = self.world.wmap.copy()
        for r in self.robots:
            if r.x != -1 and r.y != -1:
                im[r.y, r.x] = 255*255*255
                if self.showTrails:
                    im -= (self.locs[r]*300)
        pygame.surfarray.blit_array(self.surface, rot90(im,3))
        pygame.transform.scale(self.surface, (self.W, self.H), self.screen)
        pygame.display.update()
        self.fpsClock.tick(self.fps)
