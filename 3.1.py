import sys
from turtle import *

class Disk:
    def __init__(self, name, x,y,height,width):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        up()
        
    def showdisk(self):
        
        goto(self.x,self.y)
        color("black")
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
        up()


    def newpos(self,x,y):
        self.x = x
        self.y = y
        goto(self.x)
        goto(self.y)
        
    
    def getH(self):
        return self.height
        
    def getW(self):
        return self.width
        
    

    def cleardisk(self):
        goto(self.x,self.y)
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
        up()


r = Disk('a',0,0,30,90)
s = Disk('b',0,30,30,45)
r.showdisk()
r.cleardisk()






        
