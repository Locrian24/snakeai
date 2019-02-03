#!/usr/bin/env python3

import sys
import pygame
import random
from snake import Snake
from constants import Constants

DIMENSION = Constants.DIMENSION
SCREEN_SIZE = Constants.SCREEN_SIZE
PIXEL_SIZE = Constants.PIXEL_SIZE
DIRECTIONS = Constants.DIRECTIONS

class Game:

    pygame.init()

    def __init__(self, player):

        self.SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

        self.player = player
        self.snake = Snake()

        while self.snake.alive:
            new_direction = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    player.user_input(event)

            new_direction = self.player.move()

            if new_direction:
                self.snake.set_direction(new_direction)

            pygame.time.Clock().tick(Constants.FPS)
            self.SCREEN.fill((255,255,255))
            pygame.display.set_caption("SNAKE SCORE: {}".format(self.snake.len))


            self.snake.move()

            self.draw_objects(self.snake)
            pygame.display.update()
            self.player.reset()

        pygame.quit()
        sys.exit()

    def draw_objects(self, s):
        objects_pos = s.give_positions()
        color = (0, 255, 0)

        for p in objects_pos:
            rect = pygame.Rect(p, (PIXEL_SIZE, PIXEL_SIZE))
            pygame.draw.rect(self.SCREEN, color, rect)

            color = (0,0,0)
