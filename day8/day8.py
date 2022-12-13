import os
from functools import reduce

def setId(treeMap, input):
    setInput = []
    for rowIndex, row in enumerate(input):
        for columnIndex, value in enumerate(row):
            value = int(value)
            setInput.append([rowIndex,columnIndex,value])
    return setInput

def checkTrees(treeMap, input, rowCheck, colCheck):
    for item in input:
        # Set up Dict.
        checkIndexExists(treeMap, rowCheck, item[0])
        checkIndexExists(treeMap, colCheck, item[1])
        value = int(item[2])

        # Check if biggest value in that row
        currentList = treeMap[rowCheck][item[0]]
        if value > currentList[-1][2]:
            currentList.append(item)
        
        # Check if biggest value in that column
        currentList = treeMap[colCheck][item[1]]
        if value > currentList[-1][2]:
            currentList.append(item)

def checkIndexExists(map, key, index):
    if not index in map[key].keys():
        map[key][index] = [[-1,-1,-1]]

def scenic_score(item, comparison_trees):
    if all(item[2] > tree[2] for tree in comparison_trees):
        return len(comparison_trees)
    for ind, comparison in enumerate(comparison_trees):
        if comparison[2] >= item[2]:
            return ind + 1

# Read input
input = "input.txt"

with open(os.path.join(os.path.dirname(__file__), input)) as f:
    input = [x.strip() for x in f.readlines()]

#Build map
treeMap = {"rows": {}, "columns": {},"rows_r": {}, "columns_r": {}}

#Make an ID, so we can preserve values when list is reversed
input = setId(treeMap, input)
checkTrees(treeMap, input, "rows","columns")
input.reverse()
checkTrees(treeMap, input, "rows_r","columns_r")

#Remove any trees registered twice in the dictionary
master_list = []
for a in treeMap.values():
    for b in a.values():
        for c in b:
            if c[0] != -1 and c not in master_list:
                master_list.append(c)

#print(master_list)
print(len(master_list))

# Find Highest Scenic Score
top_scenic_score = 0
for item in input:
    left_row_compare = [x for x in input if x[0] == item[0] and x[1] < item[1]]
    up_col_compare = [x for x in input if x[1] == item[1] and x[0] < item[0]]
    # Because its currently sorted backwards, we need the lists in relation to the item so we reverse the following
    down_col_compare = [x for x in input if x[1] == item[1] and x[0] > item[0]]
    down_col_compare.reverse()
    right_row_compare = [x for x in input if x[0] == item[0] and x[1] > item[1]]
    right_row_compare.reverse()
    sc = 1
    for dir in [left_row_compare,right_row_compare,up_col_compare,down_col_compare]:
        sc *= scenic_score(item, dir)

    if (sc > top_scenic_score):
        top_scenic_score = sc

print(top_scenic_score)