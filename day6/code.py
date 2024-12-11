DAY = 'day_6'


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    line_lists = lines_to_list(lines)
    return line_lists

def lines_to_list(lines):
    # store each char of a string as element in list, return list of lists
    return [list(line.strip()) for line in lines]

def find_start_coord(grid):
    for y, line in enumerate(grid):
        for x, ele in enumerate(line):
            if ele == '^':
                # print(f"Start: ({x}, {y})")
                return (x, y)
    return IndexError("No start element found")

def turn_right(patrol_dir):
    patrol_dir += 90
    if patrol_dir == 360:
        patrol_dir = 0
    print(f"Direction {patrol_dir}")
    return patrol_dir

def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    grid = read_file(filename)
    grid_size = len(grid)
    guard_present = True
    guard_position = find_start_coord(grid)
    patrol_dir = 0
    steps = 0
    print(f"gaurd position {guard_position}")
    while guard_present and steps < 5:
        if patrol_dir == 0: # guard moving up
            x = guard_position[0]
            y = guard_position[1]
            for y in range(y, -1, -1):
                ele = grid[y][x]
                print(x, y, ele)
                if ele == '#':
                    guard_position = (x, y+1)
                    print(f"gaurd position {guard_position}")
                    patrol_dir = turn_right(patrol_dir)
                    break
                grid[y][x] = '1'
                if ele == '.' and y == 0:
                    guard_present = False
                    break
        if patrol_dir == 180: # guard moving down
            x = guard_position[0]
            y = guard_position[1]
            for y in range(y, grid_size, 1):
                ele = grid[y][x]
                print(x, y, ele)
                if ele == '#':
                    guard_position = (x, y-1)
                    patrol_dir = turn_right(patrol_dir)
                    break
                grid[y][x] = '1'
                if ele == '.' and y == grid_size-1:
                    guard_present = False
                    break
        if patrol_dir == 90: # guard moving right
            x = guard_position[0]
            y = guard_position[1]
            for x in range(x, grid_size, 1):
                ele = grid[y][x]
                print(x, y, ele)
                if ele == '#':
                    guard_position = (x-1, y)
                    patrol_dir = turn_right(patrol_dir)
                    break
                grid[y][x] = '1'
                if ele == '.' and x == grid_size-1:
                    guard_present = False
                    break
        if patrol_dir == 270: # guard moving left
            x = guard_position[0]
            y = guard_position[1]
            for x in range(x, -1, -1):
                ele = grid[y][x]
                print(x, y, ele)
                if ele == '#':
                    guard_position = (x+1, y)
                    patrol_dir = turn_right(patrol_dir)
                    break
                grid[y][x] = '1'
                if ele == '.' and x == 0:
                    guard_present = False
                    break
    if not guard_present:
        print("Guard departed map")
        position_count = 0
        for line in grid:
            print(line)
            for ele in line:
                if ele == '1':
                    position_count += 1
        print(position_count)
    count_safe = 0
    print(f"{DAY} Part A: {count_safe}")



def part_b():
    filename = 'sample.txt'
    # filename = f'../inputs/{DAY}_input.txt'
    reports = read_file(filename)
    count_safe = 0
    
    print(f"{DAY} Part B: {count_safe}")

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
