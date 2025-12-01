#!/usr/bin/python3

import time
from PIL import Image

WIDTH = 101
HEIGHT = 103

TEST_WIDTH = 11
TEST_HEIGHT = 7

GRID_WIDTH = WIDTH
GRID_HEIGHT = HEIGHT

TIME = 100
EMPTY = "." * GRID_WIDTH

def main():
    with open("day14.input", "r") as file:
        robots = [tuple([int(x) for thing in robot.split() for x in thing.split(",")]) for robot in file.read().replace("p=","").replace("v=","").split("\n") ]

    st = time.time()
    part1(robots)
    print(f"\tTime: {time.time() - st}\n")

    st = time.time()
    part2(robots)
    print(f"\tTime: {time.time() - st}\n")


def part1(robots:list[tuple[int,int,int,int]]):
    robo_map:dict[tuple[int,int],list[tuple[int,int]]] = dict()

    for robot in robots:
        px,py,vx,vy = robot
        if (px,py) not in robo_map:
            robo_map[(px,py)] = [(vx,vy)]
        else:
            robo_map[(px,py)].append((vx,vy))

    for _ in range(TIME):
        new_map:dict[tuple[int,int],list[tuple[int,int]]] = dict()
        for px,py in robo_map:
            for vx,vy in robo_map[(px,py)]:
                new_px = (px + vx) % GRID_WIDTH
                new_py = (py + vy) % GRID_HEIGHT

                if (new_px,new_py) not in new_map:
                    new_map[(new_px,new_py)] = [(vx,vy)]
                else:
                    new_map[(new_px,new_py)].append((vx,vy))
        robo_map = new_map

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    x_div = GRID_WIDTH // 2
    y_div = GRID_HEIGHT // 2

    for px,py in robo_map:
        if px == x_div or py == y_div:
            continue

        left = px < x_div
        right = px > x_div
        top = py < y_div
        bottom = py > y_div

        if left and top:
            q1 += len(robo_map[(px,py)])
            continue

        if left and bottom:
            q2 += len(robo_map[(px,py)])
            continue

        if right and top:
            q3 += len(robo_map[(px,py)])
            continue

        if right and bottom:
            q4 += len(robo_map[(px,py)])
            continue

    score = q1 * q2 * q3 * q4
    print(f"Security score: {score}")

def part2(robots:list[tuple[int,int,int,int]]):
    robo_map:dict[tuple[int,int],list[tuple[int,int]]] = dict()

    for robot in robots:
        px,py,vx,vy = robot
        if (px,py) not in robo_map:
            robo_map[(px,py)] = [(vx,vy)]
        else:
            robo_map[(px,py)].append((vx,vy))

    offset = 0
    IMAGE_WIDTH = GRID_WIDTH * (GRID_HEIGHT - offset)
    IMAGE_HEIGHT = GRID_WIDTH * ( GRID_HEIGHT + offset)

    img = Image.new("1", (IMAGE_WIDTH, IMAGE_HEIGHT), (0))
    for sec in range(GRID_WIDTH * GRID_HEIGHT):
        new_map:dict[tuple[int,int],list[tuple[int,int]]] = dict()
        for px,py in robo_map:
            for vx,vy in robo_map[(px,py)]:
                new_px = (px + vx) % GRID_WIDTH
                new_py = (py + vy) % GRID_HEIGHT

                try:
                    img.putpixel((new_px + ((sec % (GRID_HEIGHT - offset)) * GRID_WIDTH) , new_py + ((sec // (GRID_HEIGHT - offset)) * GRID_HEIGHT)), (1))
                except IndexError:
                    print(f"Sec {sec} : {(new_px, new_py)} -> {(new_px + ((sec % (GRID_HEIGHT - offset)) * GRID_WIDTH) , new_py + ((sec // (GRID_HEIGHT - offset)) * GRID_HEIGHT))}")
                    img.show()
                    exit()

                if (new_px,new_py) not in new_map:
                    new_map[(new_px,new_py)] = [(vx,vy)]
                else:
                    new_map[(new_px,new_py)].append((vx,vy))
        robo_map = new_map

        # Detect some sort of tree
        if detect_tree(robo_map):
            plot:list[str] = []

            for _ in range(GRID_HEIGHT):
                plot.append(EMPTY)


            for px, py in robo_map:
                line = plot[py]
                line = line[:px] + "#" + line[px+1:]
                plot[py] = line

            print(f"\nSecond: {sec}")
            for line in plot:
                print(line)

    img.show()

def detect_tree(robo_map):
    # Detect some sort of tree
    for px, py in robo_map:
        if (
            (px, py + 1) in robo_map
            and (px + 1, py) in robo_map
            and (px + 1, py + 1) in robo_map
            and (px + 2, py) in robo_map
            and (px + 2, py + 1) in robo_map
            and (px + 2, py + 2) in robo_map
            and (px + 1, py + 2) in robo_map
            and (px, py + 2) in robo_map
        ):
            return True

    return False

if __name__ == "__main__":
    main()