from common import *
from bacteria import Bacteria
from core import *


pygame.init()
is_started = False
pygame.time.set_timer(pygame.USEREVENT, 10000)
font = pygame.font.SysFont('Arial', 15)

num = 0

while True:

    
    surface.fill(pygame.Color('white'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                print("The new story begins...")
                if not is_started:
                    #is_started = True
                    pass
                new_color = (randint(0, 255), randint(0, 255),
                             randint(0, 255), randint(0, 255))
                for j in range(25):
                    test1.append(Bacteria(family=current_family_number,
                                          color=new_color, position=i.pos, radius=randint(5, 7)))
                current_family_number += 1
                num = current_family_number

        if(i.type == pygame.USEREVENT):
            if is_started:
                cell_growth()

    cell_division()
    handle_collisions()
    for member in test1:
        member.wobble()
        member.draw()
    
    text = compute_results(num)
    shift = 10
    for line in text:
        surface.blit(font.render(line, True, (0, 0, 0)), (5, shift))
        shift+=15
    pygame.display.flip()
    clock.tick(FPS)
