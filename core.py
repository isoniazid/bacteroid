from bacteria import *
import random


current_family_number = 0

test1 = []
#test1 = [Bacteria(color=(108, 60, 170, 48), family = 0,
#                  radius=random.randint(5, 7) ) for i in range(10)]
#for i in range(10):
#    test1.append(Bacteria(color=(198, 49, 168, 60), family = 1, position=(
#        350, 350), radius=random.randint(5, 7)))
#for i in range(10):
#    test1.append(Bacteria(color=(182, 21, 21, 80), family = 2, position=(
#        400, 400), radius=random.randint(5, 7)))

def handle_collisions():
    #global test1, collision_list_rects
    i=0
    while(i < len(test1)):
        collision = test1[i].check_collision()
        if(collision != -1):
            #print(collision)
            if test1[i]._family_ != test1[collision]._family_:
                if test1[i]._radius_ > test1[collision]._radius_:
                    test1[i]._radius_+=test1[collision]._radius_
                    test1.pop(collision)
                    collision_list_rects.pop(collision)
                    i=0
                if test1[i]._radius_ < test1[collision]._radius_:
                    test1[collision]._radius_+=test1[i]._radius_
                    test1.pop(i)
                    collision_list_rects.pop(i)
                    i=0
        i+=1
                #if test1


def cell_division():
    for member in test1:
        if member._radius_>=11:
            newborn_color = member._color_
            newborn_family = member._family_
            newborn_position = (member._body_.x,member._body_.y)
            newborn_radius = 5
            member._radius_-=5
            test1.append(Bacteria(color = newborn_color, family=newborn_family, position=newborn_position, radius=newborn_radius))
            #print("SEX!")


def cell_growth():
    for member in test1:
        member.grow()

def compute_results(asd):
    results = []
    counter = 0
    for i in range(asd):
        for member in test1:
            if(i == member._family_):
                counter += 1
        results.append(f'Colony {str(i+1)}: {str(counter)}')
        counter = 0
    return results