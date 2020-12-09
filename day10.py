import math
from collections import defaultdict

with open("input.txt", "r") as f:
    grid = [list(x) for x in f.read().splitlines()]


    def getAngles(x, y, b=False):
        s = set()
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if i != x or j != y:
                    if grid[j][i] == "#":
                        if b:
                            s.add(((i, j), math.atan2(y - j, x - i)))
                        else:
                            s.add(math.atan2(y - j, x - i))
        return s


    arr = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                arr.append(([x, y], getAngles(x, y)))

    station = max(arr, key=lambda x: len(x[1]))
    print(len(station[1]))

    angles = sorted(getAngles(station[0][0], station[0][1], True), key=lambda x: x[1])


    # print(angles)

    def dis(p):
        return ((p[0] - station[0][0]) ** 2 + (p[1] - station[0][1]) ** 2) ** .5


    dct = defaultdict(list)

    for a in angles:
        dct[math.degrees(a[1])].append(a[0])
        dct[math.degrees(a[1])].sort(key=dis)

    # print(dct)

    keys = sorted([x for x in dct.keys() if x >= 90]) + sorted([x for x in dct.keys() if x < 90])

    # print(keys)

    c = 0
    for i in range(len(keys)):
        a = keys[i]

        if len(dct[a]) > 0:
            # print(dct[a][0])
            if c == 199:
                print(dct[a][0])
                break
            dct[a].pop(0)
            c += 1


