from collections import Counter
from utils import read_from_file


def part_one():
    content = read_from_file("day_three")

    line_len = len(content[0])

    gamma = ''
    eps = ''

    for i in range(0, line_len):
    
        digit = [x[i] for x in content]
        occ = max(set(digit), key=digit.count)

        gamma += occ
        tmp_eps = '1' if occ == '0' else '0'
        eps = eps + tmp_eps
    
    return int(gamma, 2) * int(eps, 2)


def find_mask(lines, upper, stop):

    for line in range(len(lines[0])):
        col = [r[line] for r in lines]
        gamma = eps = ""
        gamma += max(set(col), key=col.count)
        eps += min(set(col), key=col.count)
        match = gamma if upper else eps

        if gamma != eps:
            lines = [x for x in lines if x[line] == match]
        else:
            lines = [x for x in lines if x[line] == stop]
        
        if len(lines) == 1:
            return "".join(lines)


def part_two():

    content = read_from_file("day_three")

    line_len = len(content[0])

    ret_generator = 0
    ret_srub = 0

    ret_generator = find_mask(content, True, '1')
    ret_srub = find_mask(content, False, '0')
    
    return int(ret_generator, 2) * int(ret_srub, 2)


if __name__ == "__main__":
    #one = part_one()
    #print(one)
    two = part_two()
    print(two)
