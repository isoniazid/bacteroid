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
        if i.type == pygame.MOUSEBUTTONDOWN: #Создать новую колонию
            if i.button == 1:
                print("The new story begins...")
                if not is_started:
                    is_started = True
                    pass
                new_color = (randint(0, 255), randint(0, 255),
                             randint(0, 255), randint(0, 255))
                for j in range(NEW_COLONY_SIZE):
                    test1.append(Bacteria(family=current_family_number,
                                          color=new_color, position=i.pos, radius=randint(MINIMAL_RADIUS, MAXIMAL_RADIUS)))
                current_family_number += 1
                num = current_family_number

        if(i.type == pygame.USEREVENT):
            if is_started:
                cell_death()
                cell_growth()

    cell_division()
    handle_collisions()

    for member in test1:
        member.wobble()
        member.draw()
    text = []
    score_data = compute_results(num)
    #print(score_data)
    for line in score_data:
        text.append(font.render(line[0], True, line[1]))
        
    shift = 10
    for line in text:
        surface.blit(line,(5, shift))
        shift+=15
        
    pygame.display.flip()
    clock.tick(FPS)
