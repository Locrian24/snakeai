#!/usr/bin/env python3

import random

from base.food import Food
from base.map import Map
from base.constants import Constants

#CONSTANTS
VELOCITY = Constants.VELOCITY
DIMENSION = Constants.DIMENSION
SCREEN_SIZE = Constants.SCREEN_SIZE
PIXEL_SIZE = Constants.PIXEL_SIZE

class BodyPart:
    """ Object for each "bodypart" of the snake """

    def __init__(self, position, state_name, ancestor=None):
        self.pos = position
        self.ancestor = ancestor
        self.state_name = state_name

    #getter for ancestor
    def get_ancestor(self):
        return self.ancestor

    #setter for position
    def update_pos(self, new_pos):
        self.pos = new_pos

    #returns position of BP in the grid (rather than pixel location)
    def grid_pos(self):
        return ( int(self.pos[0]/PIXEL_SIZE), int(self.pos[1]/PIXEL_SIZE) )

    #returns the future move that will be made next frame
    def future_path(self, direction):
        dir_x, dir_y = direction
        pos_x, pos_y = self.pos

        pos_x += VELOCITY * dir_x
        pos_y += VELOCITY * dir_y

        return pos_x, pos_y

    #moves BP to position of next move
    def _move(self, direction):
        self.pos = ( self.future_path(direction) )

########################################

class Snake:
    """ SNAKE OBJECT """

    def __init__(self):
        #initial position - SHOULD CHANE TO RANDOOM
        self.x = 100
        self.y = 100

        #init of snake itself
        self.head = BodyPart((100, 100), 'H')
        self.len = 1
        self.tail = []

        #init of snake attributes
        self.lifetime = 1
        self.alive = True
        self.current_direction = (1, 0)

        #init of snake's objects
        #important the snake has it's own map and food for when there are multiple
        self.food = Food()
        self.map = Map()

        #init of screen grid - THIS IS WHAT IS PASSED TO THE PLAYER_MODEL
        self.objects = [self.head, self.food]
        self.map.update(self.objects)

    def move(self):
        """ MOVES SNAKE IN CURRENT DIRECTION AND CHECKS EVENTS """

        future_x, future_y = self.head.future_path(self.current_direction)

        self.alive = not self.is_dead(future_x, future_y) #CHECK IF DEAD IF IT MOVES [SO PYTHONIC!!!]

        if self.alive:
            #Head has same pos as food (eat the food)
            if future_x == self.food.pos[0] and future_y == self.food.pos[1]:
                self.eat()

            #update from back of snake to front
            for t in reversed(self.tail):
                if t.ancestor:
                    t.pos = t.ancestor.pos

            #what actually determines the movement direction of the snake
            self.head._move(self.current_direction)

            #update grid rep
            self.map.update(self.objects)

    def eat(self):
        tail_pos = [t.pos for t in self.tail]
        self.food = Food(tail_pos)

        #add head duplicate to tail list
        temp = BodyPart(self.head.pos, 'T', self.head)
        if self.tail:
            self.tail[0].ancestor = temp
            self.tail.insert(0, temp)
        else:
            self.tail = [temp]

        #update attributes due to tail length increase
        self.len += 1
        self.objects = self.list_objects()

    #returns a list of all screen objects
    def list_objects(self):
         list = [self.head]
         list.extend(self.tail)
         list.append(self.food)

         return list

    #checks if head hit wall or hit a tail BP
    def is_dead(self, future_x, future_y):
        tail_pos = [t.pos for t in self.tail]
        if (future_x, future_y) in tail_pos:
            return True

        if not (0 <= future_x < SCREEN_SIZE and 0 <= future_y < SCREEN_SIZE):
            return True

        return False

    #returns positions of all screen objects
    def give_positions(self):
        pos_list = [ self.food.pos ] #FOOD POSITION ALWAYS AT FRONT OF LIST

        pos_list.append(self.head.pos)
        for t in self.tail:
            pos_list.append(t.pos)

        return pos_list

    #setter for current_direction
    def set_direction(self, direction):
        self.current_direction = direction
