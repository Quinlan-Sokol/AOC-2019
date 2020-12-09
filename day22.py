l = 119315717514047
lst = open("input.txt", "r").read().splitlines()

pos = 2020
k = 0
rep = 101741582076661
while k < 10000:
    for line in lst:
        if line.startswith("deal into new stack"):
            pos = l - pos - 1
        elif line.startswith("deal"):
            n = int(line[20:])
            pos = (pos * n) % l
        elif line.startswith("cut"):
            n = int(line[4:])
            pos = (pos - n) % l
    k += 1

print(pos)