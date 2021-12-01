def read_from_file(name: str):

    lines = []

    with open("./input/{}".format(name)) as file:
        for line in file:
            lines.append(line.strip("\n"))

    return lines
