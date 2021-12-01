from utils import read_from_file


def part_one():
    content = read_from_file("day_one")
    return sum(int(content[i]) > int(content[i - 1]) for i, _ in enumerate(content))


def part_two():

    content = read_from_file("day_one")
    measurement = 0
    limit = 3
    for i in range(len(content)):

        slide_1 = content[i : i + limit]
        slide_2 = content[i + 1 : i + limit + 1]

        if len(slide_1) < limit or len(slide_2) < limit:
            return measurement

        sum_slide_1 = sum(int(slide_1[i]) for i, _ in enumerate(slide_1))
        sum_slide_2 = sum(int(slide_2[i]) for i, _ in enumerate(slide_2))

        if sum_slide_2 > sum_slide_1:
            measurement += 1

    return measurement


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
