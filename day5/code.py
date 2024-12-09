from collections import defaultdict, deque

DAY = 'day_5'

def read_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def read_file_sections(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Split into sections by the first occurrence of two newlines
    sections = content.split('\n\n', 1)
    
    # Split each section into individual lines
    section_1 = sections[0].splitlines()
    section_2 = sections[1].splitlines() if len(sections) > 1 else []
    
    section_1_list = []
    for li in section_1:
        li = list(li.split('|'))
        section_1_list.append(li)
    
    section_2_list = []
    for li in section_2:
        li = list(li.split(','))
        section_2_list.append(li)

    # print(section_2_list)
    return section_1_list, section_2_list

def check_rules(page, next_page, rules):
    for rule in rules:
        if page == rule[1] and next_page == rule[0]:
            # print(page, next_page)
            return False
    return True


def get_middle_element(pages_list):
    return pages_list[len(pages_list) // 2]


def find_correct_order(pairs):
    # Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize graph and in-degree counts
    nodes = set()
    for a, b in pairs:
        graph[a].append(b)
        in_degree[b] += 1
        in_degree[a]  # Ensure all nodes are present in the in-degree dictionary
        nodes.update([a, b])
    # Find nodes with 0 in-degree to start the process
    queue = deque([node for node in nodes if in_degree[node] == 0])
    result = []
    # Perform a topological sort
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if we used all nodes (to detect cycles)
    if len(result) != len(nodes):
        raise ValueError("Cycle detected in input pairs, ordering not possible.")
    return result


def reorder_list_based_on_rules(original_list, ordered_rules):
    # Extract items from the original list that are in the ordered rules
    filtered_items = [item for item in original_list if item in ordered_rules]
    # Sort those items according to the order specified in ordered_rules
    filtered_items.sort(key=lambda x: ordered_rules.index(x))
    # Reconstruct the list with new ordering for filtered items and original order for others
    result = []
    filtered_index = 0

    for item in original_list:
        if item in ordered_rules:
            # Add the item from filtered list in the correct sorted order
            result.append(filtered_items[filtered_index])
            filtered_index += 1
        else:
            # Add any item that is not in the rules, maintaining its original position
            result.append(item)
    return result

def find_relevant_rules(update, rules):
    relevant_rules = []
    for pair in rules:
        if pair[0] in update and pair[1] in update:
            relevant_rules.append(pair)
    return relevant_rules


def part_a():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    rules, updates = read_file_sections(filename)
    middle_sum = 0
    for update in updates:
        valid = True
        for p in range(len(update)-1):
            for q in range(p+1, len(update)):
                valid = check_rules(update[p], update[q], rules)
                if not valid:
                    break
            if not valid:
                break
        if valid:
            middle_sum += int(get_middle_element(update))
    # print(updates)
    print(f"{DAY} Part A: {middle_sum}")

def part_b():
    # filename = 'sample.txt'
    filename = f'../inputs/{DAY}_input.txt'
    rules, updates = read_file_sections(filename)
    middle_sum = 0
    for update in updates:
        relevant_rules = find_relevant_rules(update, rules)
        ordered_rules = find_correct_order(relevant_rules)
        print(f'Relevant rules: {ordered_rules}')
        valid = True
        for p in range(len(update)-1):
            for q in range(p+1, len(update)):
                valid = check_rules(update[p], update[q], rules)
                if not valid:
                    break
            if not valid:
                # print(update)
                # print()
                break
        if not valid:
            new_update = reorder_list_based_on_rules(update, ordered_rules)
            middle_sum += int(get_middle_element(new_update))
    print(f"{DAY} Part B: {middle_sum}")
    pass

def main():
    # part_a()
    part_b()

if __name__ == "__main__":
    main()
