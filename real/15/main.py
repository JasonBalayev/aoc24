example, test = "15/example.txt", "15/test.txt"

# P1
def setup(file):
    grid, moves, robot = [], [], None
    reading_grid = True

    with open(file, "r") as f:
        row = 0
        for line in f:
            line = line.strip()
            if line == "":
                reading_grid = False
                continue
            
            if reading_grid:
                for col, char in enumerate(line):
                    if char == "@":
                        robot = (row, col)
                grid.append(list(line))
                row += 1
            else:
                moves.extend(list(line))

    return grid, moves, robot

def move_robot(grid, moves, robot):
    for move in moves:
        x, y = robot
        direction = in_front(move)
        new_x, new_y = x + direction[0], y + direction[1]
        
        # check if new position is within grid bounds
        if (new_x < 0 or new_x >= len(grid) or 
            new_y < 0 or new_y >= len(grid[0])):
            continue
            
        # if the robot is in front of a wall, continue
        if grid[new_x][new_y] == "#":
            continue

        # is the robot in front of a box?
        if grid[new_x][new_y] == "O":
            # is the box pushable?
            if box_can_be_pushed(grid, robot, direction):
                # then push the box
                grid = push_boxes(grid, move, robot)
                robot = (new_x, new_y)
            continue # else, continue
        
        # if the robot is in front of an empty space, move it
        if grid[new_x][new_y] == ".":
            # move the robot to the new position
            grid[x][y] = "."
            grid[new_x][new_y] = "@"
            # update the robot position
            robot = (new_x, new_y)

    return grid

def in_front(move):
    directions = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }

    return directions[move]

def box_can_be_pushed(grid, robot, direction):
    curr_pos = (robot[0] + direction[0], robot[1] + direction[1])
    boxes_to_push = []
    
    # keep checking forward until we find empty space or a wall
    while True:
        # check bounds
        if (curr_pos[0] < 0 or curr_pos[0] >= len(grid) or 
            curr_pos[1] < 0 or curr_pos[1] >= len(grid[0])):
            return False
        
        # check what's in the current position
        curr_cell = grid[curr_pos[0]][curr_pos[1]]
        
        if curr_cell == ".":  # found empty space - we can push!
            return True
        elif curr_cell == "#":  # hit a wall - can't push
            return False
        elif curr_cell == "O":  # found another box
            boxes_to_push.append(curr_pos)
            # keep looking forward
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
        else:
            return False

def push_boxes(grid, move, robot):
    direction = in_front(move)
    curr_pos = robot
    boxes = []
    
    # find all the boxes in sequence
    while True:
        next_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
        if grid[next_pos[0]][next_pos[1]] == "O":
            boxes.append(next_pos)
            curr_pos = next_pos
        else:
            break
    
    # move all the boxes (starting from the last one)
    for box in reversed(boxes):
        new_box_pos = (box[0] + direction[0], box[1] + direction[1])
        grid[box[0]][box[1]] = "."
        grid[new_box_pos[0]][new_box_pos[1]] = "O"
    
    # move the robot
    x, y = robot
    new_x, new_y = x + direction[0], y + direction[1]
    grid[x][y] = "."
    grid[new_x][new_y] = "@"
    
    return grid

def final_grid(file):
    grid, moves, robot = setup(file)
    grid = move_robot(grid, moves, robot)
    return grid
 
def sum_gps(grid):
    res = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "O":
                res += 100 * r + c
    return res

# P2
def make_second_grid(grid):
    new_grid = []
    for row in grid:
        line = []
        for ch in row:
            if ch == "#":
                line.extend(["#", "#"])
            elif ch == "O":
                line.extend(["[", "]"])
            elif ch == ".":
                line.extend([".", "."])
            else:  # "@"
                line.extend(["@", "."])
        new_grid.append(line)
    return new_grid

def setup_part2(file):
    grid, moves, robot = setup(file)
    wide_grid = make_second_grid(grid)
    # Robot's x position stays same, y position doubles
    new_robot = (robot[0], robot[1] * 2)
    return wide_grid, moves, new_robot

def sum_gps_part2(grid):
    total = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "[":  # Only count left edge of boxes
                total += 100 * r + (c // 2)  # Convert to original coordinate system
    return total

def final_grid_part2(file):
    grid, moves, robot = setup_part2(file)
    final = move_robot_part2(grid, moves, robot)
    return final

def push_boxes_part2(grid, move, robot):
    direction = in_front(move)
    boxes = []
    curr_pos = (robot[0] + direction[0], robot[1] + direction[1])
    
    # Find all boxes that need to be pushed
    while curr_pos[0] >= 0 and curr_pos[0] < len(grid) and curr_pos[1] >= 0 and curr_pos[1] < len(grid[0]):
        curr_cell = grid[curr_pos[0]][curr_pos[1]]
        if curr_cell == "[":
            # Found a box, store its position and skip over the "]"
            boxes.append((curr_pos[0], curr_pos[1]))
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1] + 1)
        elif curr_cell == "]":
            # Skip over the right side of the box
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
        elif curr_cell in [".", "@"]:
            break
        else:
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
    
    # Move boxes from last to first
    for box_pos in reversed(boxes):
        # Clear old box position
        grid[box_pos[0]][box_pos[1]] = "."
        grid[box_pos[0]][box_pos[1] + 1] = "."
        
        # Calculate new box position
        new_x = box_pos[0] + direction[0]
        new_y = box_pos[1] + direction[1]
        if direction[1] != 0:  # If moving horizontally
            grid[new_x][new_y] = "["
            grid[new_x][new_y + 1] = "]"
        else:  # If moving vertically
            grid[new_x][new_y] = "["
            grid[new_x][new_y + 1] = "]"
    
    # Move robot
    grid[robot[0]][robot[1]] = "."
    new_robot = (robot[0] + direction[0], robot[1] + direction[1])
    grid[new_robot[0]][new_robot[1]] = "@"
    
    return grid

def box_can_be_pushed_part2(grid, robot, direction):
    curr_pos = (robot[0] + direction[0], robot[1] + direction[1])
    boxes = []
    
    while True:
        # Check bounds
        if (curr_pos[0] < 0 or curr_pos[0] >= len(grid) or 
            curr_pos[1] < 0 or curr_pos[1] >= len(grid[0])):
            return False
        
        curr_cell = grid[curr_pos[0]][curr_pos[1]]
        
        if curr_cell == ".":  # Empty space - can push!
            return True
        elif curr_cell == "#":  # Wall - can't push
            return False
        elif curr_cell in ["[", "]"]:
            if curr_cell == "[":
                boxes.append(curr_pos)
                # Skip to after the "]"
                curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + 2)
            else:  # "]"
                curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + 1)
        else:
            return False

def move_robot_part2(grid, moves, robot):
    current_robot = robot
    
    for move in moves:
        direction = in_front(move)
        new_x = current_robot[0] + direction[0]
        new_y = current_robot[1] + direction[1]
        
        # Check bounds
        if (new_x < 0 or new_x >= len(grid) or 
            new_y < 0 or new_y >= len(grid[0])):
            continue
            
        # Check wall
        if grid[new_x][new_y] == "#":
            continue
            
        # Check box
        if grid[new_x][new_y] in ["[", "]"]:
            if box_can_be_pushed_part2(grid, current_robot, direction):
                grid = push_boxes_part2(grid, move, current_robot)
                current_robot = (new_x, new_y)
            continue
            
        # Move to empty space
        if grid[new_x][new_y] == ".":
            grid[current_robot[0]][current_robot[1]] = "."
            grid[new_x][new_y] = "@"
            current_robot = (new_x, new_y)
    
    return grid

def main():
    print(f"P1:")
    print(f"Example GPS sum: {sum_gps(final_grid(example))}")
    print(f"Test GPS sum: {sum_gps(final_grid(test))}")

    print()
    print(f"P2:")

    initial, _, robot = setup_part2(example)
    for row in initial:
        print(''.join(row))
    print(robot)
    print(initial[robot[0]][robot[1]])

    print()
    final = final_grid_part2(example)
    for row in final:
        print(''.join(row))
    print()
    print(f"Example GPS sum (part 2): {sum_gps_part2(final)}")
    # print(f"Test GPS sum (part 2): {sum_gps_part2(final_grid_part2(test))}")

main()