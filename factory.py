#!/usr/bin/env python3

# Simply factory that imports and returns the kind of player to be used

class PlayerFactory:
    def __init__(self):
        self.default = "human"
        self.choices = ["human", "astar", "genetic", "dnn", "super"]

    def createPlayer(self, type):
        if type == "human":
            from players.human import Human
            return ["human", Human()]
