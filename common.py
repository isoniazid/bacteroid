import pygame


"""Здесь хранятся константы и глобальные переменные"""

#CONSTS
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 100
NEWBORN_RADIUS = 5
THRESHOLD_RADIUS = 12
NEW_COLONY_SIZE = 50

# PYGAME
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
is_started = False
pygame.time.set_timer(pygame.USEREVENT, 10000)



collision_list_rects = []