from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=3)
    data = puzzle.input_data
    data = [line for line in data.split("\n")]
    return data


def part_1():
    data = get_puzzle()
    value_list = [(string[:len(string) // 2], string[len(string) // 2:]) for string in data]
    compartments = [''.join(set(compartment[0]).intersection(compartment[1])) for compartment in value_list]
    values = [ord(i) - 96 if i.islower() else ord(i) - 38 for i in compartments]
    return sum(values)


def part_2():
    data = get_puzzle()
    value_list = [data[3 * i:3 * i + 3] for i in range(int(len(data) / 3))]
    compartments = [''.join(set(compartment[0]).intersection(compartment[1]).intersection(compartment[2])) for
                    compartment in value_list]
    values = [ord(i) - 96 if i.islower() else ord(i) - 38 for i in compartments]
    return sum(values)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
