import matplotlib.pyplot as plt
import numpy as np
import user_variables as uv
import matplotlib.colors as mcolors
import matplotlib.cm as cm

'''
Displays the final route for individual algorithms when called from the main function.
In the case of anthill_algorithm, it also shows a plot of pheromone concentration before displaying the final route.
'''


def display_grid(grid, current_position, path=None, pheromones=None):
    # If pheromones are provided, display them using a custom color map
    if pheromones is not None:
        # Create a custom color map from light yellow to red
        cmap = mcolors.LinearSegmentedColormap.from_list(
            "custom_cmap", ['lightyellow', 'red'])
        # Normalize the pheromones to fit within the color map
        normalized_pheromones = (pheromones - np.min(pheromones)) / \
            (np.max(pheromones) - np.min(pheromones))
        # Plot the pheromones using the custom color map
        plt.imshow(normalized_pheromones, cmap=cmap)
        # Add a color bar to show the pheromone levels
        plt.colorbar(label="Pheromone Level")
    else:
        # If no pheromones are provided, use the original plotting code
        cmap = plt.cm.colors.ListedColormap(['lightblue', 'yellow', 'darkblue'])
        bounds = [0, 0.5, 1.5, 2.5]
        norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
        plot_grid = np.zeros_like(grid, dtype=np.float64)
        if path:
            for cell in path:
                plot_grid[cell] = 1
        plt.imshow(plot_grid, cmap=cmap, norm=norm)

    # Plot the current position of the agent
    plt.scatter(*current_position, color='r')

    # Add text labels to each cell
    for (i, j), value in np.ndenumerate(grid):
        plt.text(j, i, value, ha='center', va='center',
                 color='black', weight='bold', fontsize=10)

    plt.show()


def generate_grid(height, width):
    playing_grid = np.random.randint(
        uv.lowest_value, uv.highest_value, size=(height, width))
    return playing_grid


def starting_conditions(playing_grid, height, width):
    start_index = uv.start_index
    current_value = playing_grid[uv.start_index]
    end_index = (height - 1, width - 1)  # End index is bottom-right corner
    return start_index, current_value, end_index
