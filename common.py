import pymunk.pygame_util
import pygame


pymunk.pygame_util.positive_y_is_up = False

# PYGAME
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# PYMUNK VARIABLES:
space = pymunk.Space()
space.gravity = 0, 0
draw_options = pymunk.pygame_util.DrawOptions(surface)

