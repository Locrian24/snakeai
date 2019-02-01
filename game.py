import sys
import pygame
import random
from snake import Snake

DIMENSION = 60
DIRECTIONS = [ (0,-1), (1,0), (0,1), (-1, 0) ]

class Game:

    pygame.init()

    screen_objects = []

    def __init__(self, fps):
        self.fps = fps
        self.pixel_size = 10
        self.screen_size = DIMENSION * self.pixel_size

        self.SCREEN = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption("SNAKE LAB")

        self.snake = Snake()

        while self.snake.alive:
            new_direction = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    new_direction = self.return_user_inputs(event)

            if new_direction:
                self.snake.set_direction(new_direction)

            pygame.time.Clock().tick(fps)
            self.SCREEN.fill((255,255,255))

            #UPDATE DIRECTION RANDOMLY
            # new_direction = random.choice(DIRECTIONS)
            # self.snake.set_direction(new_direction)

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
            rect = pygame.Rect(p, (self.pixel_size, self.pixel_size))
            pygame.draw.rect(self.SCREEN, color, rect)

            color = (0,0,0)


        # rect = pygame.Rect(s.head.pos, (self.pixel_size, self.pixel_size))
        # pygame.draw.rect(self.SCREEN, (0,0,0), rect)
        # for t in s.tail:
        #     rect = pygame.Rect(t.pos, (self.pixel_size, self.pixel_size))
        #     pygame.draw.rect(self.SCREEN, (0,0,0), rect)
        #
        # rect = pygame.rect.Rect(s.food.pos, (self.pixel_size, self.pixel_size))
        # pygame.draw.rect(self.SCREEN, (0,255,0), rect)

if __name__ == "__main__":
    game = Game(30)
