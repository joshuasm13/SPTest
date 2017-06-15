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
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from random import randint
from HelperFunctions import *
from SliderOptionBar import SliderOptionBar
from kivy.uix.label import Label
from kivy.core.window import Window

class FloorPlanSelector(Scatter):

    mainScreen = None
    def __init__(self, mainScreen):
        super(FloorPlanSelector, self).__init__()

       # self.size = (width , height)
        self.mainScreen= mainScreen
        self.do_scale = False
        self.do_rotation = False
        self.do_translation = False

        #self.pos = (width+10, 0)
    

        self.root = BoxLayout( orientation = 'vertical')
        self.add_widget(self.root)
        self.bind(size =self.updateSize, pos=self.updateSize)

        with self.root.canvas.before:
            Color(H.ranClr(), H.ranClr(), H.ranClr(), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect1 = Rectangle(size=self.size, pos_hint=self.pos)
        
        self.tiles = BoxLayout(size_hint_y = .96, orientation = 'vertical')
        
        #wid = Widget(size = (root.width, root.height*.96))
        self.options = SliderOptionBar(.04, self)
        #options = Button(text = 'bt 0', size_hint= (None,None), size = (root.width, root.height*.2))
        #options1 = Button(text = 'bt 1', size = (root.width, root.height*.5))
        #wid.add_widget(options)
        self.root.add_widget(self.options)
        self.root.add_widget(self.tiles)
    


        
    
        names = ["Rectangle1", "Triangle1", "Circle1", "Circle2", "Rectangle2", "Rectangle3", "Diamond1", "Diamond2"]

        for i in range(4):
            self.tiles.add_widget(BoxLayout(orientation = 'horizontal', size_hint_y = .25))

        count  = 0
        for child in self.tiles.children:
            for i in range (2):
                btn = Button(text= names[count], size_hint = (.5, .25), \
                    background_color =(H.ranClr(), H.ranClr(), H.ranClr())) 

                closeSlider = lambda btn:self.floorSelected(btn)
                btn.bind(on_release=closeSlider)

                child.add_widget(btn)
                count = count +1






    def open(self):
        anim = Animation(x=0, duration =.07) 
        anim.start(self)

    def close(self):
        anim = Animation(x=self.width+10, duration =.05)
        anim.start(self)

    def floorSelected(self, btn):
        self.close()
        self.mainScreen.changeFloorPlan(btn.text)


    def on_touch_down(self, touch):
        if super(FloorPlanSelector, self).on_touch_down(touch):
            return True
        if not self.collide_point(touch.x, touch.y):
            return False

        touch.grab(self)
        touch.ud[self] = True

        return True


    def updateSize(self, *args, **kwargs):
    	self.rect1 = self.size
    	self.updateRootSize()


    def updateRootSize(self, *args, **kwargs):
        self.root.size = self.size
        self.root.pos = self.rect1.pos = (self.width -20 , 0)
  		#self.updateHTiles()

    def updateHTileSize(self, *args, **kwargs):
    	pass
     #   self.options.size = self.size
       # for child in self.tiles.children:
       #		child.size = self.size * .4

    #def updateHTiles

       # for child in self.tiles:
       # 	child.height = self.tiles



