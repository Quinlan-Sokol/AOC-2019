import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

grid = list(map(list, open("input.txt", "r").read().splitlines()))
arr = []
start = [55, 2]
end = [63, 116]
portals = {(39,2): (81,30),
           (47,2): (30,81),
           (49,2): (86,47),
           (57,2): (73,88),
           (69,2): (86,63),
           (75,2): (86,79),
           (79,2): (30,60),
           (35,30): (53,116),
           (43,30): (79,116),
           (53,30): (114,65),
           (59,30): (39,116),
           (69,30): (45,116),
           (73,30): (114,43),
           (86,35): (114,79),
           (30,37): (114,57),
           (30,49): (2,43),
           (86,51): (2,47),
           (114,41): (45,88),
           (114,53): (86,75),
           (86,55): (65,116),
           (2,57): (30,61),
           (2,67): (37,88),
           (114,73): (30,69),
           (2,75): (49,88),
           (2,83): (59,88),
           (57,88): (43,116),
           (77,88): (67,116)}
for p in portals.keys():
    portals[portals[p]] = p


def solve(pos, dct, steps, level):
    if pos == end and level == 0:
        arr.append(steps)
        print(arr)
    else:
        up = grid[pos[1] - 1][pos[0]]
        down = grid[pos[1] + 1][pos[0]]
        left = grid[pos[1]][pos[0] - 1]
        right = grid[pos[1]][pos[0] + 1]

        if up == "." and not [pos[0], pos[1] - 1] in dct[level]:
            temp = dct.copy()
            temp[level].append(pos)
            solve([pos[0], pos[1] - 1], temp, steps + 1, level)
        if down == "." and not [pos[0], pos[1] + 1] in dct[level]:
            temp = dct.copy()
            temp[level].append(pos)
            solve([pos[0], pos[1] + 1], temp, steps + 1, level)
        if left == "." and not [pos[0] - 1, pos[1]] in dct[level]:
            temp = dct.copy()
            temp[level].append(pos)
            solve([pos[0] - 1, pos[1]], temp, steps + 1, level)
        if right == "." and not [pos[0] + 1, pos[1]] in dct[level]:
            temp = dct.copy()
            temp[level].append(pos)
            solve([pos[0] + 1, pos[1]], temp, steps + 1, level)

        if tuple(pos) in portals:
            layer =  level + (1 if pos[0] == 114 or pos[0] == 2 or pos[1] == 116 or pos[1] == 2 else -1)
            if not list(portals[tuple(pos)]) in dct[layer] and 0 <= layer <= len(portals.keys()) // 2:
                temp = dct.copy()
                temp[level].append(pos)
                solve(portals[tuple(pos)], temp, steps + 1, layer)


solve(start, defaultdict(list), 0, 0)
print(arr)