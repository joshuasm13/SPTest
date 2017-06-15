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

from kivy.lib.osc         import oscAPI 

class SendFile():

    def build(self):
        oscAPI.init()

    def UpdateScreen(self, file, screen, number, size):

        ip = '127.0.0.1'
        port = 5000

        
        screen = str(screen)
        file = str(file)

        print("Sending Message to Screen: " + str(screen) + " - " + file )
        print("Image Slice: " + str(number) + "/" + str(size) + "\n")
       # oscAPI.sendMsg( '/tuios/screen_change', [screen, file], ipAddr= ip, port= port)

    def IPInfo(self, file):

        pass
        # ip = '198.21.242.1'
        # ip = '192.168.43.151'
        # ip = '127.0.0.1'
        #
        # port = 5000
        # print("Sending Message! " 3333 +tokenNum +)
        # oscAPI.sendMsg( '0', [tokenNum], ipAddr= ip, port= port)