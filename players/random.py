#!/usr/bin/env python3

import random
from pygame.locals import * #MUST BE INCLUDED TO HANDLE USER INPUT

from base.constants import Constants

"""
    IMPORTANT:
        All players must have the following functions: (pass if not needed, but must be defined)
            - frame_update(self):       a process to be run on each frame
            - user_input(self, type):   handle user input in some way
"""

class RandomPlayer:
    def __init__(self):
        self.action = random.choice( Constants.DIRECTIONS )

    def frame_update(self):
        self.action = random.choice( Constants.DIRECTIONS )

    def user_input(self, type):
        pass
