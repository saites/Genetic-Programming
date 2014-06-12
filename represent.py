from robot import *
from copy import copy

class IfStatement:
    NW,N,NE,W,C,E,SW,S,SE = range(9)
    def __init__(self, direction):
        self.dirx = direction % 3
        self.diry = direction / 3
        self.children = [None, None]

    def __str__(self):
        return "if robot.getView()[%d,%d]:" % (self.diry, self.dirx)

class MoveStatement:
    UP,DOWN,LEFT,RIGHT = range(4)
    def __init__(self, move):   
        self.move = move
        self.children = [None]

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
        self.maxSteps = 1000
        self.startPos = (-1,-1)
        self.mapname = ''

    '''
    def deepcopy(self):
        new = copy(self.entry)
        q = [(new, c, i) for (i,c) in enumerate(new.children) if c]
        while q:
            p,c,i = q.pop(0)
            p.children[i] = copy(c)
            q.extend([(c, cc, i) for (i,cc) in enumerate(c.children) if cc])
        retval = copy(self)
        retval.entry = new
        return retval
        '''

    def execute(self, robot):
        laststeps = -1
        while robot.numSteps < self.maxSteps and robot.numSteps != laststeps:
            node = self.entry
            laststeps = robot.numSteps
            while robot.numSteps < self.maxSteps:
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

    def resetExecuteScore(self, robot, x, y):
        robot.reset(x,y)
        self.execute(robot)
        return robot.getScore()

    def strHelper(self, node, strList, iLevel):
        if node == None:
            strList.append('\t'*iLevel+"pass")
        elif isinstance(node, IfStatement):
            strList.append('\t'*iLevel+str(node))
            self.strHelper(node.children[0], strList, iLevel+1)
            strList.append('\t'*iLevel+"else:")
            self.strHelper(node.children[1], strList, iLevel+1)
        elif isinstance(node, MoveStatement):
            strList.append('\t'*iLevel+str(node))
            if node.children[0] is not None:
                self.strHelper(node.children[0], strList, iLevel)

    def __str__(self):
        strList = [ 
            'from robot import *', 
            'from world import *',
            '',
            'w = World(\'resources/{}\')'.format(self.mapname),
            'robot = Robot(w, {}, {})'\
                .format(str(self.startPos[0]), str(self.startPos[1])),
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
            strList.append('while(robot.numSteps < {}):'.format(self.maxSteps))
        self.strHelper(self.entry, strList, 1)
        if not self.toView:
            strList.append('print robot.getScore()')
        return '\n'.join(strList)

    def getDepth(self):
        if not self.entry:
            return 0
        q = [(1, self.entry)]
        maxd = 1
        while q:
            d, n = q.pop(0)
            maxd = max(d, maxd)
            q += [(d+1,c) for c in n.children if isinstance(c,IfStatement)]
            q += [(d,c) for c in n.children if isinstance(c,MoveStatement)]
        return maxd
