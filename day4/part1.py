data = open("input.txt", "r", encoding="utf-8").read().splitlines()


def test_input():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()


# data = test_input()


count = 0
for line in data:
    left, right = line.split(",")
    a, b = left.split("-")
    c, d = right.split("-")
    # got stuck ~ 16 minutes until i realized i forgot to convert to ints...
    a, b, c, d = int(a), int(b), int(c), int(d)
    if a <= c and b >= d:
        count += 1
    elif c <= a and d >= b:
        count += 1

print(count)
