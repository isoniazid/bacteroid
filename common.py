import pygame


"""Здесь хранятся константы и глобальные переменные"""

#CONSTS
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 100
MINIMAL_RADIUS = 5
MAXIMAL_RADIUS = 7
NEWBORN_RADIUS = 5
THRESHOLD_RADIUS = 15
NEW_COLONY_SIZE = 100
GROWTH_STEP = 1

# PYGAME
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
is_started = False
pygame.time.set_timer(pygame.USEREVENT, 10000)



collision_list_rects = []