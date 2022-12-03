import os
input = 'input.txt'

dupes = []
group_badges = []

def find_common_item(s1, s2, s3):
    for i in ''.join(set(s1)):
        if i in s2 and i in s3:
            return i
    
def find_priorities_sum(li):
    sum_var = 0
    for item in li:
        print(item)
        if item.islower():
            sum_var += ord(item) - 96
        else:
            sum_var += ord(item) - 38
    return sum_var

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    for index, rucksack in enumerate(lines):
        c1 = ''.join(set(rucksack[:len(rucksack)//2]))
        c2 = rucksack[len(rucksack)//2:]
        for i in c1:
            if i in c2:
                dupes.append(i)
        # Part 2
        if (index+1) % 3 == 0:
            group_badges.append(find_common_item(rucksack, lines[index-1],lines[index-2]))

rucksack_priority_sum = find_priorities_sum(dupes)  # Part 1
group_priority_sum = find_priorities_sum(group_badges)  # Part 2

print(f'Part 1: {rucksack_priority_sum}, Part 2:  {group_priority_sum}')
