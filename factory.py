#!/usr/bin/env python3

# Simply factory that imports and returns the kind of player to be used

"""
    IMPORTANT:
        If you are implementing a new player model:
        - Add it to the list of choices,
        - Make an "elif" statement that checks the name called
            + Import the player model class
            + return ["<name>", <model_class_name>()]

    NOTES:
        A player model should return a direction for each call,
            this depends on the model but any pathsolving alg
            should return a next_direction each frame
"""

class PlayerFactory:
    def __init__(self):
        self.default = "human"
        self.choices = ["human", "random"] #add to when new model is being implemented

    #type of player_model inputted is then imported and the class is returned
    def createPlayer(self, type):
        if type == "human":
            from players.human import HumanPlayer
            return ["human", HumanPlayer()]
        elif type == "random":
            from players.random import RandomPlayer
            return ["random", RandomPlayer()]
