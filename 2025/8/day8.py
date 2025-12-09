#!/bin/python3
import time
import math
import networkx as nx

def euc_distance(one, two):
    x1,y1,z1 = one
    x2,y2,z2 = two
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def part1(points:list[tuple], num_con):

    distances = [(points[i], sub_point) for i in range(len(points)-1) for sub_point in points[i+1:]]
    distances.sort(key=lambda x:euc_distance(x[0], x[1]))
    
    G = nx.Graph()
    for u,v in distances[:num_con]:
        G.add_edge(u,v)

    return math.prod(sorted(map(len,nx.connected_components(G)))[-3:])

def part2(points:list[tuple], num_con):

    G = nx.Graph()
    G.add_nodes_from(points)

    distances = [(points[i], sub_point) for i in range(len(points)-1) for sub_point in points[i+1:]]
    distances.sort(key=lambda x:euc_distance(x[0], x[1]))

    for u,v in distances[:num_con]:
        G.add_edge(u,v)

    for u,v in distances[num_con:]:
        G.add_edge(u,v)
        if len(list(nx.connected_components(G))) == 1:
            return u[0] * v[0]

    return 0

def process_input(data:str) ->list[tuple]:
    return [tuple(map(int, row.split(","))) for row in data.strip().splitlines()]

if __name__ == "__main__":
    with open("input.txt") as file:
        DATA = file.read().strip()

    INPUT_DATA = process_input(DATA)
    CONNECTIONS = 1000

    start_time = time.time()
    print(f"Part 1: {part1(INPUT_DATA, CONNECTIONS)} - {time.time() - start_time:.6f}s\n")

    start_time = time.time()
    print(f"Part 2: {part2(INPUT_DATA, CONNECTIONS)} - {time.time() - start_time:.6f}s")