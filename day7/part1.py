from collections import defaultdict

data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


# data = test_data()

data = data.splitlines()

dirs = defaultdict(lambda: 0)
dir_paths = set()
path = ()
dirListing = False
for i in range(len(data)):
    line = data[i]
    if line == "$ cd /":
        path = []
        continue
    if line == "$ ls":
        continue
    if line == "$ cd ..":
        path.pop()
        continue
    if line.startswith("$ cd "):
        path.append(data[i].split(" ", 2)[2])
        continue

    left, right = data[i].split(" ")
    if left == "dir":
        dir_paths.add((*path, right))
    else:
        dirs[(*path, right,)] = int(left)


dir_sizes = {
    dp: sum(size for k, size in dirs.items() if "/".join(k).startswith("/".join(dp)))
    for dp in dir_paths
}

result = sum(val for val in dir_sizes.values() if val <= 100_000)
print(result)
