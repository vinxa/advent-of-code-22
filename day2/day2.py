import os
input = 'input.txt'
score_p1 = 0
score_p2 = 0

with open(os.path.join(os.path.dirname(__file__),input)) as f:
    for line in f:
        opponent = ord(line[0])-64
        response = ord(line[2])-87
        score_p1 += response

        # Part 1
        match(response - opponent):
            case 1:
                score_p1 += 6
            case -2:
                score_p1 += 6
            case 0:
                score_p1 += 3
        
        # Part 2
        match(response):
            case 1:  # lose
                if opponent - 1 == 0:
                    score_p2 += 3
                else:
                    score_p2 += opponent - 1
            case 2:  # draw
                score_p2 += 3
                score_p2 += opponent
            case 3:  # win
                score_p2 += 6
                if opponent + 1 == 4:
                    score_p2 += 1
                else:
                    score_p2 += opponent + 1
        print(f'{line[0]} - {line[2]} - Shape: {response} - Part 1 Current Score: {score_p1} - Part 2 Current Score: {score_p2}')