from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
#x,y,z = mc.player.getPos()

mc.setBlocks(-200,-150,-200,200,150,200,0)
mc.setBlocks(-2.00,-6.4,-2.00,2.00,6.0,-2.00,2)
time.sleep(5)

def rbd():
    g = random.randint(0, 7)
    #if g == 7:
    #    return "DogCatBobJellyfish"
    return g

while True:
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    z = random.randint(-200, 200)

    mc.setBlock(x,y,z,random.randint(0, 100),rbd())
    mc.setBlocks(-200,-64,-200,200,-60,-200,2)
