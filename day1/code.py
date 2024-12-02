def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def part_a():
    # filename = 'sample.txt'
    filename = 'input.txt'
    lines = read_file(filename)
    list1 = []
    list2 = []
    for line in lines:
        chars = line.split()
        list1.append(int(chars[0]))
        list2.append(int(chars[1]))
    list1.sort(reverse=False)
    list2.sort(reverse=False)
    distances = []
    for i, num in enumerate(list1):
        distance = abs(num - list2[i])
        distances.append(distance)
    print(sum(distances))
    # pass

def part_b():
    # filename = 'sample.txt'
    # filename = 'input.txt'
    pass

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
