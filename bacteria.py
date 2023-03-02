from common import *
from random import randrange
FRICTION = 0.5
ELASTICITY = 0.9


class Bacteria:
    def __init__(self, family=0, color=(100, 100, 100, 100), position=(300, 300), id = 10):
        self._color_ = color
        self._family_ = family
        self._position_ = position
        self._id_ = id
        self.create_entity()

    def create_entity(self):
        self._mass_ = 1
        self._radius_ = 10.0
        self._impulse_ = 0, 0
        self._moment_ = pymunk.moment_for_circle(
        self._mass_, 0, self._radius_, (0, 0))
        self._body_ = pymunk.Body(self._mass_, self._moment_)
        self._body_.apply_impulse_at_local_point(self._impulse_)
        self._body_.position = self._position_

        self.shape = pymunk.Circle(self._body_, self._radius_, (0, 0))
        self.shape.elasticity = ELASTICITY
        self.shape.friction = FRICTION
        self.shape.color = self._color_
        self.shape.collision_type = self._id_
        space.add(self._body_, self.shape)

    def move(self, x_direction, y_direction, minimize=False):
        x_direction = float(x_direction)
        y_direction = float(y_direction)
        vec = self._body_.world_to_local((x_direction, y_direction))
        if minimize:
            vec *= 0.001
        self._body_.apply_impulse_at_local_point(vec)

    def wobble(self):
        x, y = randrange(0, WIDTH), randrange(0, HEIGHT)
        self.move(x, y, minimize=True)
