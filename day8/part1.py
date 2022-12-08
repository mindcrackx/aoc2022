data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """30373
25512
65332
33549
35390"""


# data = test_data()

grid = []
for line in data.splitlines():
    tmp = []
    for num in line:
        tmp.append(int(num))
    grid.append(tmp)


visible = 0
visible += len(grid) * 2
visible += len(grid[0]) * 2
visible -= 4

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if x == 0 or x == (len(grid) - 1) or y == 0 or y == (len(grid[0]) - 1):
            continue
        # left
        found = False
        for tree in grid[x][:y]:
            if tree >= grid[x][y]:
                found = True
                break
        if not found:
            visible += 1
            continue
        # right
        found = False
        for tree in grid[x][y + 1 :]:
            if tree >= grid[x][y]:
                found = True
                break
        if not found:
            visible += 1
            continue
        # up
        found = False
        for tree in grid[:x]:
            if tree[y] >= grid[x][y]:
                found = True
                break
        if not found:
            visible += 1
            continue
        # down
        found = False
        for tree in grid[x + 1 :]:
            if tree[y] >= grid[x][y]:
                found = True
                break
        if not found:
            visible += 1
            continue


print(visible)
