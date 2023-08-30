# Enter the dimensions of the playing field
grid_size = (25, 25)
end_index_string = f"{grid_size[0]},{grid_size[1]}"
grid_height = 25
grid_width = 25
end_index = (24, 24)
end_index_string = f"{end_index[0]},{end_index[1]}"

# Enter the starting space of the agent [vertical, horizontal]
start_index = (0, 0)
start_index_string = f"{start_index[0]},{start_index[1]}"
start_column = 0
start_row = 0

# Enter the lowest value a space can contain
lowest_value = 1

# Enter the highest value a space can contain
highest_value = 9

# Enter whether the agent's goal is to finish with the largest or smallest sum
shortest_path = 1

# Enter the name of the algorithm to use
algorithm = "anthill_algorithm"  # myopic_algorithm anthill_algorithm dijkstra_algorithm

# Enter the anthill_algorithm initialisation parameters
num_ants = 20
evaporation_rate = 0.1
pheromone_deposit = 0.5
