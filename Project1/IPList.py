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
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton


class IPList(ListView):
    list = None


    def __init__(self, iplist):
        super(IPList, self).__init__()

        #self.size = (width , height)
        #self.size_hint=(1, None)


        data = [{'text': i, 'is_selected': False} for i in iplist]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 25}

        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        self.adapter=list_adapter

