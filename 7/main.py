from itertools import product

test, ex_one = "7/input.txt", "7/ex_one.txt"
file = test

def read_input(file):
    grid = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            for char in line:
                if char == ":":
                    idx = line.index(char)
                    grid.append([int(line[:idx])] + [int(i) for i in line[idx + 1:].split()])
    return grid

def poss_operations(target, nums):
    operators = ['+', '*', '||']

    for ops in product(operators, repeat= len(nums) - 1):
        res = nums[0]
        for op, num in zip(ops, nums[1:]):
            if op == '+':
                res += num
            elif op == '*':
                res *= num
            elif op == '||':
                res = int(str(res) + str(num))
        if res == target:
            return True

    return False

# P1
def bridge_repair():
    grid = read_input(file)
    s = 0

    for line in grid:
        target = line[0]

        if poss_operations(target, line[1:]):
            s += target

    return s

print(bridge_repair())
