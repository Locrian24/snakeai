#!/usr/bin/env python3

import sys
import pygame
import random
from snake import Snake
from constants import Constants

DIMENSION = Constants.DIMENSION
SCREEN_SIZE = Constants.SCREEN_SIZE
PIXEL_SIZE = Constants.PIXEL_SIZE

DIRECTIONS = [ (0,-1), (1,0), (0,1), (-1, 0) ]

class Game:

    pygame.init()

    screen_objects = []

    def __init__(self, player_model=None):

        self.SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("SNAKE LAB")

        self.snake = Snake()

        while self.snake.alive:
            new_direction = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if player_model == "human":
                    if event.type == pygame.KEYDOWN:
                        new_direction = self.return_user_inputs(event)

            if new_direction:
                self.snake.set_direction(new_direction)

            pygame.time.Clock().tick(Constants.FPS)
            self.SCREEN.fill((255,255,255))

            self.snake.move()

            self.draw_objects(self.snake)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def return_user_inputs(self, event):
        if event.key == pygame.K_UP:
            return DIRECTIONS[0]
        elif event.key == pygame.K_RIGHT:
            return DIRECTIONS[1]
        elif event.key == pygame.K_DOWN:
            return DIRECTIONS[2]
        elif event.key == pygame.K_LEFT:
            return DIRECTIONS[3]
        else:
            return None

    def draw_objects(self, s):
        objects_pos = s.give_positions()
        color = (0, 255, 0)

        for p in objects_pos:
            rect = pygame.Rect(p, (PIXEL_SIZE, PIXEL_SIZE))
            pygame.draw.rect(self.SCREEN, color, rect)

            color = (0,0,0)

# if __name__ == "__main__":
#     game = Game()
