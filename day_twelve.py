from collections import defaultdict

maze = defaultdict(list)


def find_all_paths(position, visited, rewatch):
    if position == "end":
        return 1

    if position.islower():
        visited.add(position)

    total_neigh = sum(
        [
            find_all_paths(i, visited, rewatch)
            for i in maze[position]
            if not i in visited
        ]
    )
    total_neigh += (
        sum(
            [
                find_all_paths(i, visited, i)
                for i in maze[position]
                if i in visited and i != "start"
            ]
        )
        if rewatch == " "
        else 0
    )

    if position != rewatch:
        visited.discard(position)

    return total_neigh


def part_one():
    for left, right in [
        line.split("-") for line in open("input/day_twelve").read().splitlines()
    ]:
        maze[left].append(right)
        maze[right].append(left)

    return find_all_paths(position="start", visited=set(), rewatch="")


def part_two():
    maze = defaultdict(list)
    for left, right in [
        line.split("-") for line in open("input/day_twelve").read().splitlines()
    ]:
        maze[left].append(right)
        maze[right].append(left)

    return find_all_paths(position="start", visited=set(), rewatch=" ")


if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
