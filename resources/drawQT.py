import pygame, sys
from pygame.locals import *
from quadtree import *
from SmokeyConsts import *
from random import randint, choice

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

qt = QuadTree(0,0,SCREEN_W,SCREEN_H)

def drawQT(qt, surface):
    pygame.draw.rect(surface, RED, \
        pygame.Rect(qt.x1, qt.y1, (qt.x2-qt.x1)+1, (qt.y2-qt.y1)+1),1)
    if qt.hasPoint():
        pygame.draw.circle(surface, randColor(), qt.point, 1)
    if qt.isSubdivided():
        drawQT(qt.NE, surface)
        drawQT(qt.NW, surface)
        drawQT(qt.SE, surface)
        drawQT(qt.SW, surface)


for i in range(100):
    try:
        qt.insert((randint(0,SCREEN_W),randint(0,SCREEN_H)))
    except TooLowResolutionException:
        pass

realPoints = set([])
while True:
    screen.fill(WHITE)
    drawQT(qt, screen)
    
    if randint(0,1) is 1:
        try:
            p = (randint(0,SCREEN_W),randint(0,SCREEN_H))
            qt.insert(p)
            realPoints.add(p)
        except TooLowResolutionException:
            pass
    else:
        if len(realPoints) > 0:
            p = choice(list(realPoints))
            realPoints.remove(p)
            qt.remove(p)
            
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_a:
                try:
                    p = (randint(0,SCREEN_W),randint(0,SCREEN_H))
                    qt.insert(p)
                    realPoints.add(p)
                except TooLowResolutionException:
                    pass
            if event.key == K_r:
                if len(realPoints) > 0:
                    p = choice(list(realPoints))
                    realPoints.remove(p)
                    qt.remove(p)
        elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_focused():
            try:
                p = pygame.mouse.get_pos()
                qt.insert(p)
                realPoints.add(p)
            except TooLowResolutionException:
                pass

    myfont = pygame.font.SysFont("monospace", 10)
    label = myfont.render(str(pygame.mouse.get_pos()), 1, (0,255,0))
    screen.blit(label, (0, 0))
    pygame.display.update()
    fpsClock.tick(30)
