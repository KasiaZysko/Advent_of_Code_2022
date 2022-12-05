from aocd.models import Puzzle

"""
Remember to add AOC_SESSION as an environment variable. It is a cookie from AOC website called session.
"""


def get_puzzle():
    puzzle = Puzzle(year=2022, day=5)
    data = puzzle.input_data
    data = [line for line in data.split("\n\n")]

    moves = [(int(line.split()[1]), int(line.split()[3]), int(line.split()[5])) for line in data[1].split("\n")]
    containers_data = data[0].split("\n")[:-1]
    containers_data = [[line[j * 4:(j * 4) + 3][1] for j in range(0, 9)] for line in containers_data]
    container_dict = {i: [] for i in range(1, 10)}
    for container in containers_data:
        for i in range(9):
            if container[i] != " ":
                container_dict[i + 1].insert(0, container[i])

    return container_dict, moves


def part_1():
    container_dict, moves = get_puzzle()

    for move in moves:
        for k in range(move[0]):
            moved_item = container_dict[move[1]].pop()
            container_dict[move[2]].append(moved_item)

    return "".join([container_dict[i][-1] for i in range(1, 10)])


def part_2():
    container_dict, moves = get_puzzle()
    for move in moves:
        lenght = len(container_dict[move[1]])
        moved_item = container_dict[move[1]][lenght - move[0]:]
        del container_dict[move[1]][lenght - move[0]:]
        container_dict[move[2]].extend(moved_item)

    return "".join([container_dict[i][-1] for i in range(1, 10)])


print(f"Answer for part 1 is {part_1()}")
print(f"Answer for part 2 is {part_2()}")
