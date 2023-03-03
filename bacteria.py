
from math import sqrt
from random import randint

from common import *





class Bacteria:
    def __init__(self, family=0, color=(100, 100, 100, 100), position=(300, 300), radius=5, id=0):
        """Настройка цвета, выбор колонии, позиции, размеры"""
        self._color_ = color
        self._family_ = family
        self._posx_ = position[0]
        self._posy_ = position[1]
        self._radius_ = radius
        self._id_ = id
        self._rect_ = int(sqrt(2)*self._radius_) # для оптимизации коллизий рассматриваются коллизии не кружочка, а вписанного в него квадрата
        self.create_entity()

    def create_entity(self):
        """Служебная функция класса. Создает тело, которое будет подвергаться коллизиям"""
        global collision_list_rects, collision_list_ids
        self._body_ = pygame.Rect(
            self._posx_, self._posy_, self._rect_, self._rect_)
        collision_list_rects.append(self._body_)
        #collision_list_ids.append(self._family_, )

    def draw(self):
        pygame.draw.circle(surface, self._color_,
                           self._body_.center, self._radius_)

    def move(self, x_direction, y_direction):
        global collision_list_rects
        if(x_direction+self._posx_ < WIDTH-50 and x_direction+self._posx_ > 50): # Здесь ограничения, чтобы клетки не выходили за пределы карты
            if(y_direction+self._posy_ < HEIGHT-50 and y_direction+self._posy_ > 50): # то же самое
                self._body_.x+=x_direction
                self._body_.y += y_direction
                #collision_list_rects[self._id_] = self._body_

    def check_collision(self):
        """ Проверка коллизии со всеми возможными клетками на карте """
        global collision_list_rects
        collision = self._body_.collidelist(collision_list_rects) 
        return collision

    def wobble(self):
        """беспорядочное движение"""
        x, y = randint(-1, 1), randint(-1, 1)
        self.move(x, y)

    def grow(self):
        """Я думал сделать рост раз в несколько секунд, но с ним колонии очень быстро растут и все начинает тормозить. Пока отключено"""
        self._radius_+=6