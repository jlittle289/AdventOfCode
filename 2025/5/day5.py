#!/bin/python3
import time

TEST="""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def part1(ranges:list[tuple[int, int]], ids:list[int]):

    fresh = 0

    for id in ids:
        for low, high in ranges:
            if low > id:
                break
            if id in range(low, high+1):
                fresh += 1
                break

    return fresh

def part2(ranges:list[tuple[int,int]], _):

    total = 0

    for low, high in ranges:
        total += len(range(low, high+1))

    return total

def merge_ranges(ranges: list[tuple[int,int]]):
    merged_ranges = []
    index = 0
    while index < len(ranges):
        low, high = ranges[index]
        merged = 0
        for sub_low, sub_high in ranges[index+1:]:
            if (sub_low > high):
                break
            low = min(low, sub_low)
            high = max(high, sub_high)
            merged += 1

        merged_ranges.append((low, high))
        index += merged + 1

    return merged_ranges

def process_input(raw:str):
    ranges = raw.split("\n\n")[0].split()
    ranges = [tuple(map(int,x.split("-"))) for x in ranges]
    ranges.sort()

    ranges = merge_ranges(ranges)

    ingredients = list(map(int, raw.split("\n\n")[1].split()))
    ingredients.sort()

    return ranges, ingredients


if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = process_input(DATA)

    start_time = time.time()
    print(f"Part 1: {part1(*INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(*INPUT_DATA)} - {time.time() - start_time:.6f}s")