from collections import defaultdict

s = "109,424,203,1,21102,11,1,0,1106,0,282,21101,18,0,0,1106,0,259,1202,1,1,221,203,1,21101,31,0,0,1105,1,282,21101,0,38,0,1106,0,259,20101,0,23,2,22101,0,1,3,21102,1,1,1,21102,57,1,0,1105,1,303,2102,1,1,222,21002,221,1,3,21001,221,0,2,21101,0,259,1,21101,80,0,0,1106,0,225,21101,0,149,2,21101,91,0,0,1106,0,303,1202,1,1,223,21002,222,1,4,21102,1,259,3,21101,225,0,2,21101,0,225,1,21101,118,0,0,1106,0,225,21001,222,0,3,21102,1,58,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,1201,1,0,223,21002,221,1,4,20102,1,222,3,21101,21,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,105,1,109,20207,1,223,2,20102,1,23,1,21101,0,-1,3,21102,1,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22101,0,-3,1,21201,-2,0,2,22101,0,-1,3,21101,250,0,0,1106,0,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21101,0,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21102,1,384,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2105,1,0"
s = list(map(int, s.split(",")))
dct1 = defaultdict(int)

for i in range(len(s)):
    dct1[i] = s[i]


def decode(n):
    d = [0, 0, 0, 0, 0]
    pos = len(d) - 1
    while n > 0 and pos >= 0:
        d[pos] = n % 10
        n //= 10
        pos -= 1
    return d


def getPoint(x,y):
    dct = dct1.copy()
    put = [x, y]
    base = 0
    i = 0
    while dct[i] != 99:
        code = decode(dct[i])
        op = code[4]
        p1 = code[2]
        p2 = code[1]
        p3 = code[0]

        if op == 1:
            if p3 == 2:
                dct[base + dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[
                    i + 1]) + (
                                             dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[
                                                 i + 2])
            else:
                dct[dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[
                    i + 1]) + (
                                      dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
            i += 4
        elif op == 2:
            if p3 == 2:
                dct[base + dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[
                    i + 1]) * (
                                             dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[
                                                 i + 2])
            else:
                dct[dct[i + 3]] = (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[
                    i + 1]) * (
                                      dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])
            i += 4
        elif op == 3:
            if p1 == 2:
                dct[base + dct[i + 1]] = put[0]
            else:
                dct[dct[i + 1]] = put[0]
            put.pop(0)
            i += 2
        elif op == 4:
            return dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]
            i += 2
        elif op == 5:
            i = (dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2]) if (
                    (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) != 0) else i + 3
        elif op == 6:
            i = (dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2]) if (
                    (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == 0) else i + 3
        elif op == 7:
            if p3 == 2:
                dct[base + dct[i + 3]] = 1 if (
                            (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) < (
                        dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
            else:
                dct[dct[i + 3]] = 1 if (
                            (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) < (
                        dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
            i += 4
        elif op == 8:
            if p3 == 2:
                dct[base + dct[i + 3]] = 1 if (
                            (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == (
                        dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
            else:
                dct[dct[i + 3]] = 1 if (
                            (dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]) == (
                        dct[dct[i + 2]] if p2 == 0 else dct[base + dct[i + 2]] if p2 == 2 else dct[i + 2])) else 0
            i += 4
        elif op == 9:
            base += dct[dct[i + 1]] if p1 == 0 else dct[base + dct[i + 1]] if p1 == 2 else dct[i + 1]
            i += 2


def getGrid(offsetX, offsetY):
    grid = [["." for i in range(100)] for j in range(100)]

    for x in range(offsetX, offsetX + 100):
        if getPoint(x, offsetY) == 1:
            grid[0][x - offsetX] = "#"
        if getPoint(x, offsetY + 100) == 1:
            grid[99][x - offsetX] = "#"

    for y in range(offsetY, offsetY + 100):
        if getPoint(offsetX, y) == 1:
            grid[y - offsetY][0] = "#"
        if getPoint(offsetX + 100, y) == 1:
            grid[y - offsetY][99] = "#"

    return grid


#g = getGrid(667, 1097)
#print("\n".join("".join(x) for x in g))

print

g = [["." for i in range(100)] for j in range(100)]
offsetX = 667
offsetY = 1097
for x in range(offsetX, offsetX + 100):
    for y in range(offsetY, offsetY + 100):
        if getPoint(x,y) == 1:
            g[y - offsetY][x - offsetX] = "#"
print("\n".join("".join(x) + "\t" + str(x.count("#")) for x in g))