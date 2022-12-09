import os
input = 'input.txt'

def findFirst(input, num_distinct):
    for i in range(len(input)-num_distinct):
        temp_list = []
        for j in range(i,i+num_distinct):
            temp_list.append(input[j])
        if len(temp_list) == len(set(temp_list)):
            return(i+num_distinct)

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    input = f.readlines()[0]

print(findFirst(input, 4))
print(findFirst(input, 14))