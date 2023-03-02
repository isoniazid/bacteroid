from bacteria import *
import random

test1 = [Bacteria(color =(108, 60, 170,48), radius = random.randint(5,7)  ) for i in range(10)]
for i in range(10):
    test1.append(Bacteria(color =(198, 49, 168,60), position = (500,500), radius = random.randint(5,7)))


