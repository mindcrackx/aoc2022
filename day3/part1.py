data = open("input.txt", "r", encoding="utf-8").read().splitlines()

# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """.splitlines()

result = 0
for line in data:
    left, right = line[: len(line) // 2], line[len(line) // 2 :]
    x = set(left).intersection(set(right))
    val = list(x)[0]
    if val.upper() == val:
        num = ord(val) - 38
    else:
        num = ord(val) - 96
    result += num

print(result)
