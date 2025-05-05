from math import gcd

test, ex_one = "8/input.txt", "8/ex_one.txt"
file = test

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            lst = list(line.strip())
            grid.append(lst)
    return grid

def find_antinodes(grid): 
    rows, cols = len(grid), len(grid[0]) if len(grid) > 0 else 0

    antennas = {}
    for y in range(rows):
        for x in range(cols):
            cell = grid[y][x]
            if cell != '.':
                antennas.setdefault(cell, []).append((x, y))

    for _, pos in antennas.items():
        n = len(pos)
        if n < 2: continue

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = pos[i]
                x2, y2 = pos[j]

                dx, dy = x2 - x1, y2 - y1
                div = gcd(dx, dy) if gcd(dx, dy) != 0 else 1
                step_x, step_y = dx // div, dy // div

                antinode1 = (x1 - step_x * div, y1 - step_y * div)
                antinode2 = (x2 + step_x * div, y2 + step_y * div)

                for ax, ay in [antinode1, antinode2]:
                    if 0 <= ax < cols and 0 <= ay < rows:
                        grid[ay][ax] = '#'

# P1
def resonant_collinearity():
    grid = read_input(file)
    num_antinodes = 0

    find_antinodes(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                num_antinodes += 1

    return num_antinodes # sol 1 = 390

print(resonant_collinearity())

def find_antinodes_normalized(grid):

    def get_normalized_line(x1, y1, x2, y2):
        A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2

        div = gcd(gcd(abs(A), abs(B)), abs(C)) if C != 0 else gcd(abs(A), abs(B))
        if div != 0:
            A //= div
            B //= div
            C //= div

        if A < 0 or (A == 0 and B < 0):
            A *= -1
            B *= -1
            C *= -1

        return (A, B, C)

    rows, cols = len(grid), len(grid[0]) if len(grid) > 0 else 0

    antennas = {}
    for y in range(rows):
        for x in range(cols):
            cell = grid[y][x]
            if cell != '.':
                antennas.setdefault(cell, []).append((x, y))

    for _, pos in antennas.items():
        n = len(pos)
        if n < 2:
            continue

        lines = set()
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                line = get_normalized_line(x1, y1, x2, y2)
                lines.add(line)

        for line in lines:
            A, B, C = line
            for y in range(rows):
                for x in range(cols):
                    if A * x + B * y + C == 0:
                        grid[y][x] = '#'

# P2
def resonant_collinearity_normalized():
    grid = read_input(file)
    num_antinodes = 0

    find_antinodes_normalized(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                num_antinodes += 1

    return num_antinodes # sol 2 --> 1246

print(resonant_collinearity_normalized())