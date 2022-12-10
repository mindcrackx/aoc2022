data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


# def test_data():
# return """noop
# addx 3
# addx -5"""


# data = test_data()
data = data.splitlines()

cycle = 0
x = 1
new_x = x
ops = []
results = []
cont = 0
linenum = 0
addr = 0
while True:
    cycle += 1

    print("=" * 30, "cycle", cycle)
    print(f"start  cycle={cycle} x={x} cont={cont} addr={addr}")

    if cont > 0:
        cont -= 1

    new_x = x
    if cont == 0:
        new_x += addr
        addr = 0

    if cont == 0 and x == new_x:
        line = data[linenum]
        linenum += 1
        if line == "noop":
            pass
        else:
            addr = int(line.split(" ")[1])
            cont += 1
        print(f"during cycle={cycle} x={x} cont={cont} addr={addr} line={line}")

    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle, x, cycle * x, "*" * 30)
        results.append(cycle * x)

    if cycle == 220:
        break

    x = new_x
    print(f"end    cycle={cycle} x={x} cont={cont} addr={addr}")


print(sum(results))
