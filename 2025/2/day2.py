#!/bin/python3
import time

TEST="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

DATA = ""

def has_odd_digits(num:str):
    return len(num) % 2 == 1

factor_cache = {}
def factor_digits(num:str):
    if len(num) not in factor_cache:
        factors = [div for div in range(1,len(num)//2 + 1) if len(num) % div == 0]
        factor_cache[len(num)] = factors

    return factor_cache[len(num)]

def part1(input:list[tuple[str,str]]):
    total = 0

    for low, high in input:
        if has_odd_digits(low) and has_odd_digits(high):
            continue

        if has_odd_digits(low):
            low = "1" + "0" * len(low)

        if has_odd_digits(high):
            high = "9" * (len(high) - 1)

        target = low[0:len(low)//2]

        while int(target*2) <= int(high):
            if int(target*2) in range(int(low), int(high) + 1):
                total += int(target*2)
            target = str(int(target)+1)

    return total

def part2(input:list[tuple[str,str]]):
    finds = set()

    for low,high in input:
        factors = factor_digits(low)

        for factor in factors:
            target:str = low[0:factor]
            inverse:int = len(low)//factor

            while int(target*inverse) <= int(high):
                if int(target*inverse) in range(int(low), int(high) + 1):
                    finds.add(target*inverse)

                target = str(int(target)+1)

    return sum(map(int, finds))

def parse_ranges(input:str):
    ranges = input.split(",")
    ranges = [tuple(code_range.split("-")) for code_range in ranges]

    remove = []

    # Clean up ranges by spliting ranges that span multiple string lengths
    # ex. 98-105 -> 98-99, 100-105
    for low, high in ranges:
        if len(low) != len(high):
            low_range = (low, "9" * len(low))
            high_range = ("1" + "0"*(len(high)-1), high)

            remove.append((low, high))

            ranges.append(low_range)
            ranges.append(high_range)

    for range in remove:
        ranges.remove(range)

    return ranges

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = TEST

    ranges = parse_ranges(INPUT_DATA)

    start_time = time.time()
    print(f"Part 1: {part1(ranges)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(ranges)} - {time.time() - start_time:.6f}s")