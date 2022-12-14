import os

# Read input
input = "input.txt"
with open(os.path.join(os.path.dirname(__file__), input)) as f:
    input = [x.strip() for x in f.readlines()]

print(input)

#class Monkey:
#    def __init__(self, num, items, test, true, false):
#        self.name
