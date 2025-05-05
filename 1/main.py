def read_input(file):
    left_list = []
    right_list = []
    
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
                
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    
    # Calculate distance between corresponding elements
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
        
    return total_distance

def main():
    left_list, right_list = read_input("input.txt")
    
    # Calculate the total distance between the lists
    total_distance = calculate_total_distance(left_list, right_list)
    print(total_distance)

if __name__ == "__main__":
    main()
