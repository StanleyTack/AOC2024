import re

DAY = 'day_4'

def read_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def find_xmas(line):
    matches = re.findall(r"XMAS", line)
    return len(matches)

def find_xmas_reverse(line):
    reversed_line = line[::-1]
    matches = re.findall(r"XMAS", reversed_line)
    return len(matches)

def shift_columns_up(lines):
    # Split the input strings into individual characters to form a 2D list
    matrix = [list(line) for line in lines]
    
    # Transpose the matrix (columns become rows)
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    # Create a new grid where each column is shifted up by one
    shifted_lines = []
    top_half = [[] for _ in range(len(transposed))]  # Initialize rows for the disappearing characters

    for i in range(len(transposed)):
        # Shift the column up by `i` positions
        removed = transposed[i][:i]  # Characters that "disappear"
        shifted_column = transposed[i][i:] + [' '] * i  # Add spaces for disappearing characters

        # Collect the removed characters for the top half
        for j, char in enumerate(removed):
            while len(top_half) <= j:
                top_half.append([])  # Ensure enough rows
            top_half[j].append(char)  # Place the character in the correct position

        # Add this shifted column to the output
        for j, char in enumerate(shifted_column):
            if len(shifted_lines) <= j:
                shifted_lines.append([' '] * len(transposed))  # Start with spaces
            shifted_lines[j][i] = char

    # Rotate the top half 90 degrees clockwise
    top_half_rotated = []
    max_length = max(len(row) for row in top_half)  # Find the widest row
    for i in range(max_length):
        new_row = [row[i] if i < len(row) else ' ' for row in reversed(top_half)]
        top_half_rotated.append(''.join(new_row).rstrip())

    # Convert the bottom half into strings
    shifted_lines = [''.join(row).rstrip() for row in shifted_lines]

    # Combine the rotated top half and the shifted lines
    final_output = top_half_rotated + shifted_lines
    # for line in final_output:
    #     print(line)
    return final_output

def shift_columns_down(lines):
    # Split the input strings into individual characters to form a 2D list
    matrix = [list(line) for line in lines]
    
    # Transpose the matrix (columns become rows)
    transposed = [[row[i] if i < len(row) else ' ' for row in matrix] for i in range(len(matrix[0]))]

    # Create a new grid where each column is shifted down by one position
    shifted_lines = []
    bottom_half = [[] for _ in range(len(transposed))]  # Initialize rows for the overflowing characters

    for i in range(len(transposed)):
        # Shift the column down by `i` positions
        overflow = transposed[i][-i:] if i > 0 else []  # Characters that overflow
        shifted_column = [' '] * i + transposed[i][:-i] if i > 0 else transposed[i]  # Add spaces for overflow

        # Collect the overflow characters for the bottom half
        for j, char in enumerate(overflow):
            while len(bottom_half) <= j:
                bottom_half.append([])  # Ensure enough rows
            bottom_half[j].append(char)  # Place the character in the correct position

        # Add this shifted column to the output
        for j, char in enumerate(shifted_column):
            if len(shifted_lines) <= j:
                shifted_lines.append([' '] * len(transposed))  # Start with spaces
            shifted_lines[j][i] = char

    # Convert list to strings
    shifted_lines = [''.join(row).rstrip() for row in shifted_lines]
    bottom_half = [''.join(row).rstrip() for row in bottom_half]

    final_output = shifted_lines + bottom_half
    # for line in final_output:
    #     print(line)
    return final_output


def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    xmas_count = 0
    # check right and left
    for line in lines:
        xmas_count += find_xmas(line)
        xmas_count += find_xmas_reverse(line)
    # check up and down
    transposed_lines = [[row[i] for row in lines] for i in range(len(lines[0]))]
    transposed_lines_string = [''.join(row) for row in transposed_lines]
    for line in transposed_lines_string:
        xmas_count += find_xmas(line)
        xmas_count += find_xmas_reverse(line)
    # check diagonal /
    shift_up_lines = shift_columns_up(lines)
    for line in shift_up_lines:
        xmas_count += find_xmas(line)
        xmas_count += find_xmas_reverse(line)
    # check diagonal /
    shift_down_lines = shift_columns_down(lines)
    for line in shift_down_lines:
        xmas_count += find_xmas(line)
        xmas_count += find_xmas_reverse(line)
    print(f"{DAY} Part A: {xmas_count}")

def part_b():
    # filename = 'sample.txt'
    # filename = f'../inputs/{DAY}_input.txt'
    # lines = read_file(filename)
    # pairs = []
    # single_line = ''
    # for line in lines:
    #     single_line += line
    # data = find_patterns_and_positions(single_line)
    # # print(data['do'])
    # # print(data['dont'])
    # print(f"\nDo: \n{data['do']}")
    # print(f"\nDont: \n{data['dont']}")
    # # print(f"\nAll pairs: \n{data['mul']}")
    # pairs.extend(filter_mul_positions(data))
    # print(f"\nIncluded pairs: \n{pairs}")
    # result = sum([x * y for x, y in pairs])
    # print(f"{DAY} Part B: {result}")
    pass

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
