DAY = 'day_13'

import re
from math import gcd
from tqdm import tqdm


def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def parse_sections(lines):
    """Parses the lines into a list of tuples for each section."""
    sections = []
    current_section = []

    for line in lines:
        line = line.strip()
        if line:
            current_section.append(line)
        else:
            if current_section:
                sections.append(current_section)
                current_section = []

    if current_section:  # Add the last section if no trailing blank line
        sections.append(current_section)

    return sections

def process_file(filename, partb=False):
    """Processes the file and returns the parsed data as a list of tuples."""
    lines = read_file(filename)
    sections = parse_sections(lines)
    result = [extract_coordinates(section, partb) for section in sections]
    return result

def extract_coordinates(section, partb):
    """Extracts coordinates from a section and returns them as a tuple."""
    coordinates = []
    correction = 10000000000000
    for line in section:
        if line.startswith("Button A"):
            match = re.search(r"X\+([0-9]+), Y\+([0-9]+)", line)
            if match:
                coordinates.append((int(match.group(1)), int(match.group(2))))
        elif line.startswith("Button B"):
            match = re.search(r"X\+([0-9]+), Y\+([0-9]+)", line)
            if match:
                coordinates.append((int(match.group(1)), int(match.group(2))))
        elif line.startswith("Prize"):
            match = re.search(r"X=([0-9]+), Y=([0-9]+)", line)
            if match:
                if partb:
                    coordinates.append((int(match.group(1))+correction, int(match.group(2))+correction))
                else:
                    coordinates.append((int(match.group(1)), int(match.group(2))))
    return coordinates

def find_min_factors(machine):
    """
    Finds the values of (num_a, num_b) such that:
    num_a * ax + num_b * bx = px
    num_a * ay + num_b * by = py
    """
    (ax, ay), (bx, by), (px, py) = machine
    # Calculate the determinant
    determinant = ax * by - ay * bx

    # Check if determinant is zero (no unique solution)
    if determinant == 0:
        return None

    # Solve using Cramer's rule
    num_a = (px * by - py * bx) / determinant
    num_b = (ax * py - ay * px) / determinant

    # Check if num_a and num_b are integers
    if num_a.is_integer() and num_b.is_integer():
        return int(num_a), int(num_b)

    return None

def validate_prize(machine, result):
    (ax, ay), (bx, by), (px, py) = machine
    if ax * result[0] + bx * result[1] == px and ay * result[0] + by * result[1] == py:
        return True
    else:
        return False

def calculate_costs(machine_coords):
    a_cost = 3
    b_cost = 1
    total_cost = 0
    for m, machine in enumerate(tqdm(machine_coords, desc="Processing Machines")):
        x_result = find_min_factors(machine)
        if x_result and validate_prize(machine, x_result):
            machine_cost = a_cost * x_result[0] + b_cost * x_result[1]
            total_cost += machine_cost
            # print(f"{m} - {machine_cost}")
        else: total_cost += 0
    return total_cost
    

def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/input_{DAY}.txt'
    machine_coords = process_file(filename)
    total_cost = calculate_costs(machine_coords)
    print(f"{DAY} Part A: {total_cost}")

def part_b():
    filename = 'sample.txt'
    filename = f'../inputs/input_{DAY}.txt'
    machine_coords = process_file(filename, partb=True)
    total_cost = calculate_costs(machine_coords)
    print(f"{DAY} Part B: {total_cost}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
