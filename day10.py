import itertools
from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=10)
    data = puzzle.input_data
    data = [x.split() for x in data.split("\n")]
    return data


def sum_until_index(data, limit):
    data_zip = list(zip(*data))
    i = 0
    while sum(data_zip[0][:i + 1]) < limit:
        i += 1
    return sum(data_zip[1][:i])


def part_1():
    data = get_puzzle()
    data = [(1, 0) if x[0] == 'noop' else (2, int(x[1])) for x in data]
    signal_strength = 0
    for x in [20, 60, 100, 140, 180, 220]:
        signal_strength += ((sum_until_index(data, x) + 1) * x)
    return signal_strength


def part_2():
    data = get_puzzle()
    output = []
    for line in data:
        output.append(0)
        if not line[0] == 'noop':
            output.append(int(line[1]))
    register = list(itertools.accumulate(output, initial=1))
    pixels = list([0 for _ in range(40)] for _ in range(6))
    for cycle in range(240):
        is_pixel_on = int(abs(register[cycle] - cycle % 40) <= 1)
        pixels[cycle // 40][cycle % 40] = "#" if is_pixel_on else "."

    return "\n".join(["".join(x) for x in pixels])


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is : \n {part_2()}")

