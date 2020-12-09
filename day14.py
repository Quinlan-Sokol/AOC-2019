from collections import defaultdict

arr = []
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        parts = line.split(" => ")
        arr.append([[(int(x.split()[0]), x.split()[1]) for x in parts[0].split(", ")], (int(parts[1].split()[0]), parts[1].split()[1])])


def hasEnough(dct, items):
    for item in items:
        n = item[0]
        name = item[1]
        if dct[name] < n:
            return False
    return True


def applyRule(dct, rule):
    d = dct.copy()
    for item in rule[0]:
        d[item[1]] -= item[0]
    d[rule[1][1]] += rule[1][0]
    return d


def solve(dct):
    q = [dct]
    m = -1

    while len(q) > 0:
        e = q.pop()
        #print(e)
        if e["FUEL"] > m:
            m = e["FUEL"]
            print(m)

        for k in arr:
            if hasEnough(e, k[0]):
                q.append(applyRule(e, k))

    return m

dct = defaultdict(int)
dct["ORE"] = 10000

print(solve(dct))