from typing import List, Tuple, Set
from collections import deque

data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


# data = test_data()


def compare(a, b) -> int:
    match (a, b):
        case (int(), int()):
            return a - b
        case (int(), list()):
            return compare([a], b)
        case (list(), int()):
            return compare(a, [b])
        case (list(), list()):
            for x, y in zip(a, b):
                c = compare(x, y)
                if c == 0:
                    continue
                return c
            return len(a) - len(b)


indices = []
for i, chunk in enumerate(data.split("\n\n"), start=1):
    left_packet, right_packet = chunk.splitlines()
    # NOT SAFE!
    left, right = eval(left_packet), eval(right_packet)
    if compare(left, right) < 0:
        indices.append(i)

print(sum(indices))
