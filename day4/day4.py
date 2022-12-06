import os
input = 'input.txt'
contain_counter = 0
overlap_counter = 0

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    for pair in lines:
        elf1_min = int(pair.split(',')[0].split('-')[0])
        elf1_max = int(pair.split(',')[0].split('-')[1])
        elf2_min = int(pair.split(',')[1].split('-')[0])
        elf2_max = int(pair.split(',')[1].split('-')[1])

        if elf1_min >= elf2_min and elf1_max <= elf2_max:
            contain_counter += 1  # Part 1
            overlap_counter += 1  # Part 2
        elif elf2_min >= elf1_min and elf2_max <= elf1_max:
            contain_counter += 1  # Part 1
            overlap_counter += 1  # Part 2
        elif elf1_min in range(elf2_min, elf2_max+1) or elf1_max in range(elf2_min, elf2_max+1):
            overlap_counter += 1  # Part 2
        else:
            pass



print(f'Part 1: {contain_counter}')
print(f'Part 2: {overlap_counter}')