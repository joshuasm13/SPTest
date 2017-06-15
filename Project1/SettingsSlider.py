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
from HelperFunctions import *
from SliderOptionBar import SliderOptionBar
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListView
from IPList import IPList

from kivy.uix.popup import Popup

class SettingsSlider(Scatter):


    IP = None
    def __init__(self, mainScreen):
        super(SettingsSlider, self).__init__()

        #self.size = (width , height)
        self.mainScreen= mainScreen
        self.do_scale = False
        self.do_rotation = False
        self.do_translation = False

       # self.pos = (width+10, 0)
    

        self.root = BoxLayout( orientation = 'vertical')
        self.add_widget(self.root)


        with self.root.canvas.before:

            Color(H.ranClr(), H.ranClr(), H.ranClr(), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect1 = Rectangle(size=self.size, pos_hint=self.pos)
        
        self.tiles = BoxLayout(size_hint_y = .96, orientation = 'vertical')


        with self.tiles.canvas.before:

            Color(H.ranClr(), H.ranClr(), H.ranClr(), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect2 = Rectangle(size = self.tiles.size, pos_hint=self.pos)
        
        #wid = Widget(size = (root.width, root.height*.96))
        self.options = SliderOptionBar( .04, self)
        #options = Button(text = 'bt 0', size_hint= (None,None), size = (root.width, root.height*.2))
        #options1 = Button(text = 'bt 1', size = (root.width, root.height*.5))
        #wid.add_widget(options)
        self.root.add_widget(self.options)
        self.root.add_widget(self.tiles)
        #options.draw1()
        #root.add_widget(tiles)


        self.IP = IpPopup()

        self.tiles.add_widget(self.createIPButton())
        
        self.bind(size =self.updateSize1, pos=self.updateSize1)

        
    def createIPButton(self):
        btn = Button(text= "Edit IP Adresses", size_hint_y = .1)

        openIPPopup = lambda btn:self.IP.show_edit()
        btn.bind(on_release=openIPPopup)

        return btn


    def open(self):
        anim = Animation(x=0, duration =.07) 
        anim.start(self)

    def close(self):
        anim = Animation(x=self.width+10, duration =.05)
        anim.start(self)

    def floorSelected(self, btn):
        self.close()
        #self.mainScreen.changeFloorPlan(btn.text)

    def on_touch_down(self, touch):
        if super(SettingsSlider, self).on_touch_down(touch):
            return True
        if not self.collide_point(touch.x, touch.y):
            return False

        touch.grab(self)
        touch.ud[self] = True

        return True

    def updateSize(self, size):

    	self.rect1.size = size
    	self.rect2.size = size
    	self.options.size = size
    	self.tiles.size = size

    	print self.tiles.size
    	for child in self.root.children:
    		child.size = size


    def updateSize1(self, *args, **kwargs):

    	#self.rect1.size = size
    	#self.rect2.size = size
    	self.options.size = self.size
    	self.tiles.size = self.size



class IpPopup(RelativeLayout):

    def __init__(self):
        super(IpPopup, self).__init__()

    ipAdresses = ['127.0.0.1']
    
    for i in range(50):
        strn = str(randint(0,256)) + "." +  str(randint(0,256)) + "." + str(randint(0,256)) + "!" +str(randint(0,256))
        ipAdresses.append(strn)

    def show_edit(self):

        content = self.createEditDialog()
        self._popup = Popup(title="Edit IP Addresses", content=content,
                            size_hint=(0.5, 0.5))
        self._popup.open()


    def add(self, item):
        self.ipAdresses.append(item)
    def remove(self, item):
        self.ipAdresses.remove(item)


    def createEditDialog(self):
        dialog = BoxLayout(size = self.size, pos = self.pos, orientation = "horizontal")
        dialog.add_widget(IPList(self.ipAdresses))

        bx = BoxLayout(size_hint_x = .3, orientation = "vertical")
        remove = Button (text = "Remove")
        newip=  Button(text = "New IP")

        bx.add_widget(newip)
        bx.add_widget(remove)
        #dialog.add_widget(RelativeLayout(size_hint_y = .05))
        dialog.add_widget(bx)



        return dialog










































