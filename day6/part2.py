data = open("input.txt", "r", encoding="utf-8").read()

x = 14
for start in range(len(data) - 14):
    if len(set(data[start : start + x])) == x:
        print(start + x)
        break
