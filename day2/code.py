DAY = 'day_2'

def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def check_safe(levels):
    differences = []
    for i, level in enumerate(levels):
        if i == len(levels)-1:
            break
        differences.append(level - levels[i+1])
    safe = False
    if (min(differences) > 0 and max(differences) < 4) or (max(differences) < 0 and min(differences) > -4):
        safe = True
    return safe

def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    reports = read_file(filename)
    count_safe = 0
    levels = []
    for report in reports:
        levels = list(map(int, report.split()))
        safe = check_safe(levels)
        if safe:
            count_safe += 1
    print(f"{DAY} Part A: {count_safe}")

def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    reports = read_file(filename)
    count_safe = 0
    levels = []
    for report in reports:
        levels = list(map(int, report.split()))
        safe = check_safe(levels)
        if not safe:
            for i, ele in enumerate(levels):
                new_levels = levels.copy()
                del new_levels[i]
                safe = check_safe(new_levels)
                if safe:
                    break
        if safe:
            count_safe += 1
    print(f"{DAY} Part B: {count_safe}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
