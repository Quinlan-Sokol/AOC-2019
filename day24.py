from copy import deepcopy
grid = [list(x) for x in "....#\n#..#.\n#..##\n..#..\n#....".splitlines()]
grid2 = deepcopy(grid)
arr = []

while grid not in arr:
    arr.append(grid)
    for i in range(5):
        for j in range(5):
            up = "."
            down = "."
            left = "."
            right = "."

            if j > 0: up = grid[j-1][i]
            if j < 4: down = grid[j+1][i]
            if i > 0: left = grid[j][i-1]
            if i < 4: right = grid[j][i+1]

            n = [up, down, left, right].count("#")
            if n != 1 and grid[j][i] == "#":
                grid2[j][i] = "."
            elif (n == 1 or n == 2) and grid[j][i] == ".":
                grid2[j][i] = "#"
    grid = deepcopy(grid2)

total = 0
n = 1
for row in grid:
    for tile in row:
        if tile == "#":
            total += n
        n *= 2
print(total)