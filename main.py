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
                test2.create_entity()
            if i.button == 3:
                test2.wobble()
                print(f"moved to {i.pos[0]}, {i.pos[1]}")
                

    space.step(1/FPS)
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(FPS)