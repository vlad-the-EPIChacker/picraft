import mcpi.minecraft as minecraft
mc = minecraft.Minecraft. create()

import time
import mcpi.block as block

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    TNT = 0

    mc.setBlock(x, y, z, block.TNT)

    time.sleep(0.2)
