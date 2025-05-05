def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def calculate_areas(final_regions):
    return [len(visited) for visited in final_regions]

def calculate_perimeters(final_regions, grid):
    perimeters = []
    
    for visited in final_regions:
        perimeter = 0
        visited_set = set(visited)
        
        for row, col in visited:
            edges = 4
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) in visited_set:
                    edges -= 1
            perimeter += edges
        perimeters.append(perimeter)
    
    return perimeters

def calculate_straight_edges(final_regions, grid):
    rows, cols = len(grid), len(grid[0])
    perimeters = []
    
    for visited in final_regions:
        visited_set = set(visited)
        sides = set()
        
        def is_visited(r, c):
            return (r, c) in visited_set
        
        for row, col in visited:
            # check top edge
            if not is_visited(row - 1, col):
                start_col = col
                while start_col > 0 and is_visited(row, start_col - 1) and not is_visited(row - 1, start_col - 1):
                    start_col -= 1
                end_col = col
                while end_col < cols - 1 and is_visited(row, end_col + 1) and not is_visited(row - 1, end_col + 1):
                    end_col += 1
                sides.add((row, start_col, row, end_col, 'H'))
            
            # check bottom edge
            if not is_visited(row+1, col):
                start_col = col
                while start_col > 0 and is_visited(row, start_col - 1) and not is_visited(row+1, start_col -1 ):
                    start_col -= 1
                end_col = col
                while end_col < cols - 1 and is_visited(row, end_col + 1) and not is_visited(row+1, end_col + 1):
                    end_col += 1
                sides.add((row + 1, start_col, row + 1, end_col, 'H'))
            
            # check left edge
            if not is_visited(row, col-1):
                start_row = row
                while start_row > 0 and is_visited(start_row - 1, col) and not is_visited(start_row - 1, col - 1):
                    start_row -= 1
                end_row = row
                while end_row < rows - 1 and is_visited(end_row + 1, col) and not is_visited(end_row + 1, col - 1):
                    end_row += 1
                sides.add((start_row, col, end_row, col, 'V'))
            
            # check right edge
            if not is_visited(row, col+1):
                start_row = row
                while start_row > 0 and is_visited(start_row - 1, col) and not is_visited(start_row - 1, col + 1):
                    start_row -= 1
                end_row = row
                while end_row < rows - 1 and is_visited(end_row + 1, col) and not is_visited(end_row + 1, col + 1):
                    end_row += 1
                sides.add((start_row, col + 1, end_row, col + 1, 'V'))
        
        perimeters.append(len(sides))
    
    return perimeters

# P1 & P2
def garden_groups(file, straight_edges=False):
    G = read_input(file)
    rows, cols = len(G), len(G[0])
    
    def dfs(row, col, region, visited, seen):
        if ((row, col) in seen or
            row < 0 or
            row >= rows or
            col < 0 or 
            col >= cols or
            G[row][col] != region):
            return
        
        visited.add((row, col))
        seen.add((row, col))
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(row + dr, col + dc, region, visited, seen)
        
        return visited
    
    final_regions, seen = [], set()
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in seen:
                region = G[row][col]
                visited = dfs(row, col, region, set(), seen)
                if visited:
                    final_regions.append(visited)
    
    areas = calculate_areas(final_regions)
    perimeters = calculate_straight_edges(final_regions, G) if straight_edges else calculate_perimeters(final_regions, G)
    
    return sum(area * perimeter for area, perimeter in zip(areas, perimeters))

def main():
    helper, example_1, example_2, test = "12/helper.txt", "12/example_1.txt", "12/example_2.txt", "12/test.txt"

    helper_result_p1 = garden_groups(helper)
    example_1_result_p1 = garden_groups(example_1)
    test_result_p1 = garden_groups(test)

    helper_result_p2 = garden_groups(helper, True)
    example_2_result_p2 = garden_groups(example_2, True)
    test_result_p2 = garden_groups(test, True)
    
    print(f"P1:")
    print(f"Helper total fence price: {helper_result_p1}")
    print(f"Example total fence price: {example_1_result_p1}")
    print(f"Test total fence price: {test_result_p1}")
    print()
    print(f"P2:")
    print(f"Helper total fence price: {helper_result_p2}")
    print(f"Example 2 total fence price: {example_2_result_p2}")
    print(f"Test total fence price: {test_result_p2}")

main()
