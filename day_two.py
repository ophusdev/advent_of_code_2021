from utils import read_from_file


def part_one():
    content = read_from_file("day_two")
    
    total_horizontal = 0
    total_depth = 0

    for entry in content:
        op = entry.split()[0]
        count = int(entry.split()[1])

        if op == 'forward':
            total_horizontal += count
        elif op == 'down':
            total_depth += count
        else:
            total_depth -= count

    return total_horizontal * total_depth

def part_two():

    content = read_from_file("day_two")
    
    total_horizontal = 0
    total_depth = 0
    total_aim = 0

    for entry in content:
        op = entry.split()[0]
        count = int(entry.split()[1])

        if op == 'forward':
            total_horizontal += count
            total_depth += total_aim * count
        elif op == 'down':
            #total_depth += count
            total_aim += count
        else:
            #total_depth -= count
            total_aim -= count

    return total_horizontal * total_depth


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
