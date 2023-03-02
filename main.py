from common import *
from bacteria import Bacteria
from core import *





pygame.init()



while True:
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    for member in test1:
        print(collision_list_rects)
        member.wobble()
        member.draw()
        
    pygame.display.flip()
    clock.tick(FPS)