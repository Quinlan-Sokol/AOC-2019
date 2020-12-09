from collections import defaultdict

s = "3,8,1005,8,328,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,29,1,104,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,55,1,2,7,10,1006,0,23,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,84,1006,0,40,1,1103,14,10,1,1006,16,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,116,1006,0,53,1,1104,16,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,146,2,1104,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,172,1006,0,65,1,1005,8,10,1,1002,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,204,2,1104,9,10,1006,0,30,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,233,2,1109,6,10,1006,0,17,1,2,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,266,1,106,7,10,2,109,2,10,2,9,8,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,301,1,109,9,10,1006,0,14,101,1,9,9,1007,9,1083,10,1005,10,15,99,109,650,104,0,104,1,21102,1,837548789788,1,21101,0,345,0,1106,0,449,21101,0,846801511180,1,21101,0,356,0,1106,0,449,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,235244981271,0,1,21101,403,0,0,1105,1,449,21102,1,206182744295,1,21101,0,414,0,1105,1,449,3,10,104,0,104,0,3,10,104,0,104,0,21102,837896937832,1,1,21101,0,437,0,1106,0,449,21101,867965862668,0,1,21102,448,1,0,1106,0,449,99,109,2,22102,1,-1,1,21101,40,0,2,21102,1,480,3,21101,0,470,0,1106,0,513,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,475,476,491,4,0,1001,475,1,475,108,4,475,10,1006,10,507,1101,0,0,475,109,-2,2106,0,0,0,109,4,1201,-1,0,512,1207,-3,0,10,1006,10,530,21102,1,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21102,549,1,0,1106,0,554,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,577,2207,-4,-2,10,1006,10,577,21202,-4,1,-4,1106,0,645,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,596,0,0,1106,0,554,21201,1,0,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,615,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,637,22102,1,-1,1,21101,637,0,0,105,1,512,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"
s = list(map(int, s.split(",")))
dct = defaultdict(int)

for i in range(len(s)):
    dct[i] = s[i]


def decode(n):
    d = [0, 0, 0, 0, 0]
    pos = len(d) - 1
    while n > 0 and pos >= 0:
        d[pos] = n % 10
        n //= 10
        pos -= 1
    return d


base = 0
i = 0
grid = defaultdict(int)
grid[(0,0)] = 1
pos = [0,0]
direction = 0   #0=UP  1=RIGHT  2=DOWN  3=LEFT
switch = 1
part1 = set()


def move():
    if direction == 0:
        pos[1] += 1
    elif direction == 1:
        pos[0] += 1
    elif direction == 2:
        pos[1] -= 1
    elif direction == 3:
        pos[0] -= 1


while dct[i] != 99:
    code = decode(dct[i])
    op = code[4]
    p1 = code[2]
    p2 = code[1]
    p3 = code[0]

    if op == 1:
        if p3 == 2:
            dct[base + dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) + (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
        else:
            dct[dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) + (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
        i += 4
    elif op == 2:
        if p3 == 2:
            dct[base + dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) * (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
        else:
            dct[dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) * (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
        i += 4
    elif op == 3:
        if p1 == 2:
            dct[base + dct[i + 1]] = grid[tuple(pos)]
        else:
            dct[dct[i + 1]] = grid[tuple(pos)]
        i += 2
    elif op == 4:
        out = dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]

        if switch == 1: #paint
            grid[tuple(pos)] = out
            part1.add(tuple(pos))
        else: #turn
            direction += 1 if out == 1 else -1
            direction = 0 if direction > 3 else 3 if direction < 0 else direction

            move()

        switch *= -1
        i += 2
    elif op == 5:
        i = (dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2]) if (
                    (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) != 0) else i + 3
    elif op == 6:
        i = (dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2]) if (
                    (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == 0) else i + 3
    elif op == 7:
        if p3 == 2:
            dct[base + dct[i + 3]] = 1 if ((dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) < (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
        else:
            dct[dct[i + 3]] = 1 if ((dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) < (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
        i += 4
    elif op == 8:
        if p3 == 2:
            dct[base + dct[i + 3]] = 1 if ((dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
        else:
            dct[dct[i + 3]] = 1 if ((dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == (
                dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
        i += 4
    elif op == 9:
        base += dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]
        i += 2

print(len(part1))

whites = [x for x in grid.keys() if grid[x] == 1]
minX = min(whites, key=lambda x: x[0])[0]
minY = min(whites, key=lambda x: x[1])[1]
whites = list(map(lambda x: (x[0] + abs(minX), x[1] + abs(minY)), whites))

maxX = max(whites, key=lambda x: x[0])[0] + 1
maxY = max(whites, key=lambda x: x[1])[1] + 1

hull = [["#" if (x,y) in whites else "." for x in range(maxX)] for y in range(maxY)]
print("\n".join(["".join(x) for x in reversed(hull)]))
#HJKJKGPH