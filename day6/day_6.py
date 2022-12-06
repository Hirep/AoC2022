data = [n.strip() for n in open('day_6').readlines() if n and not n.startswith('#')]


def check_marker(buffer: list):
    return len(set(buffer)) == 4


def part1():
    datastream = data[0]

    buffer = list(datastream[0:4])
    if check_marker(buffer):
        return 4
    for i in range(4, len(datastream)):
        del buffer[0]
        buffer.append(datastream[i])
        if check_marker(buffer):
            return i + 1


def check_message(buffer: list):
    return len(set(buffer)) == 14


def part2():
    datastream = data[0]
    print(datastream)
    buffer = list(datastream[0:14])
    if check_message(buffer):
        return 14
    for i in range(14, len(datastream)):
        del buffer[0]
        buffer.append(datastream[i])
        if check_message(buffer):
            return i + 1


if __name__ == '__main__':
    print(part1())
    print(part2())