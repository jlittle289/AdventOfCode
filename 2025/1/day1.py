#!/bin/python3
TEST="""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

input = ""

def main(input:str):
    rotations = input.strip().split("\n")
    zeroes = 0
    current = 50

    for rot in rotations:
        right = rot[0] == "R"
        num = int(rot[1:])

        current = current + num if right else current - num
        current = current % 100

        if current == 0:
            zeroes += 1

    print(f"Part 1 Zeroes: {zeroes}" )

def part2(input:str):
    rotations = input.strip().split("\n")
    zeroes = 0
    current = 50

    for rot in rotations:

        right = rot[0] == "R"
        num = int(rot[1:])

        new = current + num if right else current - num

        if new <= 0:
            zeroes += int(abs(new / 100) + 1)

            if current == 0:
                zeroes -= 1

        elif new >= 100:
            zeroes += int(abs(new / 100))

        current = new % 100

    print(f"Part 2 Zeroes: {zeroes}" )

if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()

    main(input)

    part2(input)