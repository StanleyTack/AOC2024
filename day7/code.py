import re
import itertools
import operator

DAY = 'day_7'


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def split_lines(lines):
    line_numbers = []
    for line in lines:
        nums = list(map(int, re.findall(r'\d+', line)))
        line_numbers.append(nums)
    return line_numbers


def evaluate_line(lines):
    def concat(a, b):
        # Custom || operator to concatenate digits
        return int(str(a) + str(b))

    ops = {
        '+': operator.add,
        '*': operator.mul,
        '||':concat
    }
    sum_found = 0

    for line in lines:
        target_result = line[0]
        nums = line[1:]  # Order remains the same
        
        # Generate combinations of operations
        operations = list(itertools.product(ops.keys(), repeat=len(nums) - 1))

        for ops_combo in operations:
            try:
                # Start with the first number
                result = nums[0]
                
                # Apply operations in sequence
                for i, op in enumerate(ops_combo):
                    result = ops[op](result, nums[i + 1])
                
                # Check if the result matches the target
                if result == target_result:
                    sum_found += target_result
                    print(f"{target_result} - match found")
                    break  # No need to check further combinations
            except ZeroDivisionError:
                # Skip invalid operations
                continue

    return sum_found

    
def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    line_numbers = split_lines(lines)
    sum_found = evaluate_line(line_numbers)
    print(f"{DAY} Part A: {sum_found}")

def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    reports = read_file(filename)
    count_safe = 0
    
    print(f"{DAY} Part B: {count_safe}")

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
