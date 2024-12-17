DAY = 'day_10'
from copy import deepcopy

def read_file(filename):
    """Reads the contents of a file and returns it as a list of lines."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def create_grid(lines):
    grid = [[int(char) for char in line.strip()] for line in lines]
    for line in grid:
        print(line)
    print("\n")
    return grid

def get_trailhead_peak_coords(grid):
    trailhead_coords = []
    peak_coords = []
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[x][y] == 0:
                trailhead_coords.append((x,y))
            if grid[x][y] == 9:
                peak_coords.append((x,y))
    print(f"Trailheads: {trailhead_coords}")
    print(f"Peaks: {peak_coords}")
    return trailhead_coords, peak_coords


def find_all_paths(grid):
    """
    Finds all paths in the grid that start at a cell with value 0 and end at a cell with value 9.
    Each step in the path must move up, down, left, or right, and the value must increase by exactly 1.
    
    Parameters:
        grid (List[List[int]]): 2D grid represented as a list of lists containing integers.
    
    Returns:
        List[List[Tuple[int, int]]]: A list of paths, where each path is a list of (x, y) coordinates.
    """
    from copy import deepcopy

    # Dimensions of the grid
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Helper function to find all coordinates with a specific value
    def find_coordinates(value):
        coordinates = []
        for y in range(num_rows):
            for x in range(num_cols):
                if grid[y][x] == value:
                    coordinates.append((x, y))
        return coordinates

    # Helper function to get valid neighbors (up, down, left, right)
    def get_neighbors(x, y):
        neighbors = []
        directions = [("up", (0, -1)),
                      ("down", (0, 1)),
                      ("left", (-1, 0)),
                      ("right", (1, 0))]
        
        for direction, (dx, dy) in directions:
            new_x = x + dx
            new_y = y + dy
            # Check if the new coordinates are within grid boundaries
            if 0 <= new_x < num_cols and 0 <= new_y < num_rows:
                neighbors.append((new_x, new_y))
        return neighbors

    # Recursive DFS function to find all paths from current cell to any peak (9)
    def dfs(current_x, current_y, path, paths):
        current_value = grid[current_y][current_x]
        
        # If current cell is a peak, add the path to paths
        if current_value == 9:
            paths.append(deepcopy(path))
            return
        
        # Explore all valid neighbors
        for neighbor_x, neighbor_y in get_neighbors(current_x, current_y):
            neighbor_value = grid[neighbor_y][neighbor_x]
            # Check if the neighbor's value is exactly 1 greater
            if neighbor_value == current_value + 1:
                # Append the neighbor to the current path
                path.append((neighbor_x, neighbor_y))
                # Continue DFS from the neighbor
                dfs(neighbor_x, neighbor_y, path, paths)
                # Backtrack: remove the neighbor from the current path
                path.pop()

    # Find all trailheads (cells with value 0)
    trailheads = find_coordinates(0)
    
    # Initialize a list to hold all valid paths
    all_paths = []
    
    # Iterate over each trailhead and perform DFS to find all paths to peaks
    for start_x, start_y in trailheads:
        initial_path = [(start_x, start_y)]
        dfs(start_x, start_y, initial_path, all_paths)
    
    # Optional: Print the paths
    for idx, path in enumerate(all_paths, start=1):
        print(f"Path {idx}: {path}")
    
    return all_paths


def count_unique_peaks(paths):
    peaks_set = set()
    for path in paths:
        end_point = path[-1]
        peaks_set.add(end_point)    
    return len(peaks_set)

def count_unique_peaks_per_start(paths):
    """
    Processes a list of paths to count the number of unique peaks each starting point can reach.
    Each end point (peak) is only counted once per starting point, regardless of the number of paths connecting them.
    
    Parameters:
        paths (List[List[Tuple[int, int]]]): List of paths, where each path is a list of (x, y) coordinates.
    
    Returns:
        Dict[Tuple[int, int], int]: A dictionary mapping each starting point to the number of unique peaks it can reach.
    """
    from collections import defaultdict

    # Dictionary to map start points to a set of unique peaks
    start_to_peaks = defaultdict(set)

    for path in paths:
        if not path:
            continue  # Skip empty paths
        
        start_point = path[0]
        end_point = path[-1]
        
        # Add the end_point to the set of peaks for the start_point
        start_to_peaks[start_point].add(end_point)
    
    # Convert the sets to counts
    start_to_peak_counts = {start: len(peaks) for start, peaks in start_to_peaks.items()}
    return start_to_peak_counts

def sum_trail_score(trailhead_scores):
    total_sum = 0
    for start_point, peak_count in trailhead_scores.items():
        total_sum += peak_count
        print(f"Start Point {start_point}: {peak_count} unique peak(s)")
    return total_sum


def part_a():
    filename = 'sample.txt'
    filename = 'sample2.txt'
    filename = 'sample3.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    grid = create_grid(lines)
    # get coords of all possible trailheads and peaks from the grid
    trailhead_coords, peak_coords = get_trailhead_peak_coords(grid)
    # find all possible paths from trailhead to peak. 
    paths = find_all_paths(grid)
    trailhead_scores = count_unique_peaks_per_start(paths)
    trail_sum = sum_trail_score(trailhead_scores)
    print(f"{DAY} Part A: {trail_sum}")

def part_b():
    # filename = 'sample.txt'
    # filename = 'sample2.txt'
    # filename = 'sample3.txt'
    filename = f'../inputs/{DAY}_input.txt'
    lines = read_file(filename)
    grid = create_grid(lines)
    # get coords of all possible trailheads and peaks from the grid
    trailhead_coords, peak_coords = get_trailhead_peak_coords(grid)
    # find all possible paths from trailhead to peak. 
    paths = find_all_paths(grid)
    trail_rating_sum = len(paths)
    print(f"{DAY} Part B: {trail_rating_sum}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
