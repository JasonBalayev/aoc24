example, test = "10/ex_one.txt", "10/input.txt"
file = test

def read_input(file):
    G = []
    with open(file, "r") as f:
        for line in f:
            G.append([int(num) for num in line.strip()])
    return G

# P1 & P2
def hoof_it():
    G = read_input(file)
    rows, cols = len(G), len(G[0])
    
    # find all trailheads
    trailheads = []
    for row in range(rows):
        for col in range(cols):
            if G[row][col] == 0:
                trailheads.append((row, col))

    # YAY! returns score_normal, score_distinct
    def dfs(pos, curr_height, visited):
        i, j = pos
        nines, paths = set(), 0

        # base case: found a path to 9
        if G[i][j] == 9:
            nines.add((i, j))
            return nines, 1

        # search all four directions
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in dirs:
            new_i, new_j = i + di, j + dj
            new_pos = (new_i, new_j)
            
            # check bounds and if position was visited
            if (0 <= new_i < rows and 
                0 <= new_j < cols and 
                new_pos not in visited):
                
                # update if we find the next number
                if G[new_i][new_j] == curr_height + 1:
                    new_nines, new_paths = dfs(new_pos,
                                            curr_height + 1,
                                            visited | {new_pos})
                    nines.update(new_nines)   
                    paths += new_paths         
                    
        return nines, paths

    # calculate both scores for each trailhead
    score, rating = 0, 0
    for start in trailheads:
        nines, paths = dfs(start, 0, {start})
        score += len(nines)
        rating += paths
    return score, rating

ans = hoof_it()
print("Reachable nines score:", ans[0])
print("Distinct paths score:", ans[1])
