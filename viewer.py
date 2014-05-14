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
        self.loc = zeros((h,w))

    def addRobot(self, robot):
        self.robots.append(robot)
        robot.addListener(self)

    def notify(self): 
        self.draw()

    def draw(self):
        im = self.world.wmap.copy()
        for r in self.robots:
            if r.x != -1 and r.y != -1:
                self.loc[r.y, r.x] = 1.
                self.loc *= .9
                im[r.y, r.x] = 255*255*255
                im -= (self.loc*300)
        pygame.surfarray.blit_array(self.surface, rot90(im,3))
        pygame.transform.scale(self.surface, (self.W, self.H), self.screen)
        pygame.display.update()
        self.fpsClock.tick(30)
