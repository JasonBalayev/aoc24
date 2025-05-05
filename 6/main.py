import copy as cpy

test, ex_one = "6/input.txt", "6/ex_one.txt"
file = test

directions = ["NORTH", "EAST", "SOUTH", "WEST"]
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def read_input(file):
    grid, guard = [], None

    with open(file) as f:
        for line in f:
            if line.strip() == "": break
            grid.append(list(line.strip()))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                guard = (i, j, "NORTH")
                grid[i][j] = "X"
                break
        if guard:
            break

    return grid, guard

def in_front(grid, guard):
    row, col, direction = guard
    dx, dy = moves[directions.index(direction)]
    target_row = row + dx
    target_col = col + dy

    if 0 <= target_row < len(grid) and 0 <= target_col < len(grid[0]):
        return grid[target_row][target_col]
    else:
        return "OVER"

def move_and_mark(grid, guard):
    row, col, direction = guard
    ahead = in_front(grid, guard)

    if ahead == "#":
        # turn right at obstacle
        direction = directions[(directions.index(direction) + 1) % 4]
    
    if ahead == "." or ahead == "X":
        # move until obstacle or edge of grid
        while ahead != "#" and ahead != "OVER":
            dx, dy = moves[directions.index(direction)]
            dx_row, dx_col = row + dx, col + dy

            # check boundaries before moving
            if 0 <= dx_row < len(grid) and 0 <= dx_col < len(grid[0]):
                row, col = dx_row, dx_col
                grid[row][col] = "X"
                ahead = in_front(grid, (row, col, direction))
            else:
                # reached the edge of the grid or obstacle
                return (row, col, direction)
    
    return (row, col, direction)

def guard_walk(grid, guard):
    visited = set()
    while True:
        if in_front(grid, guard) == "OVER":
            break  # guard has exited the grid, no loop
        guard = move_and_mark(grid, guard)
        if guard in visited:
            # loop
            return True
        visited.add(guard)
    return False

# P1
def guard_gallivant():
    grid, guard = read_input(file)
    cnt = 0
    
    guard = guard_walk(grid, guard)

    # count all visited positions marked with 'X'
    for row in grid:
        for col in row:
            if col == "X":
                cnt += 1
    
    return cnt

print(guard_gallivant()) 

def is_in_loop(grid, guard):
    visited = set()
    while True:
        if in_front(grid, guard) == "OVER":
            return False  # guard exits, no loop
        guard = move_and_mark(grid, guard)
        if guard in visited:
            return True  # loop
        visited.add(guard)

# P2
def guard_gallivant_loop():
    grid, guard = read_input(file)
    poss = 0

    starting_position = (guard[0], guard[1])
    initial_grid = cpy.deepcopy(grid)
    guard_walk(initial_grid, guard)

    potential_obstructions = []
    for i in range(len(initial_grid)):
        for j in range(len(initial_grid[i])):
            if initial_grid[i][j] == "X" and (i, j) != starting_position:
                potential_obstructions.append((i, j))

    for (i, j) in potential_obstructions:
        temp_grid = cpy.deepcopy(grid)
        temp_grid[i][j] = "#"
        new_guard = (guard[0], guard[1], guard[2])
        loop = is_in_loop(temp_grid, new_guard)

        if loop:
            poss += 1

    return poss

print(guard_gallivant_loop())
