from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()
GRASS = 2
mc.setBlock(x,y+1,z,0)
#mc.player.setPos(100,100,100)

def DIGGER(xBound1, zBound1, xBound2, zBound2):
    for i in range(xBound1, xBound2):
        for j in range(0, 150):
            for k in range(zBound1, zBound2):
                print "Scanning" + str(i) + str(j) + str(k)
                if mc.getBlock(i,j,k) == GRASS:
                    print "Dirt Found"
                    mc.setBlocks(i, j-1, k, i, j-100, k, 0)
DIGGER(50, 60, 50, 60)
def EATER():
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    c = random.randint(0, 1000)
    while True:
        mc.setBlock(a, b, c, 0)
        #if mc.getBlock(a,b,c) != 0:
        print ("Eaten:" + str(a) + ", " + str(b) + ", " + str(c) + " " + str(mc.getBlock(a, b, c)))
        a = random.randint(60, 85)
        b = random.randint(3, 4)
        c = random.randint(47, 60)
        #mc.player.setPos(a, b, c)
        time.sleep(0.034)
EATER()
