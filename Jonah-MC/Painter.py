from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()

while True:
    for i in range(100):
        if y-1 != 0:
            mc.setBlock(x,y-1,z,35,i)
            x,y,z = mc.player.getPos()
    x,y,z = mc.player.getPos()
