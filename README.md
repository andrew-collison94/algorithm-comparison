
# Maze Solver Algorithms

This project consists of three main algorithms to solve mazes:
- Myopic Algorithm
- Anthill Algorithm
- Dijkstra's Algorithm

## Setup

1. Clone the repository.
```
git clone <repository_url>
```

2. Navigate to the project directory.
```
cd <project_directory>
```

3. Install the required packages.
```
pip install -r requirements.txt
```

## Algorithms

### Myopic Algorithm

A right-biased algorithm that works well as long as the grid orientation maintains the same start and end positions it began with. It's named "myopic" because it's aware of its immediate neighbors and nothing else.

### Anthill Algorithm

Based on the behavior of ants as they search for food. It simulates a population of artificial ants exploring the playing grid, leaving pheromone trails towards advantageous locations based on cell values.

### Dijkstra's Algorithm

A graph-search algorithm that maintains a priority queue to explore cells in order of their distance from the starting point. The edge weights represent the cost to move to a particular cell, and the algorithm strives to minimize this cost.

## Running the Comparison

Execute the `comparison()` function to run a comparison between the three algorithms across different grid sizes. This will display a plot showing the performance of each algorithm as the grid size increases.
