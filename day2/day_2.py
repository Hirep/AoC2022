data = [tuple(n.strip().split(' ')) for n in open('day_2').readlines()]

outcome_scores = {
    ('A', 'X'): 3 + 1,
    ('A', 'Y'): 6 + 2,
    ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1,
    ('C', 'Y'): 0 + 2,
    ('C', 'Z'): 3 + 3,
}


def part1():
    score = 0
    for pair in data:
        score += outcome_scores[pair]
    return score


lose_map = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

draw_map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

win_map = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


def part2():
    score = 0
    for pair in data:
        a = pair[0]
        if pair[1] == 'X':
            b = lose_map[a]
        elif pair[1] == 'Y':
            b = draw_map[a]
        else:
            b = win_map[a]
        score += outcome_scores[(a, b)]
    return score


if __name__ == '__main__':
    print(part1())
    print(part2())