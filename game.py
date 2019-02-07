#!/usr/bin/env python3

import sys
import pygame
import random

from base.snake import Snake
from base.constants import Constants

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #KEY PRESS -- human model = input for direction
                    player.user_input(event)

            #THIS IS WHERE THE NEW DIRECTION IS SET FROM THE PLAYER MODEL
            self.player.frame_update(self.snake.map, self.snake.head, self.snake.tail, self.snake.food)
            direction = self.player.action
            if direction:
                self.snake.set_direction(direction)
            else:
                print("NO PATH TO FOOD")
                self.snake.alive = False

            pygame.time.Clock().tick(Constants.FPS)
            self.SCREEN.fill((255,255,255))
            pygame.display.set_caption("SNAKE SCORE: {}".format(self.snake.len))

            #For all non-human player models, new_direction should be set every move
            #That is, player.action is set
            self.snake.move()

            self.draw_objects(self.snake)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def draw_objects(self, s):
        h_pos = s.head.pos
        objects_pos = s.give_positions()
        color = (0, 255, 0)
        red = (255, 0, 0)

        for p in objects_pos:
            rect = pygame.Rect(p, (PIXEL_SIZE, PIXEL_SIZE))
            if p is not h_pos:
                pygame.draw.rect(self.SCREEN, color, rect)
            else:
                pygame.draw.rect(self.SCREEN, red, rect)

            color = (0, 0, 0)
