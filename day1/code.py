DAY = 'day_1'

def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    list1 = []
    list2 = []
    for line in lines:
        chars = line.split()
        list1.append(int(chars[0]))
        list2.append(int(chars[1]))
    list1.sort(reverse=False)
    list2.sort(reverse=False)
    distances = []
    for i, num in enumerate(list1):
        distance = abs(num - list2[i])
        distances.append(distance)
    print(f"Day 1 Part A: {sum(distances)}")

    # pass

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
    print(f"Day 1 Part B: {sum(sim_scores)}")
    # pass

def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
