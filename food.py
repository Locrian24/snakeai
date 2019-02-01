import random

DIMENSION = 60

class Food:
    def __init__(self, unavailable=[]):
        food_x = random.randint(0, DIMENSION-1) * 10
        food_y = random.randint(0, DIMENSION-1) * 10

        while (food_x, food_y) in unavailable:
            food_x = random.randint(0, DIMENSION-1) * 10
            food_y = random.randint(0, DIMENSION-1) * 10

        self.pos = (food_x, food_y)
