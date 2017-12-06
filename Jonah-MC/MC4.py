from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getPos()
ptid = mc.getPlayerEntityIds()[1]
x2,y2,z2=mc.entity.getPos(ptid)

print mc.getPlayerEntityIds()[1]

mc.setBlocks(x2+1, y2-1, z2+1, x2-1, y2+2, z2-1, 46, 1)
mc.setBlock(x2, y2, z2, 0)
mc.setBlock(x2, y2+1, z2, 0)
i=0
while True:
    ptid = mc.getPlayerEntityIds()[1]
    x2,y2,z2=mc.entity.getPos(ptid)
    mc.setBlocks(x2+1, y2-1, z2+1, x2-1, y2+2, z2-1, i, 1)
    mc.setBlock(x2, y2, z2, 0)
    mc.setBlock(x2, y2+1, z2, 0)
    i+=1
    if i >= 51:
        i=0
    time.sleep(.25)
