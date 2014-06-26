import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
block = 1
air = 0
stone=1
wood=5
glass=102
door=64
brick=45

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
        floor(x,z,w,len,i)
    return

def elevator(x,z,f):
    h=5
    mc.setBlocks(x+1,0,z+1,x+1,f*h,z+1,air)
    y=0
    while True:
        while y < f*h:
            mc.setBlock(x+1,y,z+1,brick)
            if y>0:
                mc.setBlock(x+1,y-1,z+1,air)
            y=y+1
            time.sleep(1)

        while y > 0:
            mc.setBlock(x+1,y,z+1,air)
            mc.setBlock(x+1,y-1,z+1,brick)
            y=y-1
            time.sleep(1)
    

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
elevator(20,20,5)

