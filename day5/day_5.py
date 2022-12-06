from collections import defaultdict

data = [n for n in open('day_5').readlines()]


def move_p1(stack_map: dict, instruction: list[int]):
    for _ in range(instruction[0]):
        value = stack_map[instruction[1]-1].pop()
        stack_map[instruction[2]-1].append(value)


def move_p2(stack_map: dict, instruction: list[int]):
    values = []
    for _ in range(instruction[0]):
        value = stack_map[instruction[1]-1].pop()
        values.append(value)
    values.reverse()
    stack_map[instruction[2]-1].extend(values)
    print(stack_map)


def parse_data(data: list[str]):
    stack_map = defaultdict(list)
    reversed_stacks = False
    for line in data:
        if line.startswith(' 1'):
            continue
        if line == '\n':
            continue
        if line.startswith('move'):
            if not reversed_stacks:
                for stack in stack_map.keys():
                    stack_map[stack].reverse()
                    reversed_stacks = True
            line = line.split(' ')
            instruction = [int(x) for x in line if x.strip().isdigit()]
            move_p2(stack_map, instruction)
            continue

        line = line.replace('\n', '')
        for stack_number, i in enumerate(range(1, len(line) - 1, 4)):
            if line[i] == ' ':
                continue
            stack_map[stack_number].append(line[i])

    result = ''
    for stack in range(len(stack_map.keys())):
        result += stack_map[stack][-1]
    return result



if __name__ == '__main__':
    print(parse_data(data))