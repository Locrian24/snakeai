#!/usr/bin/env python3

class Constants:

    DIMENSION = 20 # Number of cells in grid ( > 10 )
    PIXEL_SIZE = 10 # How big each grid cell is on screen
    SCREEN_SIZE = DIMENSION * PIXEL_SIZE
    VELOCITY = PIXEL_SIZE # How fast the snake moves per frame
    FPS = 30
    DIRECTIONS = [ (0,-1), (1,0), (0,1), (-1, 0) ] #[UP, RIGHT, DOWN, LEFT]
