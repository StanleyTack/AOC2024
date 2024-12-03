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

def find_patterns_and_positions(s):
    # Find all `mul(x,y)` patterns and their positions
    mul_matches = re.finditer(r"mul\((\d+),(\d+)\)", s)
    mul_results = [(match.start(), int(match.group(1)), int(match.group(2))) for match in mul_matches]
    do_positions = [match.start() for match in re.finditer(r"do\(\)", s)]
    dont_positions = [match.start() for match in re.finditer(r"don't\(\)", s)]
    return {
        "mul": mul_results,
        "do": [0]+do_positions,
        "dont": dont_positions,
    }

def generate_brackets(do_positions, dont_positions):
    # Combine and sort the do and don't positions with labels
    events = sorted([(pos, "do") for pos in do_positions] + [(pos, "dont") for pos in dont_positions])
    brackets = []
    start_pos = None
    for pos, label in events:
        if label == "do" and start_pos is None:
            start_pos = pos
        elif label == "dont" and start_pos is not None:
            brackets.append((start_pos, pos))
            start_pos = None  # Reset 'start-pos' after pairing
    # Add an open-ended range for any leftover 'do' without a 'dont'
    if start_pos is not None:
        brackets.append((start_pos, float('inf')))
    return brackets

def filter_mul_positions(data):
    mul = data['mul']
    do_positions = sorted(data['do'])
    dont_positions = sorted(data['dont'])
    brackets = generate_brackets(do_positions, dont_positions)
    print(f"\nBrackets \n{brackets}")
    # Define the inclusion rule: mul should be between `do` and the next `dont`
    included_mul = []
    for position, x, y in mul:
        # Check if the position is within any bracket
        if any(start <= position < end for start, end in brackets):
            included_mul.append((x, y))
    return included_mul


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
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    pairs = []
    single_line = ''
    for line in lines:
        single_line += line
    data = find_patterns_and_positions(single_line)
    # print(data['do'])
    # print(data['dont'])
    print(f"\nDo: \n{data['do']}")
    print(f"\nDont: \n{data['dont']}")
    # print(f"\nAll pairs: \n{data['mul']}")
    pairs.extend(filter_mul_positions(data))
    print(f"\nIncluded pairs: \n{pairs}")
    result = sum([x * y for x, y in pairs])
    print(f"{DAY} Part B: {result}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
