import pymunk.pygame_util
import pygame


pymunk.pygame_util.positive_y_is_up = False

#CONSTS
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60
PL_ELASTICITY = 0.5
PL_FRICTION = 0.99

# PYGAME
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# PYMUNK VARIABLES:
space = pymunk.Space()
space.gravity = 0, 0
draw_options = pymunk.pygame_util.DrawOptions(surface)

# PLATFORM
platform_top = pymunk.Segment(space.static_body, (1,1), (WIDTH,1), 26)
space.add(platform_top)
platform_top.elasticity = PL_ELASTICITY
platform_top.friction = PL_FRICTION 

platform_left = pymunk.Segment(space.static_body, (1,1), (1,HEIGHT), 26)
space.add(platform_left)
platform_left.elasticity = PL_ELASTICITY
platform_left.friction = PL_FRICTION 

platform_right = pymunk.Segment(space.static_body, (WIDTH,1), (WIDTH,HEIGHT), 26)
space.add(platform_right)
platform_right.elasticity = PL_ELASTICITY
platform_right.friction = PL_FRICTION 

platform_bottom = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH,HEIGHT), 26)
space.add(platform_bottom)
platform_bottom.elasticity = PL_ELASTICITY
platform_bottom.friction = PL_FRICTION 