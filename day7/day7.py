import os, re
from functools import reduce
import operator

def construct_dictionary(input):
    # create the directory and set active path variables
    directory = {}
    activeDict = directory
    currentPath = []

    # Process input
    while len(input) > 0:
        line = input[0]
        if line.startswith('$ cd'):
            folder = line.replace('$ cd ', '')
            if folder == '..':
                currentPath.pop()
                activeDict = reduce(operator.getitem, currentPath, directory)
            
            elif folder in activeDict.keys():
                activeDict = activeDict[folder]
                currentPath.append(folder)
            
            else:
                activeDict[folder] = {}
                activeDict = activeDict[folder]
                currentPath.append(folder)
            
        elif line.startswith('dir'):
            folder = line.replace('dir ', '')
            activeDict[folder] = {}
        
        elif re.search('\d+ ', line):
            activeDict[line.split(' ')[1]] = int(line.split(' ')[0])

        input.pop(0)

    return directory

def sum_dirs(directory, name='root'):
    x = 0
    for key, value in directory.items():
        if type(value) == int:
            x += value
        elif type(value) == dict:
            x += sum_dirs(value, key)
            
    directory_list.append([name, x])
    return x
    
# Read input
input = 'input.txt'

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    input = f.read()

# Build the paths in python dictionary
directory = construct_dictionary(input.split('\n'))

# Find directories with total size under 100,000
directory_list = []
used_space = sum_dirs(directory)

# Part 1 - Sum of directories < 1000
total_under_100k = 0
for x in directory_list:
    if x[1] <= 100000:
        total_under_100k += x[1]
print(f'Sum of directories < 1000: {total_under_100k}')

# Part 2 - Smallest directory that gets us to 30000000 free space
to_free = 30000000 - (70000000 - used_space)
print(f'Currently have {70000000 - used_space} free space, need to free up {to_free} more space')

candidates = sorted([x for x in directory_list if x[1] >= to_free],key=lambda x: x[1])
print(f'The top candidate is folder {candidates[0][0]} which takes up {candidates[0][1]} space.')