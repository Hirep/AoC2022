data = [n.strip().split(',') for n in open('day_4').readlines()]


def part1():
    c = 0
    for pair in data:
        first_elf, second_elf = pair[0].split('-'), pair[1].split('-')
        first_elf = [int(first_elf[0]), int(first_elf[1])]
        second_elf = [int(second_elf[0]), int(second_elf[1])]
        if (
            (first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]) or
            (second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1])
        ):
            print(pair)
            c += 1
    return c


def dot_product(a, b):
    return a * b

def part2():
    c = 0
    for pair in data:
        first_elf, second_elf = pair[0].split('-'), pair[1].split('-')
        first_elf = [int(first_elf[0]), int(first_elf[1])]
        second_elf = [int(second_elf[0]), int(second_elf[1])]

        if (
            (second_elf[0] <= first_elf[0] and first_elf[0] <= second_elf[1]) or
            (second_elf[0] <= first_elf[1] and first_elf[1] <= second_elf[1]) or
            (
                (first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]) or
                (second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1])
            )
        ):
            print(pair)
            c += 1
    return c


if __name__ == '__main__':
    # print(part1())
    print(part2())