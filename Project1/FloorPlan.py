import sys

import os

#sys.path.append(os.getcwd() + "/lib/garden.tei_knob/")



import kivy
from kivy.app import App
from kivy.properties     import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter    import Scatter
from kivy.uix.image      import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
#from kivy.graphics import canvas
#from kivy.graphics.instructions.CanvasBase import canvas
#from tei_knob import  Knob

from kivy.uix.video import Video
from kivy.core.audio import SoundLoader
import kivy
from kivy.lib.osc         import oscAPI 
from kivy.app import App
# Import clock (required by osc listener)
from kivy.clock           import Clock
#Wade made all changes related to resolution
from win32api import GetSystemMetrics
from HelperFunctions import *
import math
from kivy.graphics import Rectangle, Rotate, Translate, PushMatrix, PopMatrix
from random import random

from kivy.metrics import MetricsBase
from kivy.metrics import Metrics

class FloorPlan(RelativeLayout):

    num_screens = 16
    w = None
    h = None

    hitPoints = None
    collidedWidgets = None
    small_btn_size = None

    def __init__(self, width, height, name):

        super(FloorPlan, self).__init__()

        #self.size_hint = (None, None)
        #self.size = (width, height)

        self.width2 = width
        self.height2 = height
        self.w = width
        self.h = height
        self.hitPoints = []
        self.collidedWidgets = []



        #with self.canvas.before:

            #Color(H.rgb(222), H.rgb(58), H.rgb(58), 1)  # green; colors range from 0-1 instead of 0-255
            #self.rect2 = Rectangle(size=self.size, pos=self.pos)
        names = ["Rectangle1", "Triangle1", "Circle1", "Circle2", "Rectangle2", "Rectangle3", "Diamond1", "Diamond2"]
    
        if(name == names[0]):
            self.createRec1()
        elif(name == names[1]):
            self.createTriangle1()
        elif(name == names[2]):
            self.createCircle1()
        elif(name == names[3]):
            self.createCircle2(width, height)
        elif(name == names[4]):
            self.createRec2()
        elif(name == names[5]):
            self.createRec3()
        elif(name == names[6]):
            self.createDiamond1()
        elif(name == names[7]):
            self.createDiamond2()
        


    def createCircle2(self, width, height):



        fph = height
        fpw = width

        num_screens = 16

        curve = 20
        posX = []
        posY = []

        originX = (width/2) + (width*.05)
        originY = height/2
        radius = width* .25
        degree = -.3
        size = .06 * fph
        rotate = (180.0/num_screens)

        
        xcords = [00,00,00]
        ycords = [00,00,00]
    
        for i in range(0,num_screens+1,1):




            scatter1 = Scatter(do_translation = False, do_scale = False, do_rotation = False, size = (size,size*1.5 ), pos=(height-(i*80),height-(i*80)))


            scatter1.add_widget(Button(size=scatter1.size, text = str(i)))

            
            scatter1 = Scatter(do_translation = False, do_scale = False, \
            do_rotation = False, size = (size,size ), \
            pos=(self.getX(originX,radius,i*degree), self.getY(originY, radius,i*degree) ), rotation = i*15)
            scatter1.add_widget(Button(text = str(i), size=scatter1.size))
            scatter1.add_widget(Button(size=scatter1.size))
            

            self.add_widget(scatter1)
        


    def createCircle1(self):
        self.generic()
    def createDiamond1(self):
        self.generic()
    def createDiamond2(self):
        self.generic()
    def createTriangle1(self):
        self.generic()
    def createRec1(self):
        self.generic()
    def createRec2(self):
        self.generic()
    def createRec3(self):
        self.generic()


    def generic(self):

        num_screens = 16
        inches = kivy.metrics.inch(1.55)
        self.small_btn_size = inches/2
        print inches
    
        for i in range(1,9,1):

            scatter1 = Scatter(do_translation = False, do_scale = False, do_rotation = False, 
                size = (inches,inches*2), pos=((self.width2 *.1) + (i*inches), self.width2/6), size_hint = (None, None))
            bx = BoxLayout(size = scatter1.size, orientation = 'vertical')
            scatter1.add_widget(bx)

            tokenb = Button(size= (inches,inches), size_hint = (None, None), text = "token: " + str(i))
            anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')

            option = selectButton((inches/2),  str(i))
            anchor.add_widget(option)

            bx.add_widget(tokenb)
            bx.add_widget(anchor)

            self.add_widget(scatter1)

            self.hitPoints.append(option)

        for i in range(9,17,1):

            scatter1 = Scatter(do_translation = False, do_scale = False, do_rotation = False, 
                size = (inches,inches*2), pos=((self.width2 *.1) + ((i-8)*inches), self.width2/2), size_hint = (None, None))
            bx = abc(scatter1.size, str(i))
            scatter1.add_widget(bx)

            with bx.canvas.before:

                Color(H.rgb(200), H.rgb(22), H.rgb(0), 1)  # green; colors range from 0-1 instead of 0-255
                self.rect2 = Rectangle(size=bx.size, pos=bx.pos)

            tokenb = Button(size= (inches,inches), size_hint = (None, None), text = "token: " + str(i))

            anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')

            option = selectButton((inches/2),  str(i))
            anchor.add_widget(option)

            bx.add_widget(tokenb)
            bx.add_widget(anchor)

            self.add_widget(scatter1)

            self.hitPoints.append(option)



    def randX(self):
        return random()



    def getY(self, origin, radius, degrees):
        return origin + radius * math.cos(degrees)

    def getX(self, origin, radius, degrees):
        return origin + radius * math.sin(degrees)

    def checkCollision(self, main, wid, x, y):
        if(self.hitPoints):
            height = self.hitPoints[0].height



        for child in self.hitPoints:
            
            scatter_pos = (x,y)
            child_pos = child.to_window(child.x, child.y)

           # print "\n\n"
           # print scatter_pos
           # print child_pos

            #xy = child.to_window(child.x,child.y, relative = True)

            if self.inBounds(height, child_pos, scatter_pos) and  not ((wid, child) in self.collidedWidgets):

                self.collidedWidgets.append((wid, child))
                print "selected screen: " + str(child.getScreen())
                print "file: " + wid.getFileName() + "\n"

                

    def inBounds(self, height, btnxy, xy):
        height = btnxy[1] + self.small_btn_size
        width = btnxy[0]  + self.small_btn_size

        if (btnxy[0] <= xy[0] <= width and btnxy[1] <= xy[1] <= height):
            return True
        return False

    def clearCollisions(self):
        self.collidedWidgets = []


    def getCollisions(self):
        return self.collidedWidgets

class selectButton(Button):

    screen = None
    def __init__(self, dim, screen):

        super(selectButton, self).__init__()

        self.size = (dim, dim)
        self.text = screen
        self.size_hint = (None, None)
        self.screen = screen


    def getScreen(self):
        return self.screen

class abc(BoxLayout):
    screen = None

    def __init__(self, size, screen):

        super(abc, self).__init__()

        self.screen = screen
        self.orientation = 'vertical'
        self.size = size 


    def getScreen(self):
        return self.screen