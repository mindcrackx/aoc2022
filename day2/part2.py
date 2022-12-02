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
    if b == "X":  # lose
        score += 0
        if a == "A":
            score += 3
        elif a == "B":
            score += 1
        elif a == "C":
            score += 2

    elif b == "Y":  # draw
        score += 3
        if a == "A":
            score += 1
        elif a == "B":
            score += 2
        elif a == "C":
            score += 3

    elif b == "Z":  # win
        score += 6
        if a == "A":
            score += 2
        elif a == "B":
            score += 3
        elif a == "C":
            score += 1

print(score)
