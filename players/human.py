#!/usr/bin/env python3

from pygame.locals import * #MUST BE INCLUDED TO HANDLE USER INPUT
import random

from base.constants import Constants

"""
    IMPORTANT:
        All players must have the following functions: (pass if not needed, but must be defined)
            - frame_update(self):       a process to be run on each frame
            - user_input(self, type):   handle user input in some way
"""


class HumanPlayer:
    def __init__(self):
        self.action = random.choice( Constants.DIRECTIONS )

    #For this player, user input IS how the new_direction is determined
    def user_input(self, event):
        if event.key == K_UP:
            self.action = (0,-1)
        elif event.key == K_RIGHT:
            self.action = (1,0)
        elif event.key == K_DOWN:
            self.action = (0,1)
        elif event.key == K_LEFT:
            self.action = (-1,0)

    def frame_update(self):
        pass
