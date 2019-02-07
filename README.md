# snakeai
Side project for learning machine learning through the game Snake, written in Python 3.7.5, implementing Pygame (1.9.4)
Note: Python 3.7 and Pygame will be needed to run the snake program

To run in terminal:
```
python3 main.py -p <player_model>
```

Base game is controlled by various "players":
  - HumanPlayer (player_model = human):    human controlled
  - RandomPlayer (player_model = random):  randomly moves
  - BfsPlayer (player_model = bfs): implements BFS pathfinding to move along the shortest path to the food calculated each frame. Dies when the head is cut off from the food by its tail

  (Not yet implemented: )
  - Genetic Algorithm
  - DNN (Deep Neural Network)
  - Hamiltonian cycling
  - The SuperPlayer: a combination of all AI players based on Coding Bullet's SnakeFusion (linked at bottom)


Coding Bullet's SnakeFusion:
  <i>https://github.com/Code-Bullet/SnakeFusion</i>
