import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
block = 1
air = 0

x= 10
y= 11
z= 12
x2= x+10
y2= y+5
z2= z+8

mc.player.setPos(x+9,y+9,z-4)

i=0
while i<10:
    
    mc.setBlocks(x, y, z, x2, y2, z2, block)    
    z= z2
    z2= z+8
    i=i+1

mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air)

