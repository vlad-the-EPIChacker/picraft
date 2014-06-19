import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
while True:
    time.sleep(10)
    points = 0

    hits = mc.events.pollBlockHits()



    for hit in hits:
        x=hit.pos.x
        y=hit.pos.y
        z=hit.pos.z
        block =mc.getBlock(x, y, z)
        points =points + block
        mc.postToChat("You got " +str(block) + " points.")
    
                            

