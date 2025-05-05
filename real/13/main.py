import re

def read_input(file):
    A, B, G = [], [], []
    with open(file, "r") as f:
        content = f.read().strip().split("\n\n")
        
        for block in content:
            lines = block.strip().split("\n")
                
            a_match = re.match(r"Button\s*A:\s*X\+(\d+),\s*Y\+(\d+)", lines[0])
            if a_match:
                x, y = map(int, a_match.groups())
                A.append((x, y))

            b_match = re.match(r"Button\s*B:\s*X\+(\d+),\s*Y\+(\d+)", lines[1])
            if b_match:
                x, y = map(int, b_match.groups())
                B.append((x, y))
            
            g_match = re.match(r"Prize:\s*X=(\d+),\s*Y=(\d+)", lines[2])
            if g_match:
                x, y = map(int, g_match.groups())
                G.append((x, y))
    
    return A, B, G

def solve_linear_system(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    
    if det == 0: return None
    
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    if x.is_integer() and y.is_integer():
        return (int(x), int(y))
    else: return None

# P1
def claw_contraption(file):
    A, B, G = read_input(file)
    tokens = 0

    for a, b, g in zip(A, B, G):
        solution = solve_linear_system(
            a[0], b[0], g[0],
            a[1], b[1], g[1]
        )
        
        if solution:
            x, y = solution
            tokens += 3 * x + y

    return tokens

# P2 
def claw_contraption_2(file):
    A, B, G = read_input(file)
    for i, (x, y) in enumerate(G):
        G[i] = (x + 10000000000000, y + 10000000000000)
    tokens = 0

    for a, b, g in zip(A, B, G):
        solution = solve_linear_system(
            a[0], b[0], g[0],
            a[1], b[1], g[1]
        )
        
        if solution:
            x, y = solution
            tokens += 3 * x + y

    return tokens
    
def main():
    example, test = "13/example.txt", "13/test.txt"
    print(f"P1:")
    print(f"Example total tokens: {claw_contraption(example)}")
    print(f"Test total tokens: {claw_contraption(test)}")
    print()
    print(f"P2:")
    print(f"Example total tokens: {claw_contraption_2(example)}")
    print(f"Test total tokens: {claw_contraption_2(test)}")

main()
