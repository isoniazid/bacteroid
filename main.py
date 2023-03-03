from common import *
from bacteria import Bacteria
from core import *





pygame.init()



while True:
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    cell_division()
    handle_collisions()
    for member in test1:
        member.wobble()
        member.draw()
        
    pygame.display.flip()
    clock.tick(FPS)