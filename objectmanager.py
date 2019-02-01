from snake import Snake
import snake
from food import Food

class ObjectManager:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(snake.DIMENSION)

    def get_all_positions(self): #create this so that game.py doesn't have to find pos
        pass

    def death(self):
        pass
