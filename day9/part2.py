data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


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


knots_x_y = [[0, 0] for _ in range(10)]
tail_visited = {(0, 0)}
for line in data:
    direction, num = line.split(" ")
    for x in range(int(num)):
        if direction == "U":
            knots_x_y[0][1] += 1
        elif direction == "D":
            knots_x_y[0][1] -= 1
        elif direction == "L":
            knots_x_y[0][0] -= 1
        elif direction == "R":
            knots_x_y[0][0] += 1

        for i, knots in enumerate(zip(knots_x_y, knots_x_y[1:]), start=1):
            kmx, kmy = knot_move(knots[0][0], knots[0][1], knots[1][0], knots[1][1])
            knots_x_y[i][0] += kmx
            knots_x_y[i][1] += kmy

        tail_visited.add((knots_x_y[-1][0], knots_x_y[-1][1]))

print(len(tail_visited))
