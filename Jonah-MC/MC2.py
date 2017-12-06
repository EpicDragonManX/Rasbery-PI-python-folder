from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getPos()
i=0
while i!=10:
    x,y,z = mc.player.getPos()
    mc.player.setPos(x, y+1.5,z)
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y-1,z,4)
    i+=1
    time.sleep(0.4)
