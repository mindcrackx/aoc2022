from heapq import nlargest

data = open("input.txt", "r", encoding="utf-8").read()

calories = []
for chunk in data.split("\n\n"):
    calories.append(sum(map(int, chunk.splitlines())))

print(sum(nlargest(3, calories)))
