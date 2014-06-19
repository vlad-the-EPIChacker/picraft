import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
block = 1
air = 0
stone=1
wood=5
glass=102
door=64

def clear(x, z, x2, z2):
    mc.setBlocks(x,0,z,x2,55,z2,air)

def floor(x, z, w, len,i):
    h=5
    hi=i*h
    mc.setBlocks(x,0+hi,z,x+w,h+hi,z+len,stone)#body#
    mc.setBlocks(x+1,0+1+hi,z+1,x+w-1,h-1+hi,z+len-1,air)#hollow#
    mc.setBlocks(x+1,0+hi,z+1,x+w-1,0+hi,z+len-1,wood)  #floor#
    mc.setBlocks(x+w/2-1,h/2+hi,z,x+w/2,h/2+1+hi,z,glass)#window#
    mc.setBlocks(x,h/2+hi,z+len/2-1,x,h/2+1+hi,z+len/2,glass)#window#
    mc.setBlock(x+w/2-1,h/2+hi-1,z+w,door,6)#door#
    mc.setBlock(x+w/2-1,h/2+hi,z+w,door,6)#door#
    mc.setBlocks(x+len,h/2+hi,z+len/2-1,x+len,h/2+1+hi,z+len/2,glass)#window#
def building(x,z,f):
    w=10
    len=10



    for i in range(0,f):
        floor(20,20,w,len,i)
    return
    

######################Main###############a######
    


x= -20
y= 0
z= 48.6
x2= 49
y2= 50
z2= 25
i=0


#clear(x, z, x2, z2)#
clear(0, 0, 50, 55)
#floor(20,20,10,10)#
building(20,20,5)


