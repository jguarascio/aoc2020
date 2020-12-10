import math
from numpy import loadtxt

lines = []
graph = {}


def setup():
    global lines, graph
    lines = loadtxt("day10.txt", dtype="int")

    # Build graph
    graph[max(lines)] = [max(lines) + 3]  # This is the last hop adapter
    #graph[max(lines) + 3] = []  # Node of last hop adapter
    queue = [0]
    while queue:
        jolt = queue.pop(0)
        min_jolt = jolt + 1
        max_jolt = jolt + 3
        options = [item for item in lines if item >= min_jolt and item <= max_jolt]
        if options != []:
            graph[jolt] = options
        
        queue.extend(item for item in options if item not in queue)
    
    print(lines)
    print(graph)


def part1():
    
    # Walk the graph
    count1 = 0
    count3 = 0
    for key in graph:
        if graph[key] != []: 
            diff = min(graph[key]) - key
            if diff == 1: count1 += 1
            if diff == 3: count3 += 1

    print(f'{count1=} {count3=} ')

    return
 

def part2():

    # Set up a dynamic programming solution
    path_count = {}
    for key in sorted(graph):
        path_count[key] = 0

    path_count[0] = 1
    for i in path_count:
        for j in range(1, 3+1):
            if i - j in path_count:
                path_count[i] += path_count[i-j]

    print(path_count)

    return

def main():
    setup()
    part1()
    part2()

if __name__ == "__main__":
    main()