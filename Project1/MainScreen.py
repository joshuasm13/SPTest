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
from FloorPlanSelector import FloorPlanSelector
from FloorPlan import FloorPlan
from  HelperFunctions import *
from OptionBar import OptionBar
from FilePane import FilePane
from SettingsSlider import SettingsSlider
from SendFile import SendFile
from kivy.core.window import Window

class MainScreen(App):
    LP = None
    RP =  None
    filePlaceHolder = None
    floorPlanSlider = None
    settingsSlider = None
    floor_plan = None
    RP2 = None
    PRP = None

    def build(self):

        root = BoxLayout(orientation = 'horizontal', padding = 30, spacing = 30)

       

        # Create Left Panel and add to root
        leftPanel = self.LP = RelativeLayout(size_hint_x = .75)
     	leftPanel.bind(size =self.updateLeftPanelSize, pos=self.updateLeftPanelSize)


        with leftPanel.canvas.before:

            Color(H.rgb(2), H.rgb(223), H.rgb(232), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect1 = Rectangle(size=leftPanel.size, pos=leftPanel.pos)
        root.add_widget(leftPanel)

        # Create RightPanel's Parent container (its only child) and add right panel. Add parent to root. 
        self.PRP = parentRightPanel = RelativeLayout(size_hint_x = .25)
     	parentRightPanel.bind(size =self.updateRightPanelSize, pos=self.updateRightPanelSize)

        with parentRightPanel.canvas.before:

            Color(H.rgb(58), H.rgb(58), H.rgb(58), 1)  # green; colors range from 0-1 instead of 0-255
            self.rect2 = Rectangle(size=parentRightPanel.size, pos=parentRightPanel.pos)

        
        self.RP2 = BoxLayout(orientation='vertical')
        parentRightPanel.add_widget(self.RP2)

        rightPanel = self.RP = BoxLayout(orientation='vertical')
        parentRightPanel.add_widget(rightPanel)
        root.add_widget(parentRightPanel)


        # Add default floorplan to leftpanel
        leftPanel.add_widget(FloorPlan(resX*.75, resY, 4))


        #Add FloorPlan slider to right panel
        self.floorPlanSlider = FloorPlanSelector(self)
        parentRightPanel.add_widget(self.floorPlanSlider)

        self.settingsSlider = SettingsSlider( self)
        parentRightPanel.add_widget(self.settingsSlider)



        '''
        optionBar = OptionBar(self, rightPanel.width, resY *.04)
        
        rightPanel.add_widget(optionBar)    


        self.filePlaceHolder = RelativeLayout(size = (rightPanel.width, resY*.96))
        self.RP2.add_widget(RelativeLayout(size = (rightPanel.width, resY*.04)))
        self.RP2.add_widget(self.filePlaceHolder)

        rightPanel.add_widget(RelativeLayout(size = (rightPanel.width, resY*.96)))
    
        
        self.changeFloorPlan("Rectangle1")
        self.changeFilePane('C:\\Users\\jsm4\\Desktop\\Project1\\images')
		'''

        return root





    def getLeftPanel(self):
        return self.LP

    def getRightPanel(self):
        return self.RP

    def openFloorSlider(self):
        self.floorPlanSlider.open()

    def openSettingsSlider(self):
        self.settingsSlider.open()

    def changeFilePane(self, filename):
        self.filePlaceHolder.clear_widgets()
        self.filePlaceHolder.add_widget(FilePane(self.RP.width, resY*.96, filename, self))


    def changeFloorPlan(self, name):

        #print name
        names = ["Rectangle1", "Triangle1", "Circle1", "Circle2", "Rectangle2", "Rectangle3", "Diamond1", "Diamond2"]
        for i in range(8):
            if(name == names[i]):

                try:
                    self.floor_plan.disabled = True
                except:
                    pass


                self.LP.clear_widgets()

                self.floor_plan = FloorPlan(self.LP.width, resY, name)

                self.LP.add_widget(self.floor_plan)



    def checkCollision(self, wid, xy):
        x = xy[0]
        y = xy[1]
        self.floor_plan.checkCollision(self, wid, x, y)

    def signalScreenUpdate(self, file, screen, count, size):
        send = SendFile()
        send.build()
        send.UpdateScreen(file, screen, count, size)


    def clearCollisions(self):
        print "here"
        print self.floor_plan 
        col = self.floor_plan.getCollisions()
        count = 1
        size = len(col)

        print len(self.floor_plan.hitPoints)

        print "\n\n\n\n\n"
        for c in col:

            
            self.signalScreenUpdate(c[0].getFileName(), c[1].getScreen(), count, size)
            count+=1

        self.floor_plan.clearCollisions()


    def updateLeftPanelSize(self, *args, **kwargs):
    	self.rect1.size = self.LP.size
    	for child in self.LP.children:
    		try:
    			#pass
    			child.updateSize(self.LP.size);
    		except:
    			print "error"

    def updateRightPanelSize(self, *args, **kwargs):
        self.rect2.size = self.PRP.size
    	for child in self.PRP.children:
    		try:
    			#pass
				child.updateSize(self.PRP.size);


	    	except:
	    		print "error"




#MainScreen().run()
