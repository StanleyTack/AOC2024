from collections import deque

DAY = 'day_12'


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def get_neighbors(x, y, max_x, max_y):
    """Returns the valid neighboring coordinates (up, down, left, right)."""
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < max_x - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < max_y - 1:
        neighbors.append((x, y + 1))
    return neighbors

def calculate_perimeter(region, grid, max_x, max_y):
    """Calculates the perimeter of a given region."""
    perimeter = 0
    for (x, y) in region:
        # Check all four sides
        neighbors = get_neighbors(x, y, max_x, max_y)
        for nx, ny in neighbors:
            if grid[nx][ny] != grid[x][y]:
                perimeter += 1
        # Also, check for boundary edges
        if x == 0:
            perimeter += 1
        if x == max_x - 1:
            perimeter += 1
        if y == 0:
            perimeter += 1
        if y == max_y - 1:
            perimeter += 1
    # To avoid double-counting boundary edges, we adjust perimeter
    # Each boundary side was added twice in the above loop
    # So, divide the total perimeter by 2
    # However, since we only add when adjacent is different, we don't need to divide
    # So, we can return the total perimeter as is
    return perimeter

def find_regions(grid):
    """Finds all regions in the grid and returns a list of regions with their plant type."""
    regions = []
    max_x = len(grid)
    max_y = len(grid[0]) if max_x > 0 else 0
    visited = [[False for _ in range(max_y)] for _ in range(max_x)]
    
    for x in range(max_x):
        for y in range(max_y):
            if not visited[x][y]:
                plant_type = grid[x][y]
                # Perform BFS to find all connected plots of the same plant type
                queue = deque()
                queue.append((x, y))
                visited[x][y] = True
                region = []
                
                while queue:
                    current_x, current_y = queue.popleft()
                    region.append((current_x, current_y))
                    
                    for neighbor in get_neighbors(current_x, current_y, max_x, max_y):
                        nx, ny = neighbor
                        if not visited[nx][ny] and grid[nx][ny] == plant_type:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                
                regions.append({
                    'plant_type': plant_type,
                    'plots': region
                })
    
    return regions

def calculate_total_cost_part_b(regions, grid):
    """Calculates the total fencing cost for all regions using Number of Sides × Area."""
    max_x = len(grid)
    max_y = len(grid[0]) if max_x > 0 else 0
    total_cost = 0
    
    for region in regions:
        plant_type = region['plant_type']
        plots = region['plots']
        area = len(plots)
        number_of_sides = calculate_number_of_sides(plots, grid, max_x, max_y)
        cost = number_of_sides * area
        total_cost += cost
        print(f"Region {plant_type}: Area = {area}, Number of Sides = {number_of_sides}, Cost = {cost}")
    
    return total_cost


def calculate_number_of_sides(region, grid, max_x, max_y):
    """
    Calculates the total number of sides in a region.
    Each plot has 4 sides. Shared sides between adjacent plots reduce the total count.
    Formula: Number of Sides = 4 * Area - 2 * Number of Adjacent Pairs
    """
    area = len(region)
    adjacent_pairs = 0
    # To avoid double-counting, we'll track processed pairs
    processed = set()
    
    for (x, y) in region:
        for neighbor in get_neighbors(x, y, max_x, max_y):
            nx, ny = neighbor
            if grid[nx][ny] == grid[x][y]:
                if (nx, ny) in region:
                    # Create a sorted tuple to avoid double-counting
                    pair = tuple(sorted(((x, y), (nx, ny))))
                    if pair not in processed:
                        adjacent_pairs += 1
                        processed.add(pair)
    
    number_of_sides = 4 * area - 2 * adjacent_pairs
    return number_of_sides

def calculate_total_cost(regions, grid):
    """Calculates the total fencing cost for all regions."""
    max_x = len(grid)
    max_y = len(grid[0]) if max_x > 0 else 0
    total_cost = 0
    
    for region in regions:
        plant_type = region['plant_type']
        plots = region['plots']
        area = len(plots)
        perimeter = calculate_perimeter(plots, grid, max_x, max_y)
        cost = area * perimeter
        total_cost += cost
        print(f"Region {plant_type}: Area = {area}, Perimeter = {perimeter}, Cost = {cost}")
    
    return total_cost


def part_a():
    filename = 'sample.txt'
    filename = f'../inputs/input_{DAY}.txt'
    lines = read_file(filename)
    grid = [list(line.strip()) for line in lines if line.strip()]
    
    regions = find_regions(grid)
    total_cost = calculate_total_cost(regions, grid)

    print(f"{DAY} Part A: {total_cost}")

def part_b():
    filename = 'sample.txt'  # Replace with your actual filename
    # filename = f'../inputs/input_{DAY}.txt'  # Uncomment and set DAY if needed
    lines = read_file(filename)
    
    # Convert lines into a grid (list of lists)
    grid = [list(line.strip()) for line in lines if line.strip()]
    
    regions = find_regions(grid)
    total_cost = calculate_total_cost_part_b(regions, grid)
 
    print(f"{DAY} Part B: {total_cost}")

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
