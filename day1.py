from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""

def get_puzzle():
    puzzle = Puzzle(year=2022, day=1)
    data = puzzle.input_data
    data = [line.split('\n') for line in data.split("\n\n")]
    data = [[int(x) for x in data] for data in data]
    data = [sum(x) for x in data]
    return data


def part_1():
    data = get_puzzle()
    return max(data)


def part_2():
    data = get_puzzle()
    calories = 0
    for i in range(3):
        calories += max(data)
        data.remove(max(data))

    return calories


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
