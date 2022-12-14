import os, math

air = "."
rock = "#"
sand = "o"
source = "+"

# Read input
input = "example.txt"
with open(os.path.join(os.path.dirname(__file__), input)) as f:
    input = [x.strip() for x in f.readlines()]

print(input)
paths = [x.split(" -> ") for x in input]
print('---')
print(paths)
cave = {}
