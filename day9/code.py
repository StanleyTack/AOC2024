DAY = 'day_9'


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def empty_spaces(line):
    # line = '12345'
    line_with_spaces = []
    is_file = True
    id = 0
    for ele in line:
        file_len = int(ele)
        if is_file:
            file = [str(id)] * file_len
            id += 1
        else:
            file = [str('.')] * file_len
        is_file = not is_file
        line_with_spaces += file
    line_with_spaces_str = ''.join(line_with_spaces)
    count_spaces = line_with_spaces.count('.')
    return line_with_spaces, count_spaces


def reverse_files(line_with_spaces, count_spaces):
    line_without_spaces = [item for item in line_with_spaces if item != '.']
    reversed_line_without_spaces = line_without_spaces[-count_spaces:][::-1]
    return reversed_line_without_spaces

def calc_checksum(line):
    nums = map(int, line)  # Convert all elements to integers
    return sum(i * num for i, num in enumerate(nums))


def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    # lines = ['12345']
    lines = read_file(filename)
    for line in lines:
        line_with_spaces, count_spaces = empty_spaces(line)
        files_to_be_places = reverse_files(line_with_spaces, count_spaces)
        final_file_size = len(line_with_spaces) - count_spaces
        new_line = line_with_spaces[:final_file_size]
        x = 0
        for i, ele in enumerate(new_line):
            if ele == '.':
                new_line[i] = files_to_be_places[x]
                x += 1
        print(new_line)
    checksum = calc_checksum(new_line)
    print(f"{DAY} Part A: {checksum}")

def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    for line in lines:
        line_with_spaces, count_spaces = empty_spaces(line)
        files_to_be_places = reverse_files(line_with_spaces, count_spaces)
        final_file_size = len(line_with_spaces) - count_spaces
        new_line = line_with_spaces[:final_file_size]
        x = 0
        for i, ele in enumerate(new_line):
            if ele == '.':
                new_line[i] = files_to_be_places[x]
                x += 1
        print(new_line)
    checksum = calc_checksum(new_line)
    print(f"{DAY} Part B: {checksum}")

    

if __name__ == "__main__":
    # part_a()
    part_b()
