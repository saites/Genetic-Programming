from robot import *
from world import *
from sys import argv

if len(argv) != 2:
    print "usage: %s worldname.bmp" % argv[0]
    exit()

w = World(argv[1])
r = Robot(w, 1,1)

print count_nonzero(r.nears - (w.wmap-255).astype(bool))
