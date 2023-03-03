import pygame


"""Здесь хранятся константы и глобальные переменные"""

#CONSTS
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 100

# PYGAME
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


collision_list_rects = []