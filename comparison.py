import matplotlib.pyplot as plt
from grid import generate_grid, starting_conditions
from algorithms import myopic_algorithm, anthill_algorithm, dijkstra_algorithm
import user_variables as uv
from datetime import datetime
import pandas as pd


def comparison():
    grid_sizes = [5, 10, 15, 20, 25]
    # grid_sizes = [10]  # You can extend this list as needed
    num_runs = 1  # of each algorithm per grid size

    # Create an empty DataFrame to store the results
    results = pd.DataFrame(columns=['Algorithm', 'Size', 'Score'])

    for size in grid_sizes:
        print(f"Running comparison for maze size {size}x{size}")
        for algorithm_name, algorithm_func in [('Myopic', myopic_algorithm), ('Anthill', anthill_algorithm), ('Dijkstra', dijkstra_algorithm)]:
            print(f"Running {algorithm_name} algorithm...")
            scores = []
            for run in range(num_runs):
                playing_grid = generate_grid(size, size)
                start_index, current_value, end_index = starting_conditions(
                    playing_grid, size, size)
                current_row, current_column = start_index
                final_score, _ = algorithm_func(
                    playing_grid, current_row, current_column, start_index, current_value, end_index, display=False)
                scores.append(final_score)

            # Calculate the average score and append to results
            avg_score = sum(scores) / num_runs
            row = pd.DataFrame({'Algorithm': [algorithm_name], 'Size': [
                               size], 'Score': [avg_score]})
            results = pd.concat([results, row], ignore_index=True)

            print(results)

    # Plot the results for each algorithm
    for algorithm in ['Myopic', 'Anthill', 'Dijkstra']:
        subset = results[results['Algorithm'] == algorithm]
        plt.plot(subset['Size'], subset['Score'], label=algorithm)

    plt.xlabel('Maze Size')
    plt.ylabel('Score')
    plt.legend()
    plt.xticks(grid_sizes)  # Set the x-ticks to the actual maze sizes
    plt.gca().invert_yaxis()  # Invert the y-axis to make lower scores better
    plt.show()


comparison()
