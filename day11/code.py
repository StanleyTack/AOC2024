from collections import Counter
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
    result = []
    for stone in stones:
        result.extend([1] if stone == 0 else 
                        list(split_even_len_digits(stone)) if len(str(stone)) & 1 == 0 else 
                        [stone * 2024])
    return result

def process_blink_counter(stone_counts):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] += count
        elif is_even_length(stone):
            first, second = split_even_len_digits_optimized(stone)
            new_counts[first] += count
            new_counts[second] += count
        else:
            new_stone = stone * 2024
            new_counts[new_stone] += count
    return new_counts

def get_digit_count(number):
    if number == 0:
        return 1
    count = 0
    n = abs(number)
    while n:
        n //= 10
        count += 1
    return count

def is_even_length(number):
    return get_digit_count(number) % 2 == 0

def split_even_len_digits_optimized(number):
    # Split number into two equal halves without using string conversion
    n = abs(number)
    digits = 0
    temp = n
    while temp:
        temp //= 10
        digits += 1
    
    half = digits // 2
    divisor = 10 ** half
    first = n // divisor
    second = n % divisor
    
    # Reapply the sign if necessary
    if number < 0:
        first = -first
    
    return first, second

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
    filename = 'sample2.txt'
    filename = f'../inputs/{DAY}_input.txt'
    line = read_file(filename)
    # Split line into numbers
    stones = get_nums_from_line(line)
    print(f"Start stones: {stones}")
    
    # Initialize Counter with initial stones
    stone_counts = Counter(stones)
    
    blinks = 75
    for blink in range(blinks):
        stone_counts = process_blink_counter(stone_counts)
        if blink % 10 == 0 or blink == blinks - 1:  # Print progress every 10 blinks
            print(f"Blink {blink + 1}: {sum(stone_counts.values())} stones")
    
    num_stones = sum(stone_counts.values())
    print(f"{DAY} Part B: {num_stones}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
