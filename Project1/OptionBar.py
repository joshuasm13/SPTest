
        



# Add left and right main panels  -----
from kivy.app import App
from kivy.config import Config
from win32api import GetSystemMetrics

import sys
import os
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
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label
from  HelperFunctions import *
#from MainScreen import *
from kivy.uix.dropdown import DropDown

from FileBrowswer import FileBrowser

class OptionBar(RelativeLayout):

    layout = None
    slider = None

    file_browser = FileBrowser()

    def __init__(self, mainl, width, height):
        
        super(OptionBar, self).__init__()
    
        # Add Option bar to top of right panel -----
        #topOptionBar =  RelativeLayout(size = (width, resY *.04), size_hint_y = None)
        self.layout= mainl

        self.size = (width, height)
        self.size_hint_y = None
        self.orientation = 'horizontal'
    

        #self.fileBrowser = 
        self.file_browser.set_layout(self.layout)


        root = BoxLayout(size=self.size, orientation='horizontal', size_hint_y = None)
        self.add_widget(root)

       # with self.canvas.before:

           # Color(H.ranClr(), H.ranClr(), H.ranClr(), 1)  # green; colors range from 0-1 instead of 0-255
          #  self.rect1 = Rectangle(size=self.size, pos=self.pos)


        #FPS = FloorPlanSelector()
        #self.add_widget(Button(text="here"))
        #self.add_widget(self.createFloorPlanSelector(self.width*.25, self.height))

        root.add_widget(self.floorSelectBtn(self.width*.25, self.height))

        root.add_widget(self.browseBtn(self.width*.25, self.height))

        root.add_widget(self.settingsBtn(self.width*.25, self.height))
        #topOptionBar.add_widget(FPS)



    def floorSelectBtn(self, width, height):
        btn = Button(text= "Floor Plans", size_hint_y=None, size_hint_x = None, size = (width, height))
        openSlider = lambda btn:self.layout.openFloorSlider()
        btn.bind(on_release=openSlider)
        #lambda btn: dropdown.select(btn.text)
        return btn


    def browseBtn(self, width, height):
        btn = Button(text= "Add Files", size_hint_y=None, size_hint_x = None, size = (width, height))
        openPopup = lambda btn:self.file_browser.show_load()
        btn.bind(on_release=openPopup)
        #lambda btn: dropdown.select(btn.text)
        return btn

    def settingsBtn(self, width, height):
        btn = Button(text= "Settings", size_hint_y=None, size_hint_x = None, size = (width, height))
        openSlider = lambda btn:self.layout.openSettingsSlider()
        btn.bind(on_release=openSlider)
        #lambda btn: dropdown.select(btn.text)
        return btn




    def on_touch_down(self, touch):
        if super(OptionBar, self).on_touch_down(touch):
            return True
        if not self.collide_point(touch.x, touch.y):
            return False

        touch.grab(self)
        touch.ud[self] = True

        return True



