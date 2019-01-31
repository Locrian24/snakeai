import sys
import pygame

class Game:

    pygame.init()

    screen_objects = []
    

    def __init__(self, fps, pixel_size, screen_size):
        self.fps = fps
        self.pixel_size = pixel_size
        self.SCREEN = pygame.display.set_mode((screen_size, screen_size))
        self.SURF = pygame.Surface(self.SCREEN.get_size())
        self.dim_pixels = screen_size / pixel_size
