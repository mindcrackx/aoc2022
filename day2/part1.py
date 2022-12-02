data = open("input.txt", "r", encoding="utf-8").read().splitlines()

# data = """A Y
# B X
# C Z""".splitlines()

# 1 rock
# 2 paper
# 3 scissors
# 0 loss
# 3 draw
# 6 win

score = 0
for line in data:
    a, b = line.split()
    if b == "X":  # rock
        score += 1
        if a == "A":
            score += 3
        elif a == "B":
            score += 0
        elif a == "C":
            score += 6

    elif b == "Y":  # paper
        score += 2
        if a == "A":
            score += 6
        elif a == "B":
            score += 3
        elif a == "C":
            score += 0

    elif b == "Z":  # scissors
        score += 3
        if a == "A":
            score += 0
        elif a == "B":
            score += 6
        elif a == "C":
            score += 3

print(score)
