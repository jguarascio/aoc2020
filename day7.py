import re
import string


def setup():
    text_file = open("day7.txt", "r")
    rules = text_file.read().splitlines()
    text_file.close()

    # build graph
    graph = {}
    for rule in rules:
        rule = rule.replace("bags","")
        rule = rule.replace("bag","")
        rule = rule.replace(".","")
        rule = rule.replace("contain",",")
        list = rule.split(",")
        list = [item.strip() for item in list]
        list = [item.replace("no other","") for item in list]

        if list[1] == "":
            graph[list[0]] = []
        else:
            graph[list[0]] = [(item.split(" ", 1)[1], item.split(" ", 1)[0]) for item in list[1:]]

    return graph

def part1():
    node = 'shiny gold'
    graph = setup()

    queue = []     #Initialize a queue
    result = set()

    for key in graph:
        if node in [item[0] for item in graph[key]]:
            queue.append(key)

    while queue:
        s = queue.pop(0) 
        #print (s, end = "->") 
        result.add(s)

        for key in graph:
            if s in [item[0] for item in graph[key]]:
                queue.append(key)

    #print(result)
    print(f'{len(result)=}')

    return

def part2():
    graph = setup()
    node = 'shiny gold'

    # Modified BFS algorithm
    queue = []     #Initialize a queue
    queue.append(node)

    total_bags = 0
    while queue:
        s = queue.pop(0) 
        #print (s, end = " ") 

        bags = 0
        for neighbour in graph[s]:
            bags += int(neighbour[1])
            for i in range(0,int(neighbour[1])):
                queue.append(neighbour[0])
        total_bags += bags

        #print(bags, end = " ")
    
    print(f'{total_bags=}')

    return

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()