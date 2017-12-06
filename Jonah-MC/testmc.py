from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()

for a in range(-50,50):
    for b in range(-50,50):
        for c in range(-50,50):
            mc.setBlock(a,b,c,35,random.randint(1,15))
            print(str(a) + ", " + str(b) + ", " + str(c))
