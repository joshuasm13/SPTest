import kivy

        



        # Add left and right main panels  -----
from kivy.app import App
from kivy.config import Config
from win32api import GetSystemMetrics

resolution = [GetSystemMetrics(0), GetSystemMetrics(1)]
resX = resolution[0] 
resY = resolution [1]

#resY = 500

Config.set('graphics', 'width', str(resX))

Config.set('graphics', 'height', str(resY))
Config.set('graphics', 'fullscreen', 'auto')

import sys
import os

from kivy.uix.pagelayout import PageLayout
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

from kivy.core.window import Window

class Main(App):
    A = None
    B = None

    def build(self):


        root = BoxLayout (orientation = 'horizontal')

        self.A = a = BoxLayout(size_hint = (.75, 1), orientation = 'vertical')
        self.B = b = BoxLayout(size_hint = (.25, 1), orientation = 'vertical')

        print resX
        root.add_widget(a)
        root.add_widget(b)
        d = Scatter(size_hint=(.5,1))
        a.add_widget(d)
  



        with d.canvas.before:

            Color(.5,.2, .1, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect1 = Rectangle(size=d.size, pos=d.pos)



        a.bind(size =self.f, pos= self.f)


        return root

    def f(self, *args, **kwargs):
        self.rect1.size = self.A.size
        print self.A.size



Main().run()