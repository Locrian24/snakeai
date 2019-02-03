#!/usr/bin/env python3
from pygame.locals import *

class Human:
    def __init__(self):
        self.action = None

    def move(self):
        return self.action

    def user_input(self, event):
        if event.key == K_UP:
            self.action = (0,-1)
        elif event.key == K_RIGHT:
            self.action = (1,0)
        elif event.key == K_DOWN:
            self.action = (0,1)
        elif event.key == K_LEFT:
            self.action = (-1,0)

    def reset(self):
        self.action = None
