from collections import defaultdict


points = []
folds = []

def part_one(points):
    for dim, pos in folds:
        for dot in points:
            if dot[dim] > pos:
                dot[dim] = 2*pos - dot[dim]
        points = [dot for dot in points if dot[dim] != pos]
        l = max([dot[dim] for dot in points])
        if pos < l // 2:
            offset = l - 2 * pos + 1
            for dot in points:
                dot[dim] += offset
        break
    return points

def part_two(points):
    for dim, pos in folds:
        for dot in points:
            if dot[dim] > pos:
                dot[dim] = 2*pos - dot[dim]
        points = [dot for dot in points if dot[dim] != pos]
        l = max([dot[dim] for dot in points])
        if pos < l // 2:
            offset = l - 2 * pos + 1
            for dot in points:
                dot[dim] += offset
    return points


def print_dots(dots):
    xmax = max([dot[0] for dot in dots])
    ymax = max([dot[1] for dot in dots])
    grid = [['.'] * (xmax+1) for count in range(ymax+1)]
    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    for row in grid:
	    print(''.join([str(n) for n in row]))

if __name__ == "__main__":
    for line in open("input/day_thirteen").read().splitlines():
        if line and line[0].isnumeric():
            points.append(([int(n) for n in line.strip().split(',')]))
        elif line:
            folds.append((0 if line[11] == 'x' else 1, int(line.split('=')[1])))

    one = len(set([tuple(dot) for dot in part_one(points)]))
    print(one)

    for line in open("input/day_thirteen").read().splitlines():
        if line and line[0].isnumeric():
            points.append(([int(n) for n in line.strip().split(',')]))
        elif line:
            folds.append((0 if line[11] == 'x' else 1, int(line.split('=')[1])))

    print_dots(part_two(points))
    
