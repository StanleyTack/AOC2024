import re

DAY = 'day_3'

def read_file(filename):
    # Reads the contents of a file and returns it as a list of lines.
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


def extract_mul_numbers(s):
    # Match the pattern `mul(a, b)` where `a` and `b` are integers
    matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    return [(int(x), int(y)) for x, y in matches]


def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    pairs = []
    for line in lines:
        new_pairs = extract_mul_numbers(line)
        pairs.extend(new_pairs)
    result = sum([x * y for x, y in pairs])
    print(f"{DAY} Part A: {result}")

def part_b():
    filename = 'sample.txt'
    # filename = f'../inputs/{DAY}_input.txt'
    reports = read_file(filename)
    count_safe = 0
    levels = []
    print(f"{DAY} Part B: {count_safe}")

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
