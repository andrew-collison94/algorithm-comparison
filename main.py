import pandas as pd
import matplotlib.pyplot as plt
from grid import generate_grid, starting_conditions
from algorithms import myopic_algorithm, anthill_algorithm, dijkstra_algorithm
import user_variables as uv

algorithm_map = {"myopic_algorithm": myopic_algorithm,
                 "anthill_algorithm": anthill_algorithm, "dijkstra_algorithm": dijkstra_algorithm}

algorithm_name = uv.algorithm

'''
Main function to run algorithms one at a time, display the plotted route, and save the score to a dataframe
'''


def main():
    # Create an empty DataFrame to store the results
    results = pd.DataFrame(columns=['Algorithm', 'Size', 'Score'])

    playing_grid = generate_grid(uv.grid_height, uv.grid_width)
    start_index, current_value, end_index = starting_conditions(
        playing_grid, uv.grid_height, uv.grid_width)
    current_row, current_column = start_index

    print(playing_grid)
    print(f"Running {algorithm_name} algorithm...")

    final_score, total_seconds = algorithm_map[algorithm_name](
        playing_grid, current_row, current_column, start_index, current_value, end_index)

    row = pd.DataFrame({'Algorithm': [algorithm_name], 'Size': [
        uv.grid_size], 'Score': [final_score], 'Time': [total_seconds]})
    results = pd.concat([results, row], ignore_index=True)
    print(results)

    return playing_grid, final_score, total_seconds


main()
