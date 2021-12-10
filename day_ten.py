chars = ["(", ")", "[", "]", "{", "}", "<", ">"]


def read_from_file(name: str):

    lines = []

    with open("./input/{}".format(name)) as file:
        return file.read().splitlines()


def part_one():
    content = read_from_file("day_ten")

    left_char = ("(", "{", "[", "<")
    match_char = {"(": ")", "{": "}", "[": "]", "<": ">"}
    wrong_char = []
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    good_score = 0
    c_stack = []
    for line in content:
        for ch in line:
            if ch in left_char:
                c_stack.append(ch)
            else:
                if len(c_stack) > 0:
                    if not (match_char[c_stack.pop()] == ch):
                        wrong_char.append(ch)
                        break
    for i in scores:
        good_score = good_score + (scores[i] * wrong_char.count(i))

    return good_score


def part_two():
    content = read_from_file("day_ten")

    left_char = ("(", "{", "[", "<")
    match_char = {"(": ")", "{": "}", "[": "]", "<": ">"}
    wrong_char = []
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    all_scores = []

    for line in content:
        c_stack = []
        for ch in line:
            if ch in left_char:
                c_stack.append(ch)
            else:
                if len(c_stack) > 0:
                    if not (match_char[c_stack.pop()] == ch):
                        c_stack = []
                        break
        score = 0
        for i in reversed(c_stack):
            score = (score * 5) + scores[i]
        if score > 0:
            all_scores.append(score)

    score_list = sorted(all_scores)
    return score_list[int(len(score_list) / 2)]


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
