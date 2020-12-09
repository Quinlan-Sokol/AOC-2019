from itertools import permutations
s = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
s = list(map(int, s.split(",")))
phaseSettings = [5, 6, 7, 8, 9]


def decode(n):
    d = [0, 0, 0, 0, 0]
    pos = len(d) - 1
    while n > 0 and pos >= 0:
        d[pos] = n % 10
        n //= 10
        pos -= 1
    return d


def gen(put):
    i = 0
    while i < len(s) and s[i] != 99:
        code = decode(s[i])
        op = code[4]
        p1 = code[2] == 0
        p2 = code[1] == 0

        if op == 1:
            s[s[i + 3]] = (s[s[i + 1]] if p1 else s[i + 1]) + (s[s[i + 2]] if p2 else s[i + 2])
            i += 4
        elif op == 2:
            s[s[i + 3]] = (s[s[i + 1]] if p1 else s[i + 1]) * (s[s[i + 2]] if p2 else s[i + 2])
            i += 4
        elif op == 3:
            s[s[i + 1]] = put[0]
            put.pop(0)
            i += 2
        elif op == 4:
            yield s[s[i + 1]] if p1 else s[i + 1]
            i += 2
        elif op == 5:
            i = (s[s[i + 2]] if p2 else s[i + 2]) if ((s[s[i + 1]] if p1 else s[i + 1]) != 0) else i + 3
        elif op == 6:
            i = (s[s[i + 2]] if p2 else s[i + 2]) if ((s[s[i + 1]] if p1 else s[i + 1]) == 0) else i + 3
        elif op == 7:
            s[s[i + 3]] = 1 if ((s[s[i + 1]] if p1 else s[i + 1]) < (s[s[i + 2]] if p2 else s[i + 2])) else 0
            i += 4
        elif op == 8:
            s[s[i + 3]] = 1 if ((s[s[i + 1]] if p1 else s[i + 1]) == (s[s[i + 2]] if p2 else s[i + 2])) else 0
            i += 4


arr = []
for perm in permutations(phaseSettings, len(phaseSettings)):
    signal = 0

    for k in perm:
        gen([k, signal])

    arr.append(signal)
print(max(arr))