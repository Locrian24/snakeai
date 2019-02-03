#!/usr/bin/env python3

import random
from food import Food
from constants import Constants

VELOCITY = Constants.VELOCITY
DIMENSION = Constants.DIMENSION
SCREEN_SIZE = Constants.SCREEN_SIZE

class BodyPart:
    def __init__(self, position, ancestor=None):
        self.pos = position
        self.ancestor = ancestor

    def get_ancestor(self):
        return self.ancestor

    def update_pos(self, new_pos):
        self.pos = new_pos

    def future_path(self, direction):
        dir_x, dir_y = direction
        pos_x, pos_y = self.pos

        pos_x += VELOCITY * dir_x
        pos_y += VELOCITY * dir_y

        return pos_x, pos_y

    def _move(self, direction):
        dir_x, dir_y = direction
        pos_x, pos_y = self.pos

        pos_x += VELOCITY * dir_x
        pos_y += VELOCITY * dir_y

        self.pos = (pos_x, pos_y)

class Snake:
    def __init__(self):
        self.x = 100
        self.y = 100

        self.head = BodyPart((100, 100))
        self.len = 1

        self.tail = []
        self.lifetime = 1
        self.alive = True
        self.current_direction = (0, 1)

        self.food = Food()

        #loading tail with 3 -- start len at 4
        temp = self.head
        for i in range(0,3):
            tail_x, tail_y = temp.pos
            tail_x -= 10

            new = BodyPart((tail_x, tail_y), temp)
            self.tail.append(new)

            temp = new

        self.len += 3

    def move(self):
        future_x, future_y = self.head.future_path(self.current_direction)

        self.alive = not self.is_dead(future_x, future_y) #CHECK IF DEAD IF IT MOVES [SO PYTHONIC!!!]

        if future_x == self.food.pos[0] and future_y == self.food.pos[1]:
            self.eat()

        temp = self.tail[self.len - 3]
        for t in reversed(self.tail):
            if t.ancestor:
                t.pos = t.ancestor.pos

        self.head._move(self.current_direction)

    def eat(self): #MAKE AN EVENT HANDLER?? DEATH AND EAT
        tail_pos = [t.pos for t in self.tail]
        self.food = Food(tail_pos)

        #add head duplicate to tail list
        temp = BodyPart(self.head.pos, self.head)
        self.tail[0].ancestor = temp
        self.tail.insert(0, temp)


    def set_direction(self, direction):
        self.current_direction = direction

    def is_dead(self, future_x, future_y):
        tail_pos = [t.pos for t in self.tail]
        if (future_x, future_y) in tail_pos:
            return True

        if not (0 <= future_x < SCREEN_SIZE and 0 <= future_y < SCREEN_SIZE):
            print(self.head.pos[0], ":", self.head.pos[1])
            return True

        return False

    def give_positions(self):
        pos_list = [ self.food.pos ] #FOOD POSITION ALWAYS AT FRONT OF LIST

        pos_list.append(self.head.pos)
        for t in self.tail:
            pos_list.append(t.pos)

        return pos_list
