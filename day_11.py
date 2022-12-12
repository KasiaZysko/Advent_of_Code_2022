import re
import operator
from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=11)
    data = puzzle.input_data
    data = [x.split('\n') for x in data.split("\n\n")]
    return data


def create_monkey_list():
    data = get_puzzle()
    monkey_dictionary = {}
    for x in data:
        monkey_number = int(x[0].replace('Monkey ', '').replace(':', ""))
        item_list = [int(z) for z in re.findall(r'\d+', x[1])]
        operation_sign = x[2].replace('Operation: new = old ', '').strip().split()
        division = int(re.findall(r'\d+', x[3])[0])
        division_true = int(re.findall(r'\d+', x[4])[0])
        division_false = int(re.findall(r'\d+', x[5])[0])
        monkey_dictionary[monkey_number] = {'items': item_list, 'operation': operation_sign,
                                            'division': [division, division_true, division_false]}
    return monkey_dictionary


def operands(oper, num1, num2):
    ops = {'+': operator.add, '*': operator.mul}
    return ops[oper](num1, num2)


def part_1():
    data_dict = create_monkey_list()
    value_of = [0 for x in range(8)]

    for i in range(20):
        for key in data_dict:
            for item in data_dict[key]['items']:
                value_of[key] = value_of[key] + 1
                operation = int(data_dict[key]['operation'][1]) if data_dict[key]['operation'][1] != 'old' else item
                opp = operands(data_dict[key]['operation'][0], item, operation)
                new_worry_level = opp // 3
                if new_worry_level % data_dict[key]['division'][0] == 0:
                    new_monkey = data_dict[key]['division'][1]
                else:
                    new_monkey = data_dict[key]['division'][2]
                data_dict[new_monkey]['items'].append(new_worry_level)
            data_dict[key]['items'] = []

    return sorted(value_of)[::-1][0] * sorted(value_of)[::-1][1]


def part_2():
    pass


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is : \n {part_2()}")
