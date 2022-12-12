from typing import List
import math

data = open("input.txt", "r", encoding="utf-8").read()


def test_data():
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


# data = test_data()

monkeys_str = data.split("\n\n")


class Monkey:
    def __init__(self, starting_items, operation, test, test_true, test_false):
        self._starting_items: List[int] = starting_items
        self._operation: str = operation
        self._test: str = test
        self._divisor: int = int(test.split("divisible by ")[1])
        self._test_true: int = test_true
        self._test_false: int = test_false

        self.inspect_count = 0

    @classmethod
    def from_string(cls, s: str):
        starting_items = None
        operation = None
        test = None
        test_true = None
        test_false = None
        for line in s.splitlines():
            if line.startswith("  Starting items: "):
                starting_items = [
                    int(x) for x in line.split("  Starting items: ")[1].split(",")
                ]
            if line.startswith("  Operation: "):
                operation = line.split("  Operation: ")[1]
            if line.startswith("  Test: "):
                test = line.split("  Test: ")[1]
            if line.startswith("    If true: "):
                test_true = int(line.split("    If true: throw to monkey ")[1])
            if line.startswith("    If false: "):
                test_false = int(line.split("    If false: throw to monkey ")[1])

        return cls(starting_items, operation, test, test_true, test_false)

    def worry_level(self, item: int, lcm: int) -> int:
        op = self._operation.replace("old", str(item))
        op = op.replace("new", "item")
        # NOT SAFE!!
        _locals = locals()
        exec(op, _locals)
        return _locals["item"] % lcm

    def throw_to(self, item):
        # item = item // 3
        if self._test.startswith("divisible by "):
            return (
                self._test_true
                if item % int(self._test.split("divisible by ")[1]) == 0
                else self._test_false
            ), item
        else:
            raise ValueError("unknown test:", self._test)

    def catch(self, item):
        self._starting_items.append(item)

    def throw(self, lcm: int):
        if len(self._starting_items) is None:
            return
        self.inspect_count += 1
        item = self._starting_items[0]
        self._starting_items = self._starting_items[1:]
        item = self.worry_level(item, lcm)
        return self.throw_to(item)

    def can_throw(self):
        return len(self._starting_items) > 0


monkeys: List[Monkey] = []
for monkey_str in monkeys_str:
    monkeys.append(Monkey.from_string(monkey_str))


div_lcm = math.lcm(*[m._divisor for m in monkeys])

round = 0
while round != 10_000:
    for monkey in monkeys:
        while monkey.can_throw():
            throw = monkey.throw(div_lcm)
            monkeys[throw[0]].catch(throw[1])
    round += 1

catchnums = [m.inspect_count for m in monkeys]
catchnums.sort(reverse=True)
print(catchnums[0] * catchnums[1])
