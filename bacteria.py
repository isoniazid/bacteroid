from common import *
from random import randrange
FRICTION = 0.5
ELASTICITY = 0.5


class Bacteria:
    def __init__(self, family = 0, color = (100,100,100,100), position = (300,300)):
        self._color_ = color
        self._family_ = family
        self._position_ = position

    def create_entity(self):
        pass
        
    def move(self, x_direction, y_direction):
        pass

    def wobble(self):
         x, y = randrange(0,WIDTH/5), randrange(0,HEIGHT/5)
         self.move(x,y)


