#!/usr/bin/env python3

from base.constants import Constants
from collections import deque

DIM = Constants.DIMENSION
DIRS = Constants.DIRECTIONS


class BfsPlayer:
    def __init__(self):
        self.action = (1,0)

    #avoid_objects = list of tail pos and enemy snake pos
    def find_shortest_path(self, map, start, avoid_objects, end):
        if start == end:
            return [start]

        visited = set(avoid_objects)
        queue = deque([(start, [])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)

            for neighbour in map.neighbours(current):
                if neighbour == end:
                    path += [current, neighbour]
                    return self.get_dir_of(path[1], path[0])
                if neighbour in visited:
                    continue
                queue.append((neighbour, path + [current]))
                visited.add(neighbour)
        return None

    def get_dir_of(self, future_pos, pos):
        y_fpos, x_fpos = future_pos
        y_pos, x_pos = pos

        y_fpos -= y_pos
        x_fpos -= x_pos

        return (y_fpos, x_fpos)

    def frame_update(self, map, head, tail, food): #objects = [ HEAD, TAIL LIST, FOOD]
        t_pos = []
        for t in tail:
            t_pos.append(t.grid_pos())
        new_action = self.find_shortest_path(map, head.grid_pos(), t_pos, food.grid_pos())
        self.action = new_action

    def user_input(self, type):
        pass
