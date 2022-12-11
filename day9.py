from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session..
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=9)
    data = puzzle.input_data
    data = [[line.split()[0], int(line.split()[1])] for line in data.split("\n")]
    return data


def move_tail(head: list[int], tail: list[int]) -> None:
    distance_diff = [x - y for x, y in zip(head, tail)]
    if abs(distance_diff[0]) > 1 or abs(distance_diff[1]) > 1:
        tail[:] = [n + (1 if diff_n >= 1 else -1 if diff_n <= -1 else 0) for n, diff_n in zip(tail, distance_diff)]


def part_1():
    data = get_puzzle()
    visited_by_tail = set()
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    head = [0, 0]
    tail = [0, 0]
    for direction, amount in data:
        for i in range(amount):
            head = [x + y for x, y in zip(head, directions[direction])]
            move_tail(head, tail)
            visited_by_tail.add(tuple(tail))

    return len(visited_by_tail)


def part_2():
    data = get_puzzle()
    visited_by_tail = set()
    tail_parts = list([0, 0] for i in range(9))
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    head = [0, 0]
    for direction, amount in data:
        for i in range(amount):
            head = [x + y for x, y in zip(head, directions[direction])]
            for j in range(len(tail_parts)):
                move_tail(head if j == 0 else tail_parts[j - 1], tail_parts[j])
                if j == 8:
                    visited_by_tail.add(tuple(tail_parts[j]))
    return len(visited_by_tail)


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
