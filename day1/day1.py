import os

elf_calories = []
input = 'input.txt'

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    elf_sum = 0
    for line in f:
        if line != '\n':
            elf_sum += int(line)
        else:
            elf_calories.append(elf_sum)
            elf_sum = 0

elf_calories = [(i+1, x) for i, x in enumerate(elf_calories)]
elf_calories = sorted(elf_calories, reverse=True, key=lambda i:i[1])[0]

print(f'The elf with the most calories is the {elf_calories[0]}th elf which has {elf_calories[1]} calories.')
