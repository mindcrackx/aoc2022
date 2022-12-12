from typing import List, Tuple, Set
from collections import deque
from tqdm import tqdm

data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


# data = test_data()
data = data.splitlines()

heightmap = []
for line in data:
    heightmap.append([*line])

# find coordinates for S and E
S_x, S_y, E_x, E_y = None, None, None, None
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        if heightmap[x][y] == "S":
            S_x, S_y = x, y
        if heightmap[x][y] == "E":
            E_x, E_y = x, y

print(S_x, S_y, E_x, E_y)
if S_x is None or S_y is None or E_x is None or E_y is None:
    raise ValueError("invalid coordinates for S or E")


def height(pos: Tuple[int, int]) -> int:
    if heightmap[pos[0]][pos[1]] == "S":
        return ord("a")
    if heightmap[pos[0]][pos[1]] == "E":
        return ord("z")
    return ord(heightmap[pos[0]][pos[1]])


def bfs(pos: Tuple[int, int], end: Tuple[int, int]):
    steps = [[0 for y in range(len(heightmap[x]))] for x in range(len(heightmap))]
    visited = set()
    visited.add(pos)
    que = deque()
    que.append(pos)
    while que:
        pos = que.popleft()
        # print("=" * 30)
        # print(pos, heightmap[pos[0]][pos[1]])
        for mov_x, mov_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = pos[0] + mov_x, pos[1] + mov_y
            if (
                0 <= i < len(heightmap)
                and 0 <= j < len(heightmap[i])
                and height((i, j)) <= height(pos) + 1
                and not (i, j) in visited
            ):
                visited.add((i, j))
                # print(visited)
                # for s in steps:
                # print(s)
                steps[i][j] = steps[pos[0]][pos[1]] + 1
                que.append((i, j))
    return steps[end[0]][end[1]]


starts = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        if heightmap[x][y] == "a":
            starts.append((x, y))
# print(starts)

steps = []
for start in tqdm(starts):  # remove tqdm if not installed
    step = bfs(start, (E_x, E_y))
    if step != 0:
        steps.append(step)
print(min(steps))
