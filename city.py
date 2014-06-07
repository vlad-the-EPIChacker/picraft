import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
block = 1
air = 0
stone=1
wood=5
glass=20
door=324

def clear(x, z, x2, z2):
    mc.setBlocks(x,0,z,x2,55,z2,air)

def floor(x, z, w, len):
    h=5
    mc.setBlocks(x,0,z,x+w,h,z+len,stone)#body#
    mc.setBlocks(x+1,0+1,z+1,x+w-1,h-1,z+len-1,air)#hollow#
    mc.setBlocks(x+1,0,z+1,x+w-1,0,z+len-1,wood)  #floor#
    mc.setBlocks(x+w/2-1,h/2,z,x+w/2,h/2+1,z,glass)#window#
    mc.setBlocks(x,h/2,z+len/2-1,x,h/2+1,z+len/2,glass)#window#
    mc.setBlocks(x+w/2-1,h/2,z+w,x+w/2,h/2+1,z+w,door)#window#
    mc.setBlocks(x+len,h/2,z+len/2-1,x+len,h/2+1,z+len/2,glass)#window#


######################Main######################
    


x= -20
y= 0
z= 48.6
x2= 49
y2= 50
z2= 25
#clear(x, z, x2, z2)#
clear(0, 0, 50, 55)
floor(20,20,10,10)