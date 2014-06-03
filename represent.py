from robot import *
from genetic import *
from random import randint

class IfStatement(Functor):
    NW,N,NE,W,C,E,SW,S,SE = range(9)
    def __init__(self, direction=0):
        Functor.__init__(self, 2)
        self.dirx = direction % 3
        self.diry = direction / 3
        self.children = None 

    def __str__(self):
        return "if robot.getView()[%d,%d]:" % (self.diry, self.dirx)

    def getDepth(self):
        return max([0]+[c.getDepth() for c in self.children if c])+1

    def makeRand(self):
        self.dirx = randint(0,2)
        self.diry = randint(0,2)

class MoveStatement(Functor):
    UP,DOWN,LEFT,RIGHT = range(4)
    def __init__(self, move=0):   
        Functor.__init__(self, 2)
        self.move = move
        self.children = None 

    def getDepth(self):
        return max([0]+[c.getDepth() for c in self.children \
            if isinstance(c, IfStatement)])+1

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

    def makeRand(self):
        self.move = randint(0,3)

class PassStatement(Terminal):
    def __init__(self,parent=None):
        Terminal.__init__(self)
    def makeRand(self):
        pass
    def __str__(self):
        return "pass"

def execute(node, robot, maxSteps=1000):
    laststeps = -1
    while robot.numSteps < maxSteps and robot.numSteps != laststeps:
        laststeps = robot.numSteps
        while robot.numSteps < maxSteps:
            if isinstance(node, IfStatement):
                if robot.getView()[node.diry, node.dirx]:
                    node = node.children[0]
                else:
                    node = node.children[1]
            elif isinstance(node, MoveStatement):
                if node.move == MoveStatement.UP:
                    robot.moveUp()
                elif node.move == MoveStatement.DOWN:
                    robot.moveDown()
                elif node.move == MoveStatement.RIGHT:
                    robot.moveRight()
                elif node.move == MoveStatement.LEFT:
                    robot.moveLeft()
                node = node.children[0]
            else:
                break
        
def resetExecuteScore(robot, x, y, maxSteps=1000):
    robot.reset(x,y)
    execute(robot)
    return robot.getScore()

def stringMe(node, mapname, x, y, toView=True, maxSteps=1000):
    strList = [ 
        'from robot import *', 
        'from world import *',
        '',
        'w = World(\'resources/%s\')' % mapname,
        'robot = Robot(w, %d, %d)' % (x,y),
        '',
        ]

    if self.toView:
        strList += [
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
                        '\t\t\tprint robot.getScore()',
                        '\t\t\tsys.exit()',
                    '\t\telif event.type == KEYDOWN '
                        'and event.key == K_ESCAPE:',
                        '\t\t\tpygame.event.post(pygame.event.Event(QUIT))'
            ]
    else:
        strList += ['while(robot.numSteps < %d):' % maxSteps]

    printing = [(node, 1)]
    while printing:
        node, iLevel = printing.pop(0)
        if isinstance(node, PassStatement):
            strList.append('\t'*iLevel+"pass")
        elif isinstance(node, IfStatement):
            strList.append('\t'*iLevel+str(node))
            printing.append((node.iftrue, iLevel+1))
            strList.append('\t'*iLevel+"else:")
            printing.append((node.iffalse, iLevel+1))
        elif isinstance(node, MoveStatement):
            strList.append('\t'*iLevel+str(node))
            if node.nextStep is not None:
                self.strHelper(node.nextStep, strList, iLevel)

    def getDepth(self):
        if not self.entry:
            return 0
        return self.entry.getDepth()

    if not self.toView:
        strList.append('print robot.getScore()')
    return '\n'.join(strList)
