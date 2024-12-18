DAY = 'day_11'


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def get_nums_from_line(line):
    numbers = [int(_) for _ in line[0].split()]
    return numbers

def split_even_len_digits(number):
    first = 0
    second = 0
    num_str = str(number)
    half = len(num_str) // 2
    first_str = num_str[0:half]
    second_str = num_str[half:len(num_str)]
    first = int(first_str)
    second = int(second_str)
    return first, second

def process_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            first, second = split_even_len_digits(stone)
            new_stones.append(first)
            new_stones.append(second)
        else:
            new_stones.append(stone * 2024)
    return new_stones


def part_a():
    filename = 'sample.txt'
    filename = 'sample2.txt'
    filename = f'../inputs/{DAY}_input.txt'
    line = read_file(filename)
    # split line into numbers
    stones = get_nums_from_line(line)
    print(f"Start stones: {stones}")

    blinks = 25
    for _ in range(blinks):
        stones = process_blink(stones)
        print(f"Blink {_}")
    num_stones = len(stones)
    print(f"{DAY} Part A: {num_stones}")



def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    count_safe = 0   
    print(f"{DAY} Part B: {count_safe}")

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
