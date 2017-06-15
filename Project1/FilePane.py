import kivy

        



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

from os import listdir
from os.path import isfile, join
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock

import glob
class FilePane(BoxLayout):

    tiles = None
    mainlayout = None
    slider = None
    startPath = None
    main = None
    count2 = 0

    count  = 0 
    total_size = 0
    images = ['.jpeg', '.png', '.jpeg', '.bmp', '.dpx', '.exr', '.gif', '.ico', '.jpg2000', '.jpg',
                '.jls', '.pam', '.pbm', '.pcx', '.pgm', '.pgmyuv', '.pic',
                '.ppm', '.ptx', '.sgi', '.ras', '.tga', '.tiff', '.webp', '.xbm',
                '.xface', '.xwd']


    def __init__(self, width, height, foldername, mainlayout):
        
        super(FilePane, self).__init__()
    
        # Add Option bar to top of right panel -----
        #topOptionBar =  RelativeLayout(size = (width, resY *.04), size_hint_y = None)

        self.size = (width, height)
        self.size_hint = (None,None)
        self.startPath = foldername
        self.auto_bring_to_front = False
        self.mainlayout = mainlayout


        self.orientation = 'horizontal'

        self.tiles = StackLayout(size = (width*.9, height), size_hint_x = None, padding=10, spacing=10)
        #print self.tiles.size    
        #print self.tiles.minimum_height


        self.tiles.bind(minimum_height = self.tiles.setter('height'))



        self.add_widget(self.tiles)


        r = RelativeLayout(height = self.height)
        scrollbar = Slider(orientation = 'vertical')
        

        r.add_widget(scrollbar)
        self.add_widget(r)



        print self.tiles.height

        try:
            dirs = os.listdir( foldername )

            # This would print all the files and directories
            for file in dirs:
                if(self.isImage(file)):
                    self.addFile(self.startPath+ "\\" + file, file)
        except OSError:
            print OSError
            print "FilePane: no files found"

        print self.tiles.height


        scrollbar.range = (0, self.tiles.height)
        scrollbar.bind(value = self.updatePos)





    def updatePos(self, instance, value):
        self.tiles.y = value





    def on_touch_down(self, touch):
        if super(FilePane, self).on_touch_down(touch):
            return False
        if not self.collide_point(touch.x, touch.y):
            return False

        touch.grab(self)
        touch.ud[self] = True

        return False


    


    def isImage(self,  file):
        for i in self.images:
            if(file.endswith(i)):
                return True



    def addFile(self, path, name): 

     
        r = RelativeLayout(size_hint =(None,None))
        file = FileWidget(path, name, self, r)

 
        r.add_widget(file)
  
        r.size = file.size

        self.total_size += r.size[1]
        self.tiles.height = self.total_size - self.height
    
        self.tiles.add_widget(r)




    def getMain(self):
        return self.mainlayout;
    def getRoot(self):
        return self.tiles









class FileWidget(Scatter):
    file_pane_layout  = None


    original_pos = None
    original_size = None
    main_layout = None
    image = None
    file_name = None

    touch_pos = (0,0)
    check = None
    RL = None


    def __init__(self, path, name, layout, r):
        
        super(FileWidget, self).__init__()
        self.do_rotation = False
        self.do_transformation = True
        self.do_scale = False
    
        self.size_hint = (None, None)
        self.file_pane_layout = layout.getRoot()
        self.main_layout = layout.getMain()
        self.original_pos = self.pos
        self.file_name = name

        self.image = img = Image(source = path)

        #self.size = img.texture.size

        img.size = (img.texture.size[0]*.4, img.texture.size[1]*.4)


        self.size = self.original_size = img.size

        self.RL = RelativeLayout(size = self.size, size_hint = (None, None))

        self.RL.add_widget(img)
        self.add_widget(self.RL)


    def getFileName(self):
        return self.file_name

    def get_t(self):

        t =  self.to_window(self.get_touch_x(), self.get_touch_y())

     
        self.main_layout.checkCollision(self, t)

    def get_touch_x(self):
        return self.touch_pos[0]
    def get_touch_y(self):
        return self.touch_pos[1]



    

    def on_touch_down(self, touch):
        x, y = touch.x, touch.y





        # if the touch isnt on the widget we do nothing
        if not self.do_collide_after_children:
            if not self.collide_point(x, y):
                return False

        # let the child widgets handle the event if they want
        touch.push()
        touch.apply_transform_2d(self.to_local)
        if super(Scatter, self).on_touch_down(touch):

            # ensure children don't have to do it themselves
            if 'multitouch_sim' in touch.profile:
                touch.multitouch_sim = True
            touch.pop()
            self._bring_to_front(touch)



            return True
        touch.pop()

        # if our child didn't do anything, and if we don't have any active
        # interaction control, then don't accept the touch.
        if not self.do_translation_x and \
                not self.do_translation_y and \
                not self.do_rotation and \
                not self.do_scale:
            return False

        if self.do_collide_after_children:
            if not self.collide_point(x, y):
                return False

        if 'multitouch_sim' in touch.profile:
            touch.multitouch_sim = True
        # grab the touch so we get all it later move events for sure
        self._bring_to_front(touch)
        touch.grab(self)
        self._touches.append(touch)
        self._last_touch_pos[touch] = touch.pos



        self.opacity = .5

        abc = lambda btn:self.get_t()

        self.check = Clock.schedule_interval(abc, .02)






        #self.image.size = (self.image.texture.size[0]*.4, self.image.texture.size[1]*.4)


        #self.size = self.image.size
        return True




    def on_touch_move(self, touch):
        x, y = touch.x, touch.y


        if self.collide_point(x, y) and not touch.grab_current == self:
            touch.push()
            touch.apply_transform_2d(self.to_local)
            if super(Scatter, self).on_touch_move(touch):
                touch.pop()
                return True
            touch.pop()
        else:

            #print "here"
            self.touch_pos = (touch.x, touch.y)


           # print touch
           # print self.touch_pos
           # print touch.x
          #  print touch.y
            pass




        # rotate/scale/translate
        if touch in self._touches and touch.grab_current == self:
            if self.transform_with_touch(touch):
                self.dispatch('on_transform_with_touch', touch)
            self._last_touch_pos[touch] = touch.pos

        # stop propagating if its within our bounds
        if self.collide_point(x, y):
            return True



    def on_touch_up(self, touch):
        x, y = touch.x, touch.y

        try:
            self.check.cancel()
        except:
            pass

        if not touch.grab_current == self:
            touch.push()
            touch.apply_transform_2d(self.to_local)
            if super(Scatter, self).on_touch_up(touch):
                touch.pop()

                return True
            touch.pop()
        else:
            self.check.cancel()
            self.main_layout.clearCollisions()
            self.opacity = 1
            self.pos = self.original_pos
            self.size = self.original_size
            self.touch_pos = (0,0)
      
        # remove it from our saved touches
        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)

        # stop propagating if its within our bounds
        if self.collide_point(x, y):


            return True

