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

class SliderOptionBar(RelativeLayout):

    parentLayout = None
    def __init__(self,  size_h_y, layout):
        super(SliderOptionBar, self).__init__()
    
        #self.size = (width, height)
        #self.size_hint = (1,1)
        self.size_hint_y = size_h_y
        self.parentLayout = layout


        #self.add_widget(Button(size=self.size))

        with self.canvas.before:

            Color(H.ranClr(), H.ranClr(), H.ranClr(), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect1 = Rectangle(size=self.size, pos_hint=self.pos)


        root = BoxLayout(size=self.size, orientation='horizontal', size_hint_y = None)
        self.add_widget(root)

        btn = Button(text="Back", size_hint_x = .25)
        closeSlider = lambda btn:self.parentLayout.close()
        btn.bind(on_release=closeSlider)




        root.add_widget(btn)
        root.add_widget(RelativeLayout(size_hint_x = .75))



    def updateSize(self, size):
    	self.rect1.size = size;


