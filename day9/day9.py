import os, math

# Read input
input = "input.txt"
with open(os.path.join(os.path.dirname(__file__), input)) as f:
    input = [x.strip() for x in f.readlines()]

# Starting coordinates
H = [0,0]
T1 = [[0,0]]
t1_visits = set()
T2 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
t2_visits = set()

def headMove(direction):
    match direction:
        case 'R':
            H[0] += 1
        case 'L':
            H[0] -= 1
        case 'U':
            H[1] += 1
        case 'D':
            H[1] -= 1
        case _:
            raise ValueError('Unable to read direction.')

def tailMove(H, T):
        # Tail movement
        if abs(H[0]-T[0]) <= 1 and abs(H[1]-T[1]) <= 1:  # No need to move
            return [T[0], T[1]]#f'{T[0]}-{T[1]}'
        if H[0] == T[0]: #  On same x plane
            T[1] += int(math.copysign(1, H[1]-T[1]))
            return [T[0], T[1]]
        if H[1] == T[1]:  # On same y plane
            T[0] += int(math.copysign(1, H[0]-T[0]))
            return [T[0], T[1]]
            
        # Diagonal
        T[0] += int(math.copysign(1, H[0]-T[0]))
        T[1] += int(math.copysign(1, H[1]-T[1]))
        return [T[0], T[1]]

t1_visits.add(f'0-0')
t2_visits.add(f'0-0')

for line in input:
    (direction, strength) = line.split(' ')
    for step in range(int(strength)):
        headMove(direction)
        for index,knot in enumerate(T2):  # changed for part 2 because im lazy
            if index == 0:  # First knot, only one used in Part 1.
                x = tailMove(H, T1[0])
                t1_visits.add(f'{x[0]}-{x[1]}')
                T2[index] = tailMove(H, T2[0])
                continue
            elif index == 8:
                x = tailMove(T2[index-1], T2[index])
                t2_visits.add(f'{x[0]}-{x[1]}')
            else:
                T2[index] = tailMove(T2[index-1], T2[index])
print(len(t1_visits))
print('----')
print(len(t2_visits))
