import sys
from turtle import *

class Disk:
    def __init__(self, name, x,y,height,width,color):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        up()
        
    def showdisk(self):
        
        goto(self.x,self.y)
        begin_fill()
        color(self.color)
        down()
        forward(self.width/2)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width/2)
        end_fill()
        up()


    def newpos(self,x,y):
        self.x = x
        self.y = y
        
    def getH(self):
        return self.height

    def cleardisk(self):
        goto(self.x,self.y)
        begin_fill()
        color("white")
        down()
        forward(self.width/2)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width/2)
        end_fill()
        up()


'''r = Disk('a',0,0,30,90,"red")
s = Disk('b',0,30,30,45)
r.showdisk()
r.cleardisk()'''

class Pole:
    def __init__(self, name,stack,topPos ,x,y,thickness,length,color):
        self.name = name
        self.stack = stack
        self.topPos = topPos
        self.x = x
        self.y = y
        self.thickness = thickness
        self.length = length
        self.color = color

    def showpole(self):
        goto(self.x,self.y)
        color("black")
        down()
        begin_fill()
        forward(self.thickness/2)
        left(90)
        forward(self.length)
        left(90)
        forward(self.thickness)
        left(90)
        forward(self.length)
        left(90)
        forward(self.thickness/2)
        end_fill()
        up()

    def pushdisk(self,disk):
        
        self.stack.append(disk)
        disk.newpos(self.x , self.y+ (self.topPos*disk.height))
        disk.showdisk()
        self.topPos += 1

    def popdisk(self):
        a = self.stack.pop()
        a.cleardisk()
        self.topPos -= 1


        
        

        

        

p = Pole("a",[],0,0,0,20,120,"black")
p.showpole()

a = Disk("b",0,0,30,90,"red")
p.pushdisk(a)
p.pushdisk(Disk("b",0,0,30,90,"blue"))

p.popdisk()
p.popdisk()


#s.showdisk()




        






        
