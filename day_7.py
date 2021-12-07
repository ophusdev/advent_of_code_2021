from utils import read_from_file


def part_one():
    content = read_from_file("day_seven")
    position = [int(c) for c in content[0].split(",")]

    total_sum = [0 for _ in range(0, len(position))]

    for i in range(0, len(position)):
        total_sum[i] = sum([abs(i - p) for p in position])

    return min(total_sum)


def part_two():
    content = read_from_file("day_seven")
    position = [int(c) for c in content[0].split(",")]

    total_sum = float("inf")

    for i in range(min(position), max(position)):
        temp_sum = 0
        for p in position:
            distance_path = abs(p - i)
            temp_sum += sum([k for k in range(1, distance_path + 1)])

        if temp_sum < total_sum:
            total_sum = temp_sum

    return total_sum


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
