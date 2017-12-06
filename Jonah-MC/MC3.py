from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getPos()
while True:
    if mc.getBlock(x, y-1, z) == 8 or mc.getBlock(x, y-1, z) == 9:
        mc.player.setPos(x,y+0.15,z)
        mc.setBlock(x,y-1,z,45)
        x,y,z = mc.player.getPos()
    x,y,z = mc.player.getPos()
