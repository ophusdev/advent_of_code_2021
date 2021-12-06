from utils import read_from_file


def part_one():
    content = read_from_file("day_six")

    init_state = content[0].split(",")
    init_state = [int(x) for x in init_state]

    day = 0

    while day < 80:

        new_state = []

        for i, state in enumerate(init_state):
            if state == 0:
                new_state.append(8)
                init_state[i] = 7

            init_state[i] -= 1

        day += 1
        init_state += new_state

    return len(init_state)


def part_two():
    content = read_from_file("day_six")

    init_state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    init_state_int = content[0].split(",")
    init_state_int = [int(x) for x in init_state_int]

    for c in init_state_int:
        init_state[c] += 1

    for _ in range(0, 256):
        app = init_state[0]
        for new in range(0, 8):
            init_state[new] = init_state[new + 1]

        init_state[8] = app
        init_state[6] += app

    return sum(init_state.values())


if __name__ == "__main__":
    # one = part_one()
    # print(one)
    two = part_two()
    print(two)
