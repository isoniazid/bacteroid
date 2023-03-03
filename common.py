import pygame


"""Здесь хранятся константы и глобальные переменные"""

#CONSTS
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 75
MINIMAL_RADIUS = 3 #Минимально возможный радиус для рожденных клеток и клеток в новых колониях
MAXIMAL_RADIUS = 10 #Макимальный радиус клеток в новых колониях
NEWBORN_RADIUS = 5 #Максимально возможный радиус для новорожденной клетки (Должен быть меньше порога)
THRESHOLD_RADIUS = 9 #Порог размера для клетки, если болььше - она делится
NEW_COLONY_SIZE = 10 #Размер новой колонии
DEATH_THRESHOLD = 4 #Порог, при котором клетка умирает
GROWTH_STEP = 1 #Шаг роста для клетки

# PYGAME
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
is_started = False
pygame.time.set_timer(pygame.USEREVENT, 10000)



collision_list_rects = []