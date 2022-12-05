from dataclasses import dataclass
import re
from typing import List

data = open("input.txt", "r", encoding="utf-8").read().splitlines()


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


header = True
steps: List[Step] = []
crates_reversed = [[] for x in range(int((len(data[0]) + 1) / 4))]
for line in data:
    if header and line == "":
        header = False
        continue

    if not header:
        m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        steps.append(Step(src=int(m[2]), dst=int(m[3]), amt=int(m[1])))
    else:
        count = int((len(line) + 1) / 4)
        if line[1].isdigit():
            continue
        line = " " + line
        for x, i in enumerate(range(1, count * 4, 4)):
            tmp = line[i + 1 : i + 2]
            if tmp != " ":
                crates_reversed[x].append(tmp)

crates = [[]] * len(crates_reversed)
for i, crate in enumerate(crates_reversed):
    crates[i] = crate[::-1]

for step in steps:
    tmp = []
    for i in range(step.amt):
        tmp.append(crates[step.src - 1].pop())
    crates[step.dst - 1].extend(tmp[::-1])

result = "".join(crate[-1] for crate in crates)
print(result)
