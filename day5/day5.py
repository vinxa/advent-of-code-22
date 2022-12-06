import os, re

def top_crates(dic):
    # Print out top item in each column
    dic = sorted(dic.items(), key=lambda x:x[0])
    for i in dic:
        print(i[1][0], end='')

input = 'input.txt'
start_file = 'starting_arrangement.txt'

crates1={}
crates2={}

# Parse the start file and create dictionary 'crates' to store the crates in each column

with open(os.path.join(os.path.dirname(__file__),start_file)) as f:
    textList = []
    start = f.readlines()
    for line in start:
        textList.append([x.strip() for x in line])

for row in textList:
    for ind,col in enumerate(row):
        if col != '' and not col in '[]1234567890':
            ind = int(((ind-1)/4)+1) # Maps the letters to the column number.
            if ind in crates1.keys():
                crates1[ind].append(col)
                crates2[ind].append(col)
            else:
                crates1[ind] = [col]
                crates2[ind] = [col]

# Process instructions from input.txt
with open(os.path.join(os.path.dirname(__file__),input)) as f:
    instructions = [x.strip('\n') for x in f.readlines()]

for instruct in instructions:
    print(instruct)
    nums = re.findall(r'\d+', instruct)
    quantity = int(nums[0])
    source = int(nums[1])
    dest = int(nums[2])

    # Part 1
    for i in range(quantity):
        x = crates1[source][0]
        crates1[source].pop(0)
        crates1[dest].insert(0,x)
    # Part 2
    working_list = []
    for i in range(quantity):
        x = crates2[source][0]
        crates2[source].pop(0)
        working_list.append(x)
    crates2[dest] = working_list + crates2[dest]
        

# Print out top item in each column
top_crates(crates1)
print('')
top_crates(crates2)