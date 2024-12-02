def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def part_a():
    filename = 'sample.txt'
    # filename = '../input.txt'
    lines = read_file(filename)
    pass

def part_b():
    # filename = 'sample.txt'
    # filename = '../input.txt'
    pass

def main():
    part_a()
    part_b()

if __name__ == "__main__":
    main()
