
# Puzzle Solving Algorithms

This puzzle-solving project compares the usefulness of three seperate algorithms as they navigate their way across a grid. Each cell in the grid is randomly populated with a numeric value that represents a time-cost. The algorithm that can reach the end point with the lowest accumulated score is considered the most effictive puzzle solver:
- Myopic Algorithm
- Anthill Algorithm
- Dijkstra's Algorithm

## Setup

1. Clone the repository.

git clone https://github.com/andrew-collison94/algorithm-comparison.git

2. Install the required packages.

pip install -r requirements.txt

## Algorithms

### Myopic Algorithm

A right-biased algorithm that works well as long as the grid orientation maintains the same start and end positions it began with. It's named "myopic" because it makes decisions based on nothing but its immediate neighbors.

### Anthill Algorithm

Based on the behavior of ants as they search for food. It simulates a population of artificial ants exploring the playing grid, leaving pheromone trails towards advantageous locations based on cell values.

### Dijkstra's Algorithm

A graph-search algorithm that maintains a priority queue to explore cells in order of their distance from the starting point. The edge weights represent the cost to move to a particular cell, and the algorithm strives to minimize this cost.

## Running the Program

Main:
Execute the 'main()' function to run the specific algorithm set in user_variables.py

Comparison:
Execute the 'comparison() function to run a comparison between the three algorithms across different grid sizes. This will display a plot showing the performance of each algorithm as the grid size increases.
