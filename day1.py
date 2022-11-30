from aocd.models import Puzzle


def get_puzzle():
    puzzle = Puzzle(year=2022, day=1)
    data = puzzle.input_data
    data_split = [line for line in data.split("\n")]
    return data_split
