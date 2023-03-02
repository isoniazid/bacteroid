from common import *
from bacteria import *


handler = space.add_collision_handler(1,2)

def handle_collision(self, arbiter, space, data):
    print('wtf')
    



def simulation():
    pygame.init()


    first_family = [Bacteria( color = (166,0,255,100), id = 10+i) for i in range(30)]
    second_family = [Bacteria(family = 1, color = (255,25,139,100), id = 100+i, position = (900, 900)) for i in range(30)]
    while True:
        surface.fill(pygame.Color('white'))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    pass
                if i.button == 3:
                    first_family[0].wobble()
                    print(f"moved to {i.pos[0]}, {i.pos[1]}")
                    
        for member in first_family:
            member.wobble()
        
        for member in second_family:
            member.wobble()
        
        handler.begin = handle_collision()

        space.step(1/FPS)
        space.debug_draw(draw_options)
        pygame.display.flip()
        clock.tick(FPS)
