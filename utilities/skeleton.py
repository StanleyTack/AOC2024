DAY = 'day_2'


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    count_safe = 0
    print(f"{DAY} Part A: {count_safe}")

def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    count_safe = 0   
    print(f"{DAY} Part B: {count_safe}")

def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
