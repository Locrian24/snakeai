#!/usr/bin/env python3

# Simply factory that imports and returns the kind of player to be used

class PlayerFactory:
    def __init__(self):
        self.default = "human"
        self.choices = ["human", "bfs", "dfs", "genetic", "nn", "super"]

    def createPlayer(self, type):
        if type == "bfs":
            #import bfs
            return ["bfs"]#, bfs.play]
        else:
            #import human
            return ["human"]#, human.play]
