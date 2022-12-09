data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


# data = test_data()
data = data.splitlines()


def knot_move(hx, hy, tx, ty):
    if tx in (hx, hx + 1, hx - 1) and ty in (hy, hy + 1, hy - 1):
        return (0, 0)
    if ty == hy:
        if tx > hx:
            return (-1, 0)
        else:
            return (1, 0)
    if tx == hx:
        if ty > hy:
            return (0, -1)
        else:
            return (0, 1)
    if tx > hx and ty > hy:
        return (-1, -1)
    if tx < hx and ty < hy:
        return (1, 1)
    if tx > hx and ty < hy:
        return (-1, 1)
    if tx < hx and ty > hy:
        return (1, -1)


hx, hy = 0, 0
tx, ty = 0, 0
tail_visited = {(0, 0)}
for line in data:
    direction, num = line.split(" ")
    for x in range(int(num)):
        if direction == "U":
            hy += 1
        elif direction == "D":
            hy -= 1
        elif direction == "L":
            hx -= 1
        elif direction == "R":
            hx += 1
        tmx, tmy = knot_move(hx, hy, tx, ty)
        tx += tmx
        ty += tmy
        tail_visited.add((tx, ty))

print(len(tail_visited))
