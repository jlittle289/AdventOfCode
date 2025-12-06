#!/bin/python3
import time
import math
import itertools

TEST="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
DATA = ""

def transpose_2d(matrix: list[list]):
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

def part1(text:str):
    total = 0

    rows = text.split("\n")
    operations = rows.pop().split()

    rows = [row.split() for row in rows]

    problems = [[int(row[i]) for row in rows] for i in range(len(operations))]

    for i, op in enumerate(operations):
        if op == "+":
            value = sum(problems[i])
        else:
            value = math.prod(problems[i])

        total += value

    return total

def part2(text:str):
    total = 0

    rows = text.split("\n")
    operations = rows.pop().split()
    
    t = transpose_2d(rows)
    combine = ["".join(x) for x in t]
    
    problems = [list(map(int, group)) for key, group in itertools.groupby(combine, lambda x: not x.split()) if not key]
    
    for i, op in enumerate(operations):
        if op == "+":
            value = sum(problems[i])
        else:
            value = math.prod(problems[i])
        total += value

    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = DATA

    start_time = time.time()
    print(f"Part 1: {part1(INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(INPUT_DATA)} - {time.time() - start_time:.6f}s")