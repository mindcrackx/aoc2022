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


packets = []
for line in data.splitlines():
    if line == "":
        continue
    # NOT SAFE!
    packets.append(eval(line))
packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key

packets.sort(key=cmp_to_key(compare))

import math

print(
    math.prod([i for i, x in enumerate(packets, start=1) if x == [[2]] or x == [[6]]])
)
