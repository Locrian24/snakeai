#!/usr/bin/env python3

import random

from base.constants import Constants

DIMENSION = Constants.DIMENSION
PIXEL_SIZE = Constants.PIXEL_SIZE

class Food:
    """ FOOD OBJECT """

    def __init__(self, unavailable=[]):
        self.state_name = 'F'
        food_x = random.randint(0, DIMENSION-1) * 10
        food_y = random.randint(0, DIMENSION-1) * 10

        #if new food is in the tail, create another until it isn't
        while (food_x, food_y) in unavailable:
            food_x = random.randint(0, DIMENSION-1) * 10
            food_y = random.randint(0, DIMENSION-1) * 10

        self.pos = (food_x, food_y)
        print("F:", self.pos)

    #returns position in grid
    def grid_pos(self):
        return ( int(self.pos[0]/PIXEL_SIZE), int(self.pos[1]/PIXEL_SIZE) )
