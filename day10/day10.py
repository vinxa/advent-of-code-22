import os
from textwrap import wrap

# Read input
input = "input.txt"

with open(os.path.join(os.path.dirname(__file__), input)) as f:
    input = [x.strip() for x in f.readlines()]

def checkCycles(cycle, x): # Part 1
    if ((cycle+1) % 20 == 0 and (cycle+1) % 40 != 0):
        interest.append((cycle+1)*x)

def drawCRT(cycle, x):  # Part 2
    if cycle > 39:
        cycle = cycle % 40
    if cycle >= x-1 and cycle <= x+1:
        return '█'
    else:
        return '.'

cycle = 0
x = 1
interest = []  # Part 1 interested signal strengths
screen_data = ''  # Part 2 screen pixels

for i in input:
    if 'addx' in i:
        i = i.replace('addx','')
        screen_data += drawCRT(cycle, x)
        cycle += 1
        checkCycles(cycle, x)
        screen_data += drawCRT(cycle, x)
        cycle += 1
        x += int(i)
    else:
        screen_data += drawCRT(cycle, x)
        cycle += 1
    checkCycles(cycle, x)

print(interest)
print(sum(interest))
print('---')

for x in wrap(screen_data, 40):
    print(x)