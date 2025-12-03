#!/bin/python3
import time

TEST="""987654321111111
811111111111119
234234234234278
818181911112111"""

def find_high_value_recursive(string:str, required) -> str:
    if required < 0:
         return ""

    for num in range(9,0,-1):
            num_index = string.find(str(num))
            if num_index != -1 and num_index < (len(string) - required):
                return string[num_index] + find_high_value_recursive(string[num_index+1:], required-1)

    raise ValueError("No numbers found!")

def part1(banks:list[str]):

    joltages = []

    NUM_BATTERIES = 2

    for bank in banks:
         joltages.append(int(find_high_value_recursive(bank, NUM_BATTERIES - 1)))

    return sum(joltages)

def part2(banks:list[str]):
    joltages = []

    NUM_BATTERIES = 12

    for bank in banks:
         joltages.append(int(find_high_value_recursive(bank, NUM_BATTERIES - 1)))

    return sum(joltages)



if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = DATA

    INPUT_DATA = INPUT_DATA.strip().split()

    start_time = time.time()
    print(f"Part 1: {part1(INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(INPUT_DATA)} - {time.time() - start_time:.6f}s")