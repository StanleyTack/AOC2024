DAY = 'day_2'

def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def checks(levels):
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
        safe = checks(levels)
        if safe:
            count_safe += 1
    print(f"{DAY} Part A: {count_safe}")

def part_b():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    list1 = []
    list2 = []
    for line in lines:
        chars = line.split()
        list1.append(int(chars[0]))
        list2.append(int(chars[1]))
    similarities = []
    counted = set()
    for num1 in list1:
        counted.add(num1)
        num_count = 0
        for num2 in list2:
            if num2 == num1:
                num_count += 1
        similarities.append((num1, num_count))
    sim_scores = []
    for pair in similarities:
        sim_score = pair[0] * pair[1]
        sim_scores.append(sim_score)
    print(f"{DAY} Part B: {sum(sim_scores)}")
    # pass

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
