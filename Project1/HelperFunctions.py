
from random import randint
class H():
    @staticmethod
    def rgb(val):
        return val/255.0

    @staticmethod
    def rc():
        return randint(0,255)

    @staticmethod
    def ranClr():
        return randint(0,255) / 255.0

    @staticmethod
    def ri(max):
        return randint(0, max)



