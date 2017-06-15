
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from filechooser import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button

import os


class LoadDialog(FloatLayout):
  pass





class FileBrowser(FloatLayout):
  
    layout = None
  
    def set_layout(self, l):
        self.layout = l

    def dismiss_popup(self):
        self.path = None
        self._popup.dismiss()

    def show_load(self):
        content = self.createLoadDialog()
        self._popup = Popup(title="Load File", content=content,
                            size_hint=(0.5, 0.5))
        self._popup.open()









    def load(self, path, filename):
        #with open(os.path.join(path, filename[0])) as stream:
           # self.text_input.text = stream.read()


        filename = str(filename)
        filename = filename[3:-2]


        for i in range (4):
            print "\n"

        print "name1: "
        print filename

        for i in range (4):
            print "\n"

        self.layout.changeFilePane(filename)
        self.dismiss_popup()



    def createLoadDialog(self):
      dialog = BoxLayout(size = self.size, pos = self.pos, orientation = "vertical")


      self.chooser =  filechooser = FileChooserIconView()

      dialog.add_widget(filechooser)
      bl = BoxLayout(size_hint_y = None, height = 40)


      cancelbtn =  Button(text = "Cancel")
      loadbtn = Button(text = "Load")

      dialog.add_widget(bl)


      cnl= lambda btn:self.dismiss_popup()
      cancelbtn.bind(on_release=cnl)

      ld= lambda btn:self.load(filechooser.path, filechooser.selection)
      loadbtn.bind(on_release=ld)

      bl.add_widget(cancelbtn)
      bl.add_widget(loadbtn)

      

      return dialog