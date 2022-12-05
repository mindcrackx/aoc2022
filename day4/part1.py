import re


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
    m = re.match(r"^(\d+)-(\d+),(\d+)-(\d+)$", line)
    a, b, c, d = int(m[1]), int(m[2]), int(m[3]), int(m[4])
    if a <= c and b >= d:
        count += 1
    elif c <= a and d >= b:
        count += 1

print(count)
