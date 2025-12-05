#!/bin/python3
import time

TEST="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

DATA = ""


def print_2d(table):
    for row in table:
        print(" ".join(map(str, row)))
    print()

check_list = {}
def get_checks(y,x):
    if (y,x) not in check_list:
        cells_y = list(map(lambda offset: y + offset, [-1, 0 , 1]))
        cells_x = list(map(lambda offset: x + offset, [-1, 0 , 1]))
        checks = [(row, col) for row in cells_y for col in cells_x if (row >= 0 and col >= 0)]
        checks.remove((y,x))

        check_list[(y,x)] = checks

    return check_list[(y,x)]

def part1(rolls:list[tuple[int,int]]):

    movable = 0
    for y, x in rolls:

        checks = get_checks(y,x)
        checks = [check for check in checks if check in rolls]

        if len(checks) < 4:
            movable += 1

    return movable

def part2(rolls:list):

    movable = 0

    cur_table = rolls.copy()
    touched = rolls.copy()

    while True:
        removed = []
        for y, x in touched:

            checks = get_checks(y,x)

            found = 0
            for check in checks:
                if check in cur_table and found < 4:
                    found += 1

            if found < 4:
                movable += 1
                removed.append((y,x))

        if not removed:
            break

        cur_table = [roll for roll in cur_table if roll not in removed]
        touched = set([cell for roll in removed for cell in get_checks(*roll) if cell in cur_table])

    return movable

def convert_entry(item:str):
    return 1 if item == "@" else 0

def process_input(input:str)-> list[tuple[int, int]]:

    table = input.split()

    rolls = [(y,x) for y, row in enumerate(table) for x, symbol in enumerate(row) if symbol == "@"]

    return rolls

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = DATA

    INPUT_DATA = process_input(INPUT_DATA)

    start_time = time.time()
    print(f"Part 1: {part1(INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(INPUT_DATA)} - {time.time() - start_time:.6f}s")