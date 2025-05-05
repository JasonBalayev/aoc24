def setup():
    test, ex_two = "4/input.txt", "4/ex_two.txt"
    with open(test) as f:
        grid = [line.strip() for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word = "XMAS"
    return grid, rows, cols, word

def find_xmas():
    # Setup the grid, it's dimensions and the directions to get the final count
    count, directions = 0, [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    grid, rows, cols, word = setup()

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            # Start of 'XMAS' at (i, j) in the grid
            if grid[i][j] == 'X':
                for dx, dy in directions:
                    found = True
                    # Try to find 'XMAS' in the all directions
                    for k in range(1, len(word)):
                        # New coordinates
                        dx_i, dy_j = i + dx * k, j + dy * k
                        # Out of bounds or not the next letter
                        out_of_bounds = dx_i < 0 or dx_i >= rows or dy_j < 0 or dy_j >= cols
                        # Not valid 'XMAS' letter
                        if out_of_bounds or grid[dx_i][dy_j] != word[k]:
                            found = False
                            break
                    # Valid 'XMAS' | + 1 to the count
                    if found:
                        count += 1
    return count

print(find_xmas())

def find_x_mas():
    count = 0
    grid, rows, cols, word = setup()

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                # get the  diagonal characters
                tl = grid[i - 1][j - 1]  # top-left
                tr = grid[i - 1][j + 1]  # top-right
                bl = grid[i + 1][j - 1]  # bottom-left
                br = grid[i + 1][j + 1]  # bottom-right

                # define the two possible MAS patterns for each diagonal
                diagonal1 = (tl, br)
                diagonal2 = (bl, tr)

                # check for both forward and backward MAS in diagonals
                if ((diagonal1 == ('M', 'S') or diagonal1 == ('S', 'M')) and
                    (diagonal2 == ('M', 'S') or diagonal2 == ('S', 'M'))):
                    count += 1

    return count

print(find_x_mas())


