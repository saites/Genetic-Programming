class IfStatement:
    NW,N,NE,W,C,E,SW,S,SE = range(9)
    def __init__(self, direction):
        self.dirx = direction % 3
        self.diry = direction / 3
        self.iftrue = None
        self.iffalse = None

    def __str__(self):
        return "if robot.getView()[%d,%d]:" % (self.diry, self.dirx)

class MoveStatement:
    UP,DOWN,LEFT,RIGHT = range(4)
    def __init__(self, move):   
        self.move = move
        self.nextStep = None

    def __str__(self):
        if self.move == MoveStatement.UP:
            mystr = "robot.moveUp()"
        elif self.move == MoveStatement.DOWN:
            mystr = "robot.moveDown()"
        elif self.move == MoveStatement.LEFT:
            mystr = "robot.moveLeft()"
        elif self.move == MoveStatement.RIGHT:
            mystr = "robot.moveRight()"
        return mystr

class Prgm:
    def __init__(self, entry=None):
        self.entry = entry
        self.toView = False
        self.maxSteps = 250

    def strHelper(self, node, strList, iLevel):
        if node == None:
            strList.append('\t'*iLevel+"pass")
        elif isinstance(node, IfStatement):
            strList.append('\t'*iLevel+str(node))
            self.strHelper(node.iftrue, strList, iLevel+1)
            strList.append('\t'*iLevel+"else:")
            self.strHelper(node.iffalse, strList, iLevel+1)
        elif isinstance(node, MoveStatement):
            strList.append('\t'*iLevel+str(node))
            if node.nextStep is not None:
                self.strHelper(node.nextStep, strList, iLevel)

    def __str__(self):
        strList = [ 
            'from robot import *', 
            'from world import *',
            '',
            'w = World(\'resources/star.bmp\')',
            'robot = Robot(w, 2, 2)' 
            '',
            ]
        if self.toView:
            strList.append([
                'from viewer import *', 
                'from pygame.locals import *',
                'import sys',
                'import pygame',
                '', 
                'v = Viewer(w,560,360)', 
                'v.addRobot(robot)', 
                'v.draw()',
                '',
                'while(True):',
                    '\tfor event in pygame.event.get():',
                        '\t\tif event.type == QUIT:',
                            '\t\t\tpygame.quit()',
                            '\t\t\tsys.exit()',
                        '\t\telif event.type == KEYDOWN '
                            'and event.key == K_ESCAPE:',
                            '\t\t\tpygame.event.post(pygame.event.Event(QUIT))'
                ])
        else:
            strList.append('while(robot.numSteps < {}):'.format(self.maxSteps))
        self.strHelper(self.entry, strList, 1)
        if not self.toView:
            strList.append('print robot.getScore()')
        return '\n'.join(strList)

