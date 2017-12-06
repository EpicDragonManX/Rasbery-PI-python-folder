from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getPos()
lava1 = 10
lava2 = 11
while True:
    mc.setBlocks(x+1, y, z+1, x-1, y, z-1, lava2)
    mc.setBlocks(x+1, y+3, z+1, x-1, y+3, z-1, 246)
    #if mc.getBlock(x, y-1, z) != 0:
    #    mc.postToChat("You are standing on: " + str(mc.getBlock(x, y-1, z)))
    x,y,z = mc.player.getPos()
    time.sleep(0.5)
