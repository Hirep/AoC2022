import string

data = [n.strip() for n in open('day_3').readlines()]
alphabet_map = {letter: i for i, letter in enumerate(string.ascii_letters)}

def part1():
    item_list = []
    for rucksack in data:
        rucksack_capacity = len(rucksack)
        (
            compartment_1,
            compartment_2
        ) = (
            rucksack[:int(rucksack_capacity/2)],
            rucksack[int(rucksack_capacity/2):]
        )
        for item in compartment_1:
            if item in compartment_2:
                item_list.append(item)
                break
    total = 0
    for item in item_list:
        total += alphabet_map[item] + 1
    return total


def part2():
    item_list = []
    for i, rucksack in enumerate(data[::3]):
        for item in rucksack:
            if item in data[i*3+1] and item in data[i*3+2]:
                item_list.append(item)
                break
    total = 0
    for item in item_list:
        total += alphabet_map[item] + 1
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())