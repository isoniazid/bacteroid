from common import *
from bacteria import Bacteria




pygame.init()


test1 = Bacteria()
test2 = Bacteria(color = (150,150,150,150))
while True:
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pass
            if i.button == 3:
                print(f"moved to {i.pos[0]}, {i.pos[1]}")
                

    pygame.display.flip()
    clock.tick(FPS)