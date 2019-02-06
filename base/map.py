#!/usr/bin/env python3

from base.constants import Constants

DIM = Constants.DIMENSION

# H = head of snake
# T = tail of snake
# F = food
# E = enemy

#not sure if this is the most efficient way (2D array vs OOP)

class Map:
    """ MAP OBJECT THAT STORES STATE OF GAME AS A GRID[Y][X] """

    def __init__(self):
        self.grid = [[None for _ in range(DIM)] for _ in range(DIM)]

    """ Is called every time the snake moves to ensure up-to-date positions
        @param objects BodyPart/Food objects passed in a list
    """
    def update(self, objects):
        self.clear()
        for o in objects:
            pos_x, pos_y = o.grid_pos()

            self.grid[pos_y][pos_x] = o.state_name

    #sets grid to new empty grid
    # NOT OPTIMAL, could change so that it only clears positions used by objects
    def clear(self):
        self.grid = [[None for _ in range(DIM)] for _ in range(DIM)]
