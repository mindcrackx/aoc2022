from dataclasses import dataclass
import re
from typing import List

data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()


# data = test_data()


@dataclass
class Step:
    src: int
    dst: int
    amt: int


crates, moves = data.split("\n\n")
cols = {}
for *row, last in zip(*crates.split("\n")):
    if last.isdigit():
        cols[int(last)] = [x for x in row if x.isupper()]

steps: List[Step] = []
for line in moves.splitlines():
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    steps.append(Step(src=int(m[2]), dst=int(m[3]), amt=int(m[1])))

for key in cols.keys():
    cols[key] = cols[key][::-1]

for step in steps:
    tmp = []
    for i in range(step.amt):
        tmp.append(cols[step.src].pop())
    cols[step.dst].extend(tmp[::-1])

# always get top value
result = "".join([v0 for *_, v0 in cols.values()])
print(result)
exit()
