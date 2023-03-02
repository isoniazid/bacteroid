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
        self._mass_ = 1
        self._radius_ = 10.0
        self._impulse_ = 0, 0
        self._moment_ = pymunk.moment_for_circle(self._mass_,0,self._radius_,(0,0))
        self._body_ = pymunk.Body(self._mass_,self._moment_)
        self._body_.apply_impulse_at_local_point(self._impulse_)
        self._body_.position = self._position_


        shape = pymunk.Circle(self._body_, self._radius_, (0,0))
        shape.elasticity = ELASTICITY
        shape.friction = FRICTION
        shape.color = self._color_
        space.add(self._body_, shape)
        
    def move(self, x_direction, y_direction):
        x_direction = float(x_direction)
        y_direction = float(y_direction)
        vec = self._body_.world_to_local((x_direction,y_direction))
        self._body_.apply_impulse_at_local_point(vec)

    def wobble(self):
         x, y = randrange(0,WIDTH/5), randrange(0,HEIGHT/5)
         self.move(x,y)


