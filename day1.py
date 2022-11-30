from aocd.models import Puzzle
"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=1)
    data = puzzle.input_data
    data_split = [line for line in data.split("\n")]
    return data_split
