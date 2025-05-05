from collections import Counter

def read_input(file):
    with open(file, "r") as f:
        line = f.readline().strip()
        return [int(num) for num in line.split()]

def split_stone(stone):
    """
    Splits a stone according to the rules:
    - If stone is 0, returns [1]
    - If number of digits is even, splits into two parts
    - If number of digits is odd, multiplies by 2024
    """
    if stone == 0:
        return [1]
    
    n = len(str(stone))
    if n % 2 == 0:
        divisor = 10 ** (n // 2)
        return [stone // divisor, stone % divisor]
    else:
        result = 2024 * stone
        return [result]

def blink(stones, blinks):
    counts = Counter(stones)
    
    while blinks > 0:
        next_counts = Counter()
        for stone, count in counts.items():
            split_results = split_stone(stone)
            for new_stone in split_results:
                next_counts[new_stone] += count
        counts = next_counts
        blinks -= 1
    
    return sum(counts.values())

def plutonian_pebbles(file, num_blinks=25):
    stones = read_input(file)
    return blink(stones, num_blinks)

def main():
    example_file = "11/example.txt"
    test_file = "11/input.txt"
    
    example_result_p1 = plutonian_pebbles(example_file, 25)
    test_result_p1 = plutonian_pebbles(test_file, 25)
    example_result_p2 = plutonian_pebbles(example_file, 75)
    test_result_p2 = plutonian_pebbles(test_file, 75)
    
    print(f"P1:")
    print(f"Example result after 25 blinks: {example_result_p1}")
    print(f"Test result after 25 blinks: {test_result_p1}")
    print()
    print(f"P2:")
    print(f"Example result after 75 blinks: {example_result_p2}")
    print(f"Test result after 75 blinks: {test_result_p2}")

main()
