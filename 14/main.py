import re as regex

one_robot, example, test = "14/move_one_robot.txt", "14/example.txt", "14/input.txt"

def setup(file, width, height):
    robots, r = [], regex.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    with open(file, "r") as f:
        for line in f: 
            if match := r.match(line.strip()):
                p_x, p_y, v_x, v_y = match.groups()
                y = int(p_y) % height
                x = int(p_x) % width
                robots.append((y, x, int(v_y), int(v_x)))

    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    for robot in robots:
        grid[robot[0]][robot[1]] += 1

    return grid, robots

def alias(robot):
    return robot[0], robot[1], robot[2], robot[3]

def move_robots(grid, robots, seconds):
    width, height = len(grid[0]), len(grid)
    while seconds > 0:
        # create new grid
        new_grid = [[0 for _ in range(width)] for _ in range(height)]
        
        for i in range(len(robots)):
            p_y, p_x, v_y, v_x = alias(robots[i])
            # move robot
            p_y, p_x = (p_y + v_y) % height, (p_x + v_x) % width
            # add to new grid
            new_grid[p_y][p_x] += 1
            # update robot position
            robots[i] = (p_y, p_x, v_y, v_x)
        
        grid = new_grid
        seconds -= 1
    return grid, robots

def find_safest_quadrant(grid):
    width, height = len(grid[0]), len(grid)
    mid_x, mid_y = width // 2, height // 2
    cnts = [0, 0, 0, 0]
    
    for i in range(height):
        for j in range(width):
            num_robots = grid[i][j]
            
            # skip robots in the middle
            if i == mid_y or j == mid_x:
                continue
            
            if i < mid_y and j < mid_x:
                cnts[0] += num_robots
            elif i < mid_y and j > mid_x:
                cnts[1] += num_robots
            elif i > mid_y and j < mid_x:
                cnts[2] += num_robots
            elif i > mid_y and j > mid_x:
                cnts[3] += num_robots
    
    # calculate safety factor
    safety_factor = 1
    for count in cnts:
        safety_factor *= count
    
    return safety_factor

def restroom_redoubt(file, seconds, width = 101, height = 103):
    grid, robots = setup(file, width, height)
    grid, robots = move_robots(grid, robots, seconds)
    return grid, find_safest_quadrant(grid)

def print_grid(grid):
    for row in grid:
        line = ""
        for cell in row:
            if cell == 0:
                line += "."
            else:
                line += str(cell)
        print(line)

# P1
print(f"P1 | One Robot: {restroom_redoubt(one_robot, 100, 11, 7)}")
print(f"P1 | Example: {restroom_redoubt(example, 100, 11, 7)}")
print(f"P1 | Test: {restroom_redoubt(test, 100)}")

def find_high_cluster_areas(grid):
    width, height = len(grid[0]), len(grid)
    # Calculate the size of each area
    area_width = width // 10
    area_height = height // 10
    
    # Check each area
    for area_y in range(10):
        for area_x in range(10):
            robot_count = 0
            # Get the bounds for this area
            start_y = area_y * area_height
            end_y = start_y + area_height
            start_x = area_x * area_width
            end_x = start_x + area_width
            
            # Count robots in this area
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    robot_count += grid[y][x]
            
            # If we find an area with more than 50 robots, return True
            if robot_count > 50:
                return True
    
    return False

# P2
def find_christmas_tree():
    for i in range(6760, 10000):
        grid, _ = restroom_redoubt(test, i)
        if find_high_cluster_areas(grid):
            print(f"P2 | Test: {print_grid(grid)}" + f" | Seconds: {i}\n")
        else:
            print(f"P2 | Tried {i} seconds")

find_christmas_tree()
