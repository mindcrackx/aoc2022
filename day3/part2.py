data = open("input.txt", "r", encoding="utf-8").read().splitlines()

# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """.splitlines()

result = 0
for x in range(0, len(data), 3):
    line1, line2, line3 = data[x], data[x + 1], data[x + 2]

    intersect = set(line1).intersection(set(line2), set(line3))

    val = list(intersect)[0]
    if val.upper() == val:
        num = ord(val) - 38
    else:
        num = ord(val) - 96
    result += num

print(result)
