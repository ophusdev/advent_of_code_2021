from utils import read_from_file


def flash_it(x, y):
    global flash_event, matrix

    matrix[x][y] += 1

    if matrix[x][y] == 10:
        flash_event += 1
        neighbours = [
            (x + i, y + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if (i, j) != (0, 0)
            and 0 <= x + i < len(matrix)
            and 0 <= y + j < len(matrix[0])
        ]
        for n1, n2 in neighbours:
            flash_it(n1, n2)

flash_event = 0

def part_one():
    content = read_from_file("day_eleven")
    global matrix, flash_event
    matrix = []
    matrix = [[int(d) for d in x] for x in content]

    for i in range(100):
        for idx, row in enumerate(matrix):
            for idy, _ in enumerate(row):
                flash_it(idx, idy)

        matrix = [[d if d <= 9 else 0 for d in row] for row in matrix]

    return flash_event


def part_two():

    content = read_from_file("day_eleven")
    global matrix, flash_event
    matrix = []
    matrix = [[int(d) for d in x] for x in content]

    

    for i in range(999):
        all_lines_zero = []
        for idx, row in enumerate(matrix):
            for idy, _ in enumerate(row):
                flash_it(idx, idy)

        matrix = [[d if d <= 9 else 0 for d in row] for row in matrix]

        for idx, digits in enumerate(matrix):
            if all([d == 0 for d in digits]):
                all_lines_zero.append(digits)

        if len(all_lines_zero) == len(matrix):
            return i + 1


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
