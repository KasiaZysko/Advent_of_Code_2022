from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=2)
    data = puzzle.input_data
    data = [line for line in data.split("\n")]
    data = [game.split(" ") for game in data]
    return data


def part_1():
    data = get_puzzle()
    choice_dict = {
        "X": {"Score": 1, "A": 3, "B": 0, "C": 6},
        "Y": {"Score": 2, "A": 6, "B": 3, "C": 0},
        "Z": {"Score": 3, "A": 0, "B": 6, "C": 3}
    }
    score = 0
    for player1, player2 in data:
        score += choice_dict[player2][player1] + choice_dict[player2]["Score"]

    return score


def part_2():
    data = get_puzzle()
    choice_dict = {
        "X": {"Score": 0, "A": 3, "B": 1, "C": 2},
        "Y": {"Score": 3, "A": 1, "B": 2, "C": 3},
        "Z": {"Score": 6, "A": 2, "B": 3, "C": 1}
    }
    score = 0
    for player1, player2 in data:
        score += choice_dict[player2][player1] + choice_dict[player2]["Score"]

    return score


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
