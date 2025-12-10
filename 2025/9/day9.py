#!/bin/python3
import time

def area(point_set):
    point1, point2 = point_set
    return (abs(point1[0]-point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

def part1(points:list[tuple]):
    rects = [(points[i], sub_point) for i in range(len(points)-1) for sub_point in points[i+1:]]

    return max(map(area, rects))

def part2(points:list[tuple]):

    edges = [(points[i], points[i+1]) for i in range(len(points)-1)]
    edges.append((points[-1],points[0]))

    y_edges = [(p1,p2) for (p1,p2) in edges if p1[0] == p2[0]]
    x_edges = [(p1,p2) for (p1,p2) in edges if p1[1] == p2[1]]

    rects = [(points[i], sub_point) for i in range(len(points)-1) for sub_point in points[i+1:]]
    rects.sort(key=area, reverse=True)

    for p1, p2 in rects:
        
        minx = min(p1[0], p2[0])
        maxx = max(p1[0], p2[0])
        miny = min(p1[1], p2[1])
        maxy = max(p1[1], p2[1])

        invalid = False
        for y1, y2 in y_edges:
            lx = y1[0]

            if not (minx < lx < maxx):
                continue

            lminy = min(y1[1], y2[1])
            lmaxy = max(y1[1], y2[1])

            if (lminy <= miny < lmaxy) or (lminy < maxy <= lmaxy):
                invalid = True
                break

        if invalid:
            continue

        for x1, x2 in x_edges:
            ly = x1[1]

            if not (miny < ly < maxy):
                continue

            lminx = min(x1[0], x2[0])
            lmaxx = max(x1[0], x2[0])
            if (lminx <= minx < lmaxx) or (lminx < maxx <= lmaxx):
                invalid = True
                break

        if not invalid:
            return area((p1,p2))
        
    return 0

def process_input(data:str):
    return [tuple(map(int,point.split(","))) for point in data.split("\n")]

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = process_input(DATA)

    start_time = time.time()
    print(f"Part 1: {part1(INPUT_DATA)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(INPUT_DATA)} - {time.time() - start_time:.6f}s")