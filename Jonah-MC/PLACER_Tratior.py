from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
#x,y,z = mc.player.getPos()

while True:
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    z = random.randint(-200, 200)

    mc.setBlock(x,y,z,random.randint(0, 100),random.randint(0, 100))
    print str(x) + ", " + str(y) + ", " + str(z)

    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    z = random.randint(-200, 200)
    
    mc.setBlock(x,y,z,random.randint(0, 100),random.randint(0, 100))
    print str(x) + ", " + str(y) + ", " + str(z)


"""
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    z = random.randint(-200, 200)

    mc.setBlock(x,y,z,57)
    print str(x) + ", " + str(y) + ", " + str(z)

    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    z = random.randint(-200, 200)
    
    mc.setBlock(x,y,z,0)
    print str(x) + ", " + str(y) + ", " + str(z)

    
    #print str(x) + ", " + str(y) + ", " + str(z)
    #mc.setBlock(x,y,z,0)
"""
    
