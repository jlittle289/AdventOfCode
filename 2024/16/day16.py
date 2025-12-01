#!/usr/bin/python3

import time
import heapq
import pprint
from collections import defaultdict

DIRECTIONS = [
    (-1, 0),    # UP
    (0, 1),     # RIGHT
    (1, 0),     # DOWN
    (0, -1)     # LEFT
]

def main():
    with open("day16-test.input", "r") as file:
        maze = [list(line.strip()) for line in file]

    part1(maze)
    part2(maze)

def part1(maze):
    distances = dict()

    start = (len(maze) - 2, 1)
    end = (1, len(maze[0]) - 2)

    for row_index, row in enumerate(maze):
        for col_index, char in enumerate(row):
            if char == "#":
                continue
            distances[(row_index, col_index)] = [float("inf")] * len(DIRECTIONS)

    print(f"Start = {start}")
    print(f"End = {end}")

    st = time.time()

    heap:list[tuple[int, tuple[int,int]]] = []
    heapq.heappush(heap, (0, start))

    distances[start][1] = 0

    while heap:
        node_score, node = heapq.heappop(heap)
        node_row, node_col = node
        for move_index, (move_row, move_col) in enumerate(DIRECTIONS):
            next_row, next_col = (node_row + move_row, node_col + move_col)

            if maze[next_row][next_col] == '#':
                continue

            node_dists = distances[(next_row, next_col)]
            score = node_score + (1001 if distances[node][move_index] == float("inf") else 1)

            if node_dists[move_index] > score:
                node_dists[move_index] = score
                heapq.heappush(heap, (score, (next_row, next_col)))

    print(f"Part 1: End score = {min(distances[end])}")
    print(f"\tTime: {time.time() - st}s\n")

def part2(maze):
    distances = defaultdict(lambda:(float("inf"), set()))

    start = (len(maze) - 2, 1)
    end = (1, len(maze[0]) - 2)

    print(f"Start = {start}")
    print(f"End = {end}\n")

    st = time.time()
    heap:list[tuple[int, tuple[int,int]]] = []
    heapq.heappush(heap, (0, start, 1))

    distances[start, 1] = (0, set())

    print(distances[start, 1])
    while heap:
        node_score, node, dir_index = heapq.heappop(heap)
        node_row, node_col = node
        _, previous_state = distances[node, dir_index]

        for move_index in range(-1, 2):
            direction = (move_index + dir_index) % 4
            (move_row, move_col) = DIRECTIONS[direction]
            next_row, next_col = (node_row + move_row, node_col + move_col)

            if maze[next_row][next_col] == '#':
                continue

            next_score, _ = distances[(next_row, next_col), move_index]

            score = node_score + 1 + 1000*(move_index != dir_index)
            new_path = previous_state | {(next_row, next_col)}

            if next_score > score:
                distances[(next_row, next_col), direction] = (score, new_path)

                print(f"Update {(next_row,next_col)} : {(score, new_path)}")
                heapq.heappush(heap, (score, (next_row, next_col), move_index))

            elif score == next_score:
                 print(f"{(next_row, next_col)} : ({next_score=}, {previous_state=}")
                 heapq.heappush(heap, (score, (next_row, next_col), move_index))

    print(f"Part 2: Total seats = {distances[end]}")
    print(f"\tTime: {time.time() - st}s\n")

if __name__ == "__main__":
    main()