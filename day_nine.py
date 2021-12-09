from utils import read_from_file

matrix_row = 100
matrix_col = 100

def create_matrix(row, col, data_list):
    return [data_list[i : i + col] for i in range(0, len(data_list), col)]

def find_minus(matrix, matrix_row, matrix_col):
    found_minus = []
    position = []

    for idx_row, row in enumerate(matrix):
        for idx_col, col in enumerate(row):

            up = float("inf")
            down = float("inf")
            left = float("inf")
            right = float("inf")

            up = matrix[idx_row - 1][idx_col] if idx_row != 0 else float("inf")
            down = (
                matrix[idx_row + 1][idx_col]
                if idx_row != matrix_row - 1
                else float("inf")
            )
            left = matrix[idx_row][idx_col - 1] if idx_col != 0 else float("inf")
            right = (
                matrix[idx_row][idx_col + 1]
                if idx_col != matrix_col - 1
                else float("inf")
            )

            actual_number = matrix[idx_row][idx_col]

            if (
                actual_number < up
                and actual_number < left
                and actual_number < right
                and actual_number < down
            ):
                found_minus.append(int(actual_number))
                position.append({
                    actual_number: [idx_row, idx_col]
                })
    return found_minus, position

def part_one():
    content = read_from_file("day_nine")

    c_list = []

    for c in content:
        c_list += [int(x) for x in c]

    matrix = create_matrix(matrix_row, matrix_col, c_list)

    found_minus, _ = find_minus(matrix, matrix_row, matrix_col)

    return len(found_minus) + sum([x for x in found_minus])


def get_neighbour(row, col):
    coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # top, bottom, left, right
    neigh = []
    for n in coords:
        y, x = (row + n[0], col + n[1])
        if y < 0 or x < 0 or y > 99 or x > 99:
            continue
        neigh.append((y, x))
    return neigh

already_visited = {}

def found_basin(matrix, idx_row, idx_col):

    already_visited[(idx_row, idx_col)] = 1
    neighbour = (idx_row,idx_col)

    for r, c in get_neighbour(idx_row,idx_col):
        if c >= matrix_col or r >= matrix_row:
            continue

        if (r, c) in already_visited or int(matrix[r][c]) >= 9:
            continue
    
        neighbour += found_basin(matrix, r, c)

    return neighbour

def part_two():
    content = read_from_file("day_nine")

    c_list = []
    matrix_row = 100
    matrix_col = 100

    for c in content:
        c_list += [int(x) for x in c]

    matrix = create_matrix(matrix_row, matrix_col, c_list)

    _, position = find_minus(matrix, matrix_row, matrix_col)

    ret = []

    for p in position:
        minus = list(p.keys())[0]
        ret.append(found_basin(matrix, p[minus][0], p[minus][1]))
    
    ret = sorted([len(x)/2 for x in ret], reverse=True)

    return int(ret[0] * ret[1] * ret[2])
    


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
