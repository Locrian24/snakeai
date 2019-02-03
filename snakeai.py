#!/usr/bin/env python3
import argparse

from factory import PlayerFactory
from game import Game

def main():
    pf = PlayerFactory()

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--player", nargs="?", const=pf.default, default=pf.default, choices=pf.choices)

    args = parser.parse_args()

    game = Game(args.player)



if __name__ == "__main__":
    main()
