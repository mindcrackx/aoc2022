data = open("input.txt", "r", encoding="utf-8").read().splitlines()

old = -1000
new = 0
sumall = []
for x in data:
    if x == "":
        sumall.append(new)
        old = new
        new = 0
        continue

    new += int(x)
sumall.append(new)

s = sorted(sumall, reverse=True)
print("========")
print(sum([s[0], s[1], s[2]]))
