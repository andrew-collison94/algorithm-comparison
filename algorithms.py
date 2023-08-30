import numpy as np
import user_variables as uv
import time
from grid import display_grid
import heapq
import random

INVALID_COORDINATE = (-1, -1)


def myopic_algorithm(playing_grid, current_row, current_column, current_index, current_value, end_index, display=True):
    '''
    The baseline algorithm is right-biased and works well 
    as long as the grid orientation maintains the same start and end 
    posititions that it began with. It is named myopic because it is aware
    of it's immediate neighbors and nothing else.
    '''
    grid_height, grid_width = playing_grid.shape
    # Create a list to store the path
    path = [(current_row, current_column)]

    start_time = time.process_time()
    while current_index != end_index:

        # Initialise the dictionary that contains adjacent values and coordinates
        adjacent_dict = {}

        # Check right neighbor
        if current_column < grid_width - 1:
            right_check = current_column + 1
            right_value = playing_grid[current_row, right_check]
            adjacent_dict[current_row, right_check] = right_value
        else:
            adjacent_dict[INVALID_COORDINATE] = uv.highest_value + 1

        # Check down neighbor
        if current_row < grid_height - 1:
            down_check = current_row + 1
            down_value = playing_grid[down_check, current_column]
            adjacent_dict[down_check, current_column] = down_value
        else:
            adjacent_dict[INVALID_COORDINATE] = uv.highest_value + 1

        # Check left neighbor
        if current_column > 0:
            left_check = current_column - 1
            left_value = playing_grid[current_row, left_check]
            adjacent_dict[current_row, left_check] = left_value
        else:
            adjacent_dict[INVALID_COORDINATE] = uv.highest_value + 1

        # Identifies the location of the lowest value in the dictionary
        minimum_value = min(adjacent_dict.values())
        # Adds the new value to existing value for the updated current_value
        current_value += minimum_value
        # Iterates through the dictionary to retrieve the coordinates associated with the minimum value
        next = [key for key in adjacent_dict if adjacent_dict[key] == minimum_value]

        # Reassigns the next step as the updated current index
        current_index = next[0]

        # Add the current cell to the final route
        path.append(current_index)

        # Changes the previous value to an amount the program cannot select to prevent backtracking
        playing_grid[current_row, current_column] = uv.highest_value + 1

        # Reassigns the next steps as the updated coordinate elements
        current_row, current_column = current_index

    if display:
        display_grid(playing_grid, (current_row, current_column), path=path)
    final_score = current_value
    end_time = time.process_time()
    print("Finished! We've reached the goal with a total score of " + str(current_value))
    total_seconds = end_time - start_time
    print(f"Game runtime from start to finish: {total_seconds:.3f} seconds")
    return final_score, total_seconds


def anthill_algorithm(playing_grid, current_row, current_column, current_index, current_value, end_index, display=True):
    '''
    The anthill algorithm is based on the behavior of ants as they search for food. 
    It simulates a population of artificial ants exploring the playing grid, leaving pheromone 
    trails towards advantageous locations based on cell values. The pheromone trails suggest good 
    paths as more ants travel there, while poor ones are left to evaporate. The final solution is 
    chosen from the best path found by the ants, and display_grid in grid.py 
    plots the pheromone trails and the final route.
    '''
    grid_height, grid_width = playing_grid.shape
    # Create a pheromone trail grid to track the pheromone levels on each edge
    pheromone_trails = np.ones_like(playing_grid, dtype=np.float64)

    start_time = time.process_time()

    # Initialize the list to store the paths of all ants
    all_paths = []

    for _ in range(uv.num_ants):
        # Reset the ant's position to the current position
        ant_row = current_row
        ant_column = current_column

        # Reset the ant's score
        ant_score = 0

        # Create a list to store the path of the ant
        path = []

        while (ant_row, ant_column) != end_index:
            # Calculate the scores for each adjacent cell based on pheromone trails and values
            scores = []
            adjacent_cells = []

            # Explore all adjacent cells
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_row = ant_row + row_offset
                neighbor_column = ant_column + col_offset

                # Check if the neighbor is within the grid boundaries
                if (0 <= neighbor_row < grid_height and 0 <= neighbor_column < grid_width):
                    adjacent_cells.append((neighbor_row, neighbor_column))

            for cell in adjacent_cells:
                cell_row, cell_column = cell
                pheromone_level = pheromone_trails[cell_row, cell_column]
                cell_value = playing_grid[cell_row, cell_column]
                score = pheromone_level / (1 + cell_value)
                scores.append(score)

            # Calculate the sum of scores
            total_score = sum(scores)

            # Calculate the probabilities
            probabilities = [score / total_score for score in scores]

            next_cell = random.choices(adjacent_cells, probabilities)[0]

            next_row, next_column = next_cell

            # Update the ant's position and score
            ant_row = next_row
            ant_column = next_column
            ant_score += playing_grid[ant_row, ant_column]

            # Add the current cell to the path
            path.append((ant_row, ant_column))

        # Add the ant's path to the list of all paths
        all_paths.append((ant_score, path))

    # Sort the paths by score (lower score is better)
    all_paths.sort(key=lambda x: x[0])

    # Choose the best path (the first one in the sorted list)
    best_path_score, best_path = all_paths[0]

    # Update the pheromone trail on the edges in the best path
    for cell in best_path:
        cell_row, cell_column = cell
        pheromone_trails[cell_row, cell_column] += uv.pheromone_deposit

    # Evaporate the pheromone trails
    pheromone_trails *= (1 - uv.evaporation_rate)

    # Normalize the pheromone trails for better visualization
    pheromone_trails = (pheromone_trails - np.min(pheromone_trails)) / \
        (np.max(pheromone_trails) - np.min(pheromone_trails))

    # Display the pheromone trails alone first
    print("Pheromone Trails:")
    if display:
        display_grid(playing_grid, (current_row, current_column),
                     pheromones=pheromone_trails)

    # Display the final state with the route
    print("Final Route:")
    if display:
        display_grid(playing_grid, (current_row, current_column), path=best_path)

    final_score = best_path_score
    end_time = time.process_time()
    print("Finished! We've reached the goal with a total score of " + str(final_score))
    total_seconds = end_time - start_time
    print(f"Game runtime from start to finish: {total_seconds:.3f} seconds")
    return final_score, total_seconds


def dijkstra_algorithm(playing_grid, current_row, current_column, current_index, current_value, end_index, display=True):
    '''
    Dijkstra's algorithm is a graph-search algorithm that maintains a priority queue to explore 
    cells in order of their distance from the starting point. It selects the unvisited cells with 
    the smallest distance, explores its neighbors, and updates their distances based on the current 
    cell's distance and the edge weight (value of the cell). 
    The edge weights represent the cost to move to a particular cell, 
    and the algorithm strives to minimize this cost.
    '''
    grid_height, grid_width = playing_grid.shape
    start_time = time.process_time()

    # Initialise the list that contains a priority queue to track the minimum score
    priority_queue = []
    # Initialise the dictionary that stores the minimum score for each node
    score = {}
    # Initialise a dictionary to store the parent of each node
    parent = {}
    # Initialise a set to keep track of visited nodes
    visited = set()

    # Initialize the score of all nodes to infinity except the starting node
    for row in range(grid_height):
        for column in range(grid_width):
            if (row, column) == current_index:
                score[(row, column)] = current_value
            else:
                score[(row, column)] = float('inf')

    # Add the starting node to the priority queue
    heapq.heappush(priority_queue, (current_value, current_index))

    while priority_queue:
        # Get the node with the minimum score from the priority queue
        current_value, current_node = heapq.heappop(priority_queue)
        current_row, current_column = current_node

        # Mark the current node as visited
        visited.add(current_node)

        # Check if the current node is the goal
        if current_node == end_index:
            break

        # Explore all adjacent nodes
        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row = current_row + row_offset
            neighbor_column = current_column + col_offset
            neighbor_node = (neighbor_row, neighbor_column)

            # Check if the neighbor is within the grid boundaries and has not been visited
            if (0 <= neighbor_row < grid_height and 0 <= neighbor_column < grid_width and neighbor_node not in visited):
                neighbor_value = playing_grid[neighbor_row, neighbor_column]
                new_score = current_value + neighbor_value

                # Check if the new score is lower than the current score
                if new_score < score[neighbor_node]:
                    score[neighbor_node] = new_score
                    parent[neighbor_node] = current_node
                    heapq.heappush(priority_queue, (new_score, neighbor_node))

    if end_index in visited:
        # Reconstruct the path
        path = []
        node = end_index
        while node != current_index:
            path.append(node)
            node = parent[node]
        path.append(current_index)
        path.reverse()

        # Display the final state with the route
        if display:
            display_grid(playing_grid, (current_row, current_column), path=path)

        final_score = current_value
        end_time = time.process_time()
        print("Finished! We've reached the goal with a total score of " + str(current_value))
        total_seconds = end_time - start_time
        print(f"Game runtime from start to finish: {total_seconds:.3f} seconds")
        return final_score, total_seconds
    else:
        print("No valid path from the starting position to the goal!")
        return None, None
