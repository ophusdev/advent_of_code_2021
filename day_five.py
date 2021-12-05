from utils import read_from_file


def part_one():
    content = read_from_file("day_five")

    lines= []

    for c in content:
        x, y = c.split(' -> ')
        x1, y1 = x.split(',')
        x2, y2 = y.split(',')

        while (str(x1)+","+str(y1)) != (str(x2)+","+str(y2)):
            if int(x1) != int(x2) and int(y1) == int(y2):
                lines.append(str(x1)+','+str(y1))
                while int(x1) != int(x2):
                    if int(x1) > int(x2):
                        x1 = int(x1) - 1
                    elif int(x1) < int(x2):
                        x1 = int(x1) + 1
                    lines.append(str(x1)+","+str(y1))
            elif int(x1) == int(x2) and int(y1) != int(y2):
                lines.append(str(x1)+","+str(y1))
                while int(y1) != int(y2):
                    if int(y1) > int(y2):
                        y1 = int(y1) - 1
                        
                    elif int(y1) < int(y2):
                        y1 = int(y1) + 1

                    lines.append(str(x1)+","+str(y1))
            break

    already_discovered = []
    overlap = 0

    for i in lines:
        if i not in already_discovered:
            if lines.count(i) > 1:
                overlap += 1

            already_discovered.append(i)
    
    return overlap

def part_two():
    content = read_from_file("day_five")

    lines = []

    for i in content:
        a, b = i.split("->")
        a, b = a.strip(" "), b.strip(" ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        while (str(x1)+","+str(y1)) != (str(x2)+","+str(y2)):
            if x1 != x2 and y1 == y2:
                lines.append(str(x1)+","+str(y1))
                while x1 != x2:
                    if x1 > x2:
                        x1 = int(x1) - 1
                        
                    elif x1 < x2:
                        x1 = int(x1) + 1

                    lines.append(str(x1)+","+str(y1))

            elif x1 == x2 and y1 != y2:
                lines.append(str(x1)+","+str(y1))
                while y1 != y2:
                    if y1 > y2:
                        y1 = int(y1) - 1
                        
                    elif y1 < y2:
                        y1 = int(y1) + 1

                    lines.append(str(x1)+","+str(y1))

            elif x1 == y1 and x2 == y2:
                lines.append(str(x1)+","+str(y1))
                while x1 != x2:
                    if x1 > x2:
                        x1, y1 = int(x1) - 1, int(y1) - 1

                    elif x1 < x2:
                        x1, y1 = int(x1) + 1, int(y1) + 1

                    lines.append(str(x1)+","+str(y1))

            elif x1 == y2 and x2 == y1:
                lines.append(str(x1)+","+str(y1))
                while x1 != x2:
                    if x1 > x2:
                        x1, y1 = int(x1) - 1, int(y1) + 1

                    elif x1 < x2:
                        x1, y1 = int(x1) + 1, int(y1) - 1

                    lines.append(str(x1)+","+str(y1))

            else:
                lines.append(str(x1)+","+str(y1))
                while x1 != x2:
                    if x1 > x2 and y1 > y2:
                        x1, y1 = int(x1) - 1, int(y1) - 1
                
                    elif x1 < x2 and y1 < y2:
                        x1, y1 = int(x1) + 1, int(y1) + 1

                    elif x1 > x2 and y1 < y2:
                        x1, y1 = int(x1) - 1, int(y1) + 1

                    elif x1 < x2 and y1 > y2:
                        x1, y1 = int(x1) + 1, int(y1) - 1

                    lines.append(str(x1)+","+str(y1))
                
            break

    already_discovered = []
    overlap = 0

    for i in lines:
        if i not in already_discovered:
            if lines.count(i) > 1:
                overlap += 1

            already_discovered.append(i)
    
    return overlap

if __name__ == "__main__":
    one = part_one()
    print(one)
    two = part_two()
    print(two)
