#!/usr/bin/env python3
#Class that keeps track of game screen in a 2D array.
#Only initialised for A* and Hamilton
from constants import Constants

class GameSpace:

    snake   = '$'
    food    = '#'
    empty   = ' '

    def __init__(self):
        self.x = Constants.DIMENSION
        self.y = Constants.DIMENSION

        self.game_space = []
