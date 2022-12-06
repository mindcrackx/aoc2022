data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


#  data = test_data()

x = 4
for start in range(len(data) - 14):
    if len(set(data[start : start + x])) == x:
        print(start + x)
        break
