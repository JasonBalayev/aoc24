def read_input(file):
    reports = []
    
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                levels = list(map(int, line.split()))
                reports.append(levels)
                
    return reports

def is_safe_report(levels):
    # Check if there are at least 2 levels
    if len(levels) < 2:
        return True
    
    # The sequence should be increasing or decreasing
    if levels[1] > levels[0]:
        direction = "increasing"
    elif levels[1] < levels[0]:
        direction = "decreasing"
    else:
        return False   
    
    # Check each pair of adjacent levels
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        
        # Check if direction is consistent
        if (direction == "increasing" and diff <= 0) or (direction == "decreasing" and diff >= 0):
            return False
        
        # Check if difference is between 1 and 3 is inclusive
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
    return True

def count_safe_reports(reports):
    safe_count = 0
    
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    
    return safe_count

def main():
    reports = read_input("input.txt")
    
    # Calculates safe reports
    safe_count = count_safe_reports(reports)
    print(safe_count)

if __name__ == "__main__":
    main()

#Solved by $J 