import re
from math import prod
from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=11)
    data = puzzle.input_data
    data = [x.split('\n') for x in data.split("\n\n")]
    return data


class Monkey:
    def __init__(self, monkey_list):
        self.monkey_number = int(re.findall(r'\d+', monkey_list[0])[0])
        self.item_list = [int(z) for z in re.findall(r'\d+', monkey_list[1])]
        self.op, factor = monkey_list[2].replace('Operation: new = old ', '').strip().split()
        self.factor = int(factor) if factor!= 'old' else 'old'
        self.div = int(re.findall(r'\d+', monkey_list[3])[0])
        self.div_true = int(re.findall(r'\d+', monkey_list[4])[0])
        self.div_false = int(re.findall(r'\d+', monkey_list[5])[0])
        self.c = 0

    @staticmethod
    def operands(oper, num1, num2, mod):
        ops = {'+': num1 + num2, '*': num1 * num2}
        return ops[oper] % mod

    def process(self, mk, mod):
        while len(self.item_list) > 0:
            self.c += + 1
            i = self.item_list.pop(0)
            n = i if self.factor == 'old' else self.factor
            i = self.operands(self.op, i, n, mod)
            target = self.div_true if i % self.div == 0 else self.div_false
            mk[target].item_list.append(i)


def monkey_game(rounds):
    monkey_list = get_puzzle()
    monkeys = [Monkey(m) for m in monkey_list]
    mod = prod([m.div for m in monkeys])
    for i in range(rounds):
        for m in monkeys:
            m.process(monkeys, mod)
    return prod(sorted([m.c for m in monkeys])[-2:])


print(f"Answer for part 1 is {monkey_game(20)}")
print(f"Answer for part 2 is {monkey_game(10000)}")
