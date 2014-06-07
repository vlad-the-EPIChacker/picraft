
import mcpi.minecraft as minecraft
import mcpi.block as block

 
""" clearZone clears an area and sets a stone floor
    takes two x,z pairs clears everything above 0y and then sets
    a stone floor at -1wy
    @author: goldfish"""
 
def clearZone( alocx, alocz, blocx, blocz ):
    mc.setBlocks( alocx, 0, alocz, blocx, 64, blocz, block.AIR )
    mc.setBlocks( alocx, -1, alocz, blocx, -1, blocz, block.GRASS )
 
def drawTower(x,z,h,w,material):
    mc.setBlocks(x,0,z,x+w,h,z+w,material)

def drawFloor(x,z,w,f,material):
    b = (f-1)*4
    t = f*4
    mc.setBlocks(x,b,z,x+w,t,z+w,material)
    #hollow it
    mc.setBlocks(x+1,b,z+1,x+w-1,t,z+w-1,block.AIR)
    #windows on 3 sides
    mc.setBlocks(x+w/2,b+1,z,x+w/2+1,t-2,z,block.GLASS_PANE)
    mc.setBlocks(x+w/2,b+1,z+w,x+w/2+1,t-2,z+w,block.GLASS_PANE)
    mc.setBlocks(x,b+1,z+w/2,x,t-2,z+w/2+1,block.GLASS_PANE)
    #door on 4th side
    if f == 1:
        mc.setBlock(x+w,0,z+w/2,64)
        mc.setBlock(x+w,1,z+w/2,64)
    else:
        mc.setBlocks(x+w,b+1,z+w/2,x+w,t-2,z+w/2+1,block.GLASS_PANE)

    # wooden floor
    mc.setBlocks(x+1,b-1,z+1,x+w-1,b-1,z+w-1,block.WOOD_PLANKS)

def getBlockId():
    hits = mc.events.pollBlockHits()
    for hit in hits:
        x=hit.pos.x
        y=hit.pos.y
        z=hit.pos.z
        block =mc.getBlock(x, y, z)
        print "id: "+str(block)

import time    
mc = minecraft.Minecraft.create(  )
clearZone( -20, -30, 20, 10 )
#drawTower(0,-30,10,1,block.WOOD)
drawFloor(-7,-6,7,1,block.STONE)
for i in range(1,10):
    drawFloor(-7,-6,7,i,block.STONE)

    
