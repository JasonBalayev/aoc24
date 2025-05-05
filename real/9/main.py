test, ex_one = "9/input.txt", "9/ex_one.txt"
file = ex_one

def read_input(file):
    res = ""
    # read line into storage form
    with open(file, "r") as f:
        idx = 0
        for file_or_storage, char in enumerate(f.read(), start = 1):
            if file_or_storage % 2 == 1:
                for _ in range(int(char)):
                    res += str(idx)
                idx += 1
            else: 
                for _ in range(int(char)):
                    res += "."
    return res

# build the grid and return the last line
def compute_grid(file):
    line = read_input(file)
    n = len(line)
    
    # find the number of dots
    num_dots = 0
    for i in range(len(line)):
        if line[i] == ".":
            num_dots += 1
    
    # add the first line to the grid
    grid = []
    grid.append(line)
    
    # add the rest of the lines to the grid
    for _ in range(num_dots):
        idx = line.find(".")
        last_char = line[len(line) - 1]
        new_line = line[:idx] + last_char + line[idx + 1:len(line) - 1]
        line = new_line
        grid.append(line)
        
        # Ensure all lines have the same length by padding with dots
        while len(line) < n:
            line += "."
    
    return grid[len(grid) - 1]

# P1
def disk_fragmenter():
    last_line = compute_grid(file)

    # calculate checksum
    checksum = 0
    for idx, char in enumerate(last_line):
        if char != ".":
            checksum += idx * int(char)

    return checksum

print(disk_fragmenter())