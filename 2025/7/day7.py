#!/bin/python3
import time
from itertools import groupby

TEST=""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

def part1(start, splitters, _):
    num_hits = 0
    active = {start[1]}

    for i, row in enumerate(splitters):
        new_active = set()

        for col in active:
            if (i,col) in row:
                num_hits += 1
                new_active.update([col-1, col+1])
            else:
                new_active.add(col)

        active = new_active

    return num_hits

def part2(start, splitters, length):

    total = [0] * length
    total[start[1]] = 1

    active = {start[1]}

    for i, row in enumerate(splitters):
        new_active = set()
        for col in active:
            if (i,col) in row:
                total[col-1] += total[col]
                total[col+1] += total[col]
                total[col] = 0
                new_active.update([col-1, col+1])
            else:
                new_active.add(col)

        active = new_active

    return sum(total)

def process_input(data:str) -> tuple[tuple,list[tuple[int,int]], int]:
    rows = data.strip().splitlines()
    start = (0, rows[0].find("S"))

    splitters = []
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            if col == "^":
                splitters.append(((i//2 - 1),j))

    splitters = [list(g) for _, g in groupby(splitters, lambda x: x[0])]

    return start, splitters, len(rows[0])

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = DATA

    INPUT_DATA = process_input(INPUT_DATA)

    start_time = time.time()
    print(f"Part 1: {part1(*INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(*INPUT_DATA)} - {time.time() - start_time:.6f}s")