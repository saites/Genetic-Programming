from world import *
from robot import *
from viewer import *
import pygame
import sys

# setup the world, the viewer, and the robot
w = World('resources/wideRoom.bmp')
v = Viewer(w, 560, 360)
r = Robot(w, 2,2)
v.addRobot(r)
v.draw()

# read in commands and move the robot around
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print r.getScore()
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_UP:
                r.moveUp()
            elif event.key == K_DOWN:
                r.moveDown()
            elif event.key == K_LEFT:
                r.moveLeft()
            elif event.key == K_RIGHT:
                r.moveRight()
