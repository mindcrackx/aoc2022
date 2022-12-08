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


view_range = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        tmp = []

        # left
        view = 0
        found = False
        for tree in grid[x][:y][::-1]:
            view += 1
            if tree >= grid[x][y]:
                break
        tmp.append(view)

        # right
        view = 0
        found = False
        for tree in grid[x][y + 1 :]:
            view += 1
            if tree >= grid[x][y]:
                break
        tmp.append(view)

        # up
        view = 0
        found = False
        for tree in grid[:x][::-1]:
            view += 1
            if tree[y] >= grid[x][y]:
                break
        tmp.append(view)

        # down
        view = 0
        found = False
        for tree in grid[x + 1 :]:
            view += 1
            if tree[y] >= grid[x][y]:
                break
        tmp.append(view)

        view_range.append(tmp)


results = []
for view in view_range:
    result = view[0]
    for x in view[1:]:
        result *= x
    results.append(result)
print(max(results))
