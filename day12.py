from itertools import combinations

pos = {"I": [-13, 14, -7],
       "E": [-18, 9, 0],
       "C": [0, -3, -3],
       "G": [-15, 3, -13]}
vel = {"I": [0, 0, 0],
       "E": [0, 0, 0],
       "C": [0, 0, 0],
       "G": [0, 0, 0]}

arr = set("".join("".join(map(str, pos[x])) + "".join(map(str, vel[x])) for x in ["I", "E", "C", "G"]))


def gravity():
    for c in combinations(["I", "E", "C", "G"], 2):
        if pos[c[0]][0] > pos[c[1]][0]:
            vel[c[0]][0] -= 1
            vel[c[1]][0] += 1
        elif pos[c[0]][0] < pos[c[1]][0]:
            vel[c[1]][0] -= 1
            vel[c[0]][0] += 1

        if pos[c[0]][1] > pos[c[1]][1]:
            vel[c[0]][1] -= 1
            vel[c[1]][1] += 1
        elif pos[c[0]][1] < pos[c[1]][1]:
            vel[c[1]][1] -= 1
            vel[c[0]][1] += 1

        if pos[c[0]][2] > pos[c[1]][2]:
            vel[c[0]][2] -= 1
            vel[c[1]][2] += 1
        elif pos[c[0]][2] < pos[c[1]][2]:
            vel[c[1]][2] -= 1
            vel[c[0]][2] += 1


def move():
    for m in ["I", "E", "C", "G"]:
        pos[m] = [sum(x) for x in zip(pos[m], vel[m])]


def s():
    return sum([sum(map(abs, pos[m])) * sum(map(abs, vel[m])) for m in ["I", "E", "C", "G"]])


i = 0
while True:
    if i == 1000: break

    gravity()
    print(vel)
    move()

    i += 1

    string = "".join("".join(map(str, pos[x])) + "".join(map(str, vel[x])) for x in ["I", "E", "C", "G"])
    if string in arr:
        break
    else:
        arr.add(string)

print(s())
print(i - 1)

