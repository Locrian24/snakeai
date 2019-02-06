#!/usr/bin/env python3

import argparse

from factory import PlayerFactory
from game import Game

def main():
    #create factory class to manage what "player" is used
    pf = PlayerFactory()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--player", nargs="?", const=pf.default, default=pf.default, choices=pf.choices)
    args = parser.parse_args()

    [player_name, player_model] = pf.createPlayer(args.player)
    print("Current Player:", player_name)

    """
        Initialises the game screen, passing the chosen player_model that will control the game
    """
    game = Game(player_model)

if __name__ == "__main__":
    main()
