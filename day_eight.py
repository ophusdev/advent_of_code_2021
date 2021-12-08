from utils import read_from_file

numbers = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def part_one():
    content = read_from_file("day_eight")

    result = []

    sum_occurence = 0

    for line in content:
        ll = line.split(" | ")
        result.append(ll[1].split(" "))

        sum_occurence += sum(
            [
                (2 <= len(occurence) <= 4) or len(occurence) == 7
                for occurence in result[-1]
            ]
        )

    return sum_occurence


def part_two():
    content = read_from_file("day_eight")

    result = [None for x in range(0, 4)]
    total = 0

    for line in content:
        ll = line.split(" | ")
        seven = set([example for example in ll[0].split(" ") if len(example) == 3][0])
        four = set([example for example in ll[0].split(" ") if len(example) == 4][0])
        lower = set([example for example in ll[0].split(" ") if len(example) == 7][0])
        for el in four.union(seven):
            lower.discard(el)
        i = 0

        for cc in ll[1].split(" "):
            cc = set(cc)
            if len(cc) == 2:
                result[i] = 1
            elif len(cc) == 3:
                result[i] = 7
            elif len(cc) == 4:
                result[i] = 4
            elif len(cc) == 7:
                result[i] = 8
            elif len(cc) == 6:
                # three possible results
                if four < cc:  # four
                    result[i] = 9
                elif seven < cc:  # seven
                    result[i] = 0
                else:
                    result[i] = 6
            else:
                if seven < cc:  # seven
                    result[i] = 3
                elif lower < cc:
                    result[i] = 2
                else:
                    result[i] = 5
            i = i + 1
        output = int("".join([str(r) for r in result]))
        total = total + output

    return total


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
