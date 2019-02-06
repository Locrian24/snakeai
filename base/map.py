#!/usr/bin/env python3

from base.constants import Constants

DIM = Constants.DIMENSION
DIRS = Constants.DIRECTIONS

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

    def neighbours(self, grid_pos): #pos = grid_pos
        all_adj = self.adj_pos(grid_pos)
        neighbours = []
        for a in all_adj:
            adj_x, adj_y = a
            if (0 <= adj_x < DIM and 0 <= adj_y < DIM):
                neighbours.append((adj_x, adj_y))

        return neighbours

    def adj_pos(self, grid_pos): #pos = grid_pos
        x_pos, y_pos = grid_pos
        list = []
        for d in DIRS:
            d_x, d_y = d
            list.append((x_pos+d_x, y_pos+d_y))

        return list

    #sets grid to new empty grid
    # NOT OPTIMAL, could change so that it only clears positions used by objects
    def clear(self):
        self.grid = [[None for _ in range(DIM)] for _ in range(DIM)]
