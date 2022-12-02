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


# Part 1
elf_most_calories = sorted(elf_calories, reverse=True, key=lambda i:i[1])[0]
print(f'The elf with the most calories is the {elf_most_calories[0]}th elf which has {elf_most_calories[1]} calories.')

#Part 2
top_three_calories = sorted(elf_calories, reverse=True, key=lambda i:i[1])[0:3]
print(top_three_calories)
print(f'The top three elves with the most calories are the {top_three_calories[0][0]}th, {top_three_calories[1][0]}th and {top_three_calories[2][0]}th elf which have {sum(amount for index,amount in top_three_calories)} calories combined.')