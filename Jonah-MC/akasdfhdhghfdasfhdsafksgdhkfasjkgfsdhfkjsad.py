from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getPos()

mc.setBlocks(-2,-2,-2,102,102,102,5)
mc.postToChat("Cube created!")
time.sleep(1)

mc.setBlocks(-1,-1,-1,101,101,101,0)
mc.postToChat("Cube completed!")
time.sleep(1)

""" ORIGINAL
for x in range(100):
    for y in range(100):
        for z in range(100):
            if (x+y+z)%3==0 or (x+y+z)%7==2:
                mc.setBlock(x,y,z,1)
                print(str(x)+", "+str(y)+", "+str(z))
            elif (x+(y^2)+z)%3==4:
                mc.setBlock(x,y,z,2)
                print(str(x)+", "+str(y)+", "+str(z) + "   GRASS PLACED")
            else:
                mc.setBlock(x,y,z,0)
                print(str(x)+", "+str(y)+", "+str(z))
"""
for x in range(60):
    for y in range(60):
        for z in range(60):
            if (x+y+z)%3==0 or (x+y+z)%7==2:
                mc.setBlock(x,y,z,1)
                print(str(x)+", "+str(y)+", "+str(z))
            elif (x+(y^2)+z)%3==4:
                mc.setBlock(x,y,z,2)
                print(str(x)+", "+str(y)+", "+str(z) + "   GRASS PLACED")
            else:
                mc.setBlock(x,y,z,0)
                print(str(x)+", "+str(y)+", "+str(z))
