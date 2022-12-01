data = open("input.txt", "r", encoding="utf-8").read().splitlines()

old = -1000
new = 0
sum_max = 0
for x in data:
    if x == "":
        if sum_max < new:
            sum_max = new
        old = new
        new = 0
        continue
    new += int(x)
if sum_max < new:
    sum_max = new

print("=" * 10)
print(sum_max)
