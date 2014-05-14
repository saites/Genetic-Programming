Genetic Programming
-------------------
Code for a simple robot simulator

Dependencies
-------------------
Makes use of numpy and scipy. If you want to use the viewer, you'll also need
pygame.

Files
-------------------
world.py -- Code to load in a bmp as a robot world. White spaces are
            interpreted as open space, and black spaces are considered walls.

            Example:
                w = World('star.bmp') # loads the 'star.bmp' file as a world
            Methods:
                isOpen(x,y):
                    returns True if the spot is an open space (white) and 
                    false otherwise.

robot.py -- Code for the robot; keeps score and informs listeners of changes.
            You should specify the world and the starting position for the
            robot. Positions are relative the bottom left corner.

            Example:
                r = Robot(w, 1, 1) # makes a new robot in the world w, starting
                                   # position (1,1)
            Methods:
                getView():
                    returns the robot's 3x3 view of the area around it
                getScore():
                    returns the robot's "score" with respect to wall following.
                    i.e., the number of spaces it touched that were next to
                    walls
                setLoc(x,y):
                    sets the robot's location to (x,y); relative the bottom 
                    left corner
                moveLeft(), moveRight(), moveUp(), moveDown():
                    moves the robot one space in that direction
                addListener(l):
                    appends l to the robot's list of listeners. The listener
                    should have a notify() method.
                notifyAll():
                    informs all listeners that the robot has changed locations

viewer.py -- Code for a simple view of the robot's movements.

            Example:
                v = Viewer(w) # creates a window sized 280*180 in which shows
                              # world. You can also specify the width and
                              # height to get a larger window.
            Methods:
                addRobot(r):
                    adds the robot r to the screen. It will be drawn and will
                    respond to updates.
                setShowTrails(value):
                    sets showTrails to value. If value is True (by default, it
                    is), then the robot's trails will be displayed on the
                    screen
                notify(robot):
                    the notify callback for the robot's notifyAll method
                draw():
                    draws the world and the robots

arrows.py -- Simple program for manipulating a robot in a world.

            Use:
                python arrows.py
                Now use the arrow keys to control the robot.


