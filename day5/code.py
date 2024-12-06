import re

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

    return section_1_list, section_2_list

def check_rules(page, next_page, rules):
    for rule in rules:
        if page == rule[1] and next_page == rule[0]:
            print(page, next_page)
            return False
    return True

def get_middle_element(pages_list):
    return pages_list[len(pages_list) // 2]

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
    lines = read_file(filename)
    mas_count = 0
    pass

def main():
    part_a()
    # part_b()

if __name__ == "__main__":
    main()
