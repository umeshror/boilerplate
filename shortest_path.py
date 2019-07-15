grid_x = 4
grid_y = 5
grid = [[1, 1, 1, 0, 1],
        [1, 0, 2, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]]

def find_shortest_route(mat, x_index, y_index, routes_found, visited_mat):
    if (x_index == 0 or y_index == 0 or x_index == (grid_x - 1) or y_index == (grid_y - 1)):
        return 0

    if (routes_found[x_index][y_index] != -1):
        # already gone though this point and returning the shortest path possible
        return routes_found[x_index][y_index]

    visited_mat[x_index][y_index] = True

    route_up, route_right, route_left, route_down = 10 ** 9, 10 ** 9, 10 ** 9, 10 ** 9

    # move up
    if (mat[x_index - 1][y_index] == 0):
        if (visited_mat[x_index - 1][y_index] == False):
            route_up = 1 + find_shortest_route(mat, x_index - 1, y_index, routes_found, visited_mat)


    # move right
    if (mat[x_index][y_index + 1] == 0):
        if (visited_mat[x_index][y_index + 1] == False):
            route_right = 1 + find_shortest_route(mat, x_index, y_index + 1, routes_found, visited_mat)


    # move down
    if (mat[x_index + 1][y_index] == 0):
        if (visited_mat[x_index + 1][y_index] == False):
            route_down = 1 + find_shortest_route(mat, x_index + 1, y_index, routes_found, visited_mat)

    # move left
    if (mat[x_index][y_index - 1] == 0):
        if (visited_mat[x_index][y_index - 1] == False):
            route_left = 1 + find_shortest_route(mat, x_index, y_index - 1, routes_found, visited_mat)


    routes_found[x_index][y_index] = min(route_up, route_right, route_left, route_down)

    return routes_found[x_index][y_index]



def find_index_of_element(grid, value):
    for x_index, row in enumerate(grid):
        for y_index, element in enumerate(row):
            if element == value:
                return x_index, y_index
    raise Exception("Value not present in Grid")

def escape_from_grid(grid_x, grid_y, grid):
    x_index, y_index = find_index_of_element(grid, 2)

    routes_found = [[-1 for _ in range(grid_y)] for _ in range(grid_x)]

    visited_mat = [[False for _ in range(grid_y)] for _ in range(grid_x)]

    return find_shortest_route(grid, x_index, y_index, routes_found, visited_mat)



shortes_path_to_escaoe = escape_from_grid(grid_x, grid_y, grid)
print shortes_path_to_escaoe
# ouput: 2
